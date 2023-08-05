#pragma once
// Copyright 2022 Jean-Marie Mirebeau, University Paris-Sud, CNRS, University Paris-Saclay
// Distributed WITHOUT ANY WARRANTY. Licensed under the Apache License, Version 2.0, see http://www.apache.org/licenses/LICENSE-2.0

/**
This file implements low-level GPU routines for the mincut problem.
*/

/** The following need to be defined in including file (example)
typedef int Int;
typedef float Scalar;
#define ndim_macro 3
#define rander_macro true
#define asym_macro false
const int newton_maxiter = 7;
// Subgrid used for gradient computation
const int shape_i[ndim] = {4,4,4}; 
const int size_i = 64;
const int shape_e[ndim] = {5,5,5};
const int size_e = 125;
*/

#include <cupy/complex.cuh>
typedef char int8;

typedef complex<Scalar> Complex;
#if   ndim_macro == 1
#include "Geometry1.h"
#elif ndim_macro == 2
#include "Geometry2.h"
#elif ndim_macro == 3
#include "Geometry3.h"
#else
STATIC_ASSERT(false,Unsupported_dimension);
#endif 

#undef bilevel_grid_macro
#include "Grid.h"

#define metric_type_iso 1
#define metric_type_iso_asym 2
#define metric_type_riemann 3
#define metric_type_riemann_asym 4
STATIC_ASSERT(1<=metric_type_macro && metric_type_macro<=4,Unsupported_metric_type);
STATIC_ASSERT(1<=ndim_macro && ndim_macro<=4,Unsupported_dimension);

// Dimension for the diagonal prox
const int pdim = (metric_type_macro == metric_type_iso_asym) ? 2 : ndim;

// Dimension for the quaternion data (d=3), or counterpart if d<3
const int qdim = (ndim_macro==1) ? 1: (ndim_macro==2) ? 2 : 4;
void copy_eigenvectors(const Scalar v0[qdim], Scalar v[__restrict__ ndim][ndim]){
#if ndim_macro==1 // 1D : there is only one possible eigenvector
	v[0][0]=1.; 
#elif ndim_macro==2 // 2D : importing only the first eigenvector, second one is perpendicular
	for(int i=0; i<ndim; ++i){v[0][i] = v0[i];} 
	perp_v(v[0],v[1]);
	trans_A(v);
#elif ndim_macro==3  // 3D : importing the eigenvector matrix as a unit quaternion
	Scalar q[qdim];
	for(int i=0; i<qdim; ++i){q[i] = v0[i];}
	rotation3_from_sphere3(q,v);
#endif
}

__constant__ Int shape_tot[ndim];
__constant__ Int size_tot; // product of shape_tot
__constant__ Scalar idx[ndim];  // inverse grid scale, along each axis
__constant__ Scalar tau, itau; // proximal time step, and its inverse

__constant__ Int shape_fft[ndim]; // The fft shape differs on the last axis
__constant__ Int size_fft;

__constant__ Int shape_o[ndim];

/** Squared modulus of a complex number */
Scalar norm2(const Complex & z){return z.real()*z.real()+z.imag()*z.imag();}

/**
Proximal operator argmin_sol (1/2) |sol-eta|^2 + a |sol|
*/
void prox_iso(
	const Scalar eta[ndim], // Projected variable
	const Scalar a, // norm multiplier
	Scalar sol[__restrict__ ndim] // minimizer
	){
	const Scalar norm = norm_v(eta);

	// Handle the case where the prox is at the origin
	if(norm<=a){zero_V(sol); return;}

	const Scalar k = Scalar(1)-a/norm;
	mul_kv(k,eta,sol);
}


/** 
Proximal operator argmin_sol (1/2)|sol-eta|^2 + sqrt(sol.m.sol),
where m is the diagonal matrix of eigenvalues lambda
*/
void prox_diagonal(
	const Scalar eta[pdim], // projected variable
	const Scalar lambda[pdim], // eigenvalues
	Scalar sol[__restrict__ pdim] // minimizer
	){ 
	// Since pdim!=ndim in general, we cannot use the Geometry_.h header here, e.g. norm2_v
	Scalar eta2[pdim];
	for(int i=0; i<pdim; ++i){eta2[i] = eta[i]*eta[i];}

	Scalar norm2=0.;
	for(int i=0; i<pdim; ++i){norm2 += eta2[i]/lambda[i];}

	// Handle the case where the prox is at the origin
	if(norm2<=1){for(int i=0; i<pdim; ++i) sol[i]=0.; return;}

	// Compute beta via a Newton method, solving the equation f(β)=0 where
	//f(β) = sum(λi*coef**2/(λi+β)**2,axis=0)-1.
	// The system should behave well enough that no damping or 
	// fancy stopping criterion is needed

	// Initial guess is exact in isotropic case
	Scalar lambda_min = lambda[0];
	for(int i=1; i<pdim; ++i) lambda_min = min(lambda_min,lambda[i]);
	Scalar beta = lambda_min * (sqrt(norm2)-1);
	Scalar lc2[pdim];
	for(int i=0; i<pdim; ++i){lc2[i]=lambda[i]*eta2[i];}

	for(int newton_iter=0; newton_iter<newton_maxiter; ++newton_iter){
		Scalar val = -Scalar(1); // f(β)
		Scalar der = Scalar(0);  // f'(β)
		for(int i=0; i<pdim; ++i){
			const Scalar ilb = Scalar(1)/(lambda[i]+beta);
			const Scalar a = lc2[i]*ilb*ilb;
			val += a;
			der += a*ilb;
		}
		der *= -Scalar(2);
		beta -= val/der;
	}
	for(int i=0; i<pdim; ++i){sol[i] = eta[i] * beta/(beta+lambda[i]);}
}

/**
Proximal operator argmin_sol (1/2) |sol-eta|^2 + sqrt(a^2|sol|^2+sign(a)<sol,w>_+^2)
*/
#if metric_type_macro==metric_type_iso_asym
void prox_iso_asym(
	const Scalar eta[ndim], // Projected variable
	const Scalar a, // norm multiplier
	const Scalar w[ndim], // Projected variable
	Scalar sol[__restrict__ ndim] // minimizer
	){
	const Scalar s = scal_vv(eta,w);
	const Scalar abs_a = abs(a), sgn_a = a>=0. ? Scalar(1) : -Scalar(1);

	// Case where eta is in the isotropic half space
	if(s<=0){prox_iso(eta,abs_a,sol); return;}

#if ndim_macro==1
	const Scalar b = sqrt(a*a+sgn_a*w[0]*w[0]);
	prox_iso(eta,b,sol);
#else
	STATIC_ASSERT(pdim==2,inconsistent_scheme_data);
	const Scalar norm2_w = norm2_v(w), inorm_w = Scalar(1)/sqrt(norm2_w);
	const Scalar lambda[2] = {a*a+sgn_a*norm2_w, a*a};

	// Generate an orthonormal basis of the space containing w and eta
	Scalar w_unit[ndim]; mul_kv(inorm_w,w,w_unit);
	const Scalar eta0 = s*inorm_w; // = <eta,w_unit>
	Scalar e_unit[ndim]; madd_kvv(-eta0,w_unit,eta,e_unit);
	const Scalar norm2_e = norm2_v(e_unit);
	if(norm2_e>0){mul_kV(Scalar(1)/sqrt(norm2_e),e_unit);}

	// Solve the prox in the transformed coordinates
	const Scalar eta_coef[2] = {eta0, scal_vv(eta,e_unit)};
	Scalar sol_coef[2]; 
	prox_diagonal(eta_coef,lambda,sol_coef);
	mul_kv(  sol_coef[0],w_unit,sol);
	madd_kvV(sol_coef[1],e_unit,sol);
#endif
}
#endif

/** 
Proximal operator argmin_sol (1/2)|sol-eta|^2 + sqrt(sol.m.sol),
where (lambda,v) is the eigendecomposition of m
*/
void prox_riemann(
	const Scalar eta[ndim], // Projected variable
	const Scalar lambda[ndim], // Eigenvalues
	const Scalar v[ndim][ndim], // Eigenvectors
	Scalar sol[__restrict__ ndim] // Minimizer
	){ 
	Scalar eta_coef[ndim], sol_coef[ndim];
	tdot_av(v,eta,eta_coef);
	prox_diagonal(eta_coef,lambda,sol_coef);
	dot_av(v,sol_coef,sol);
}


extern "C" {

/**
This function computes an orthogonal projection onto the set eta = grad(phi) in the 
Fourier domain. (Pointwise operation, involving array broadcasting)
*/
__global__ void fft_sum(
	Complex * __restrict__ phi_t,
	const Complex *  __restrict__ eta_t,

	const Complex * __restrict__ fft0_der,
	const Complex * __restrict__ fft0_mean
#if ndim_macro>=2
	,const Complex * __restrict__ fft1_der
	,const Complex * __restrict__ fft1_mean
#endif
#if ndim_macro==3
	,const Complex * __restrict__ fft2_der
	,const Complex * __restrict__ fft2_mean
#endif
	){

	const Int n_t = blockIdx.x*blockDim.x + threadIdx.x;
	if(n_t>=size_fft) {return;}
	Complex phi = phi_t[n_t]; // The value to be updated

	// Get the position where the work is to be done.
	Int x_t[ndim];
	Grid::Position(n_t,shape_fft,x_t);
	
#if ndim_macro==1
	Complex mul0 = fft0_der[x_t[0]];
	phi += mul0*eta_t[n_t];
	const Scalar lap = Scalar(1)+norm2(mul0); // Multiplier for identity - laplace
	phi /= lap;
#elif ndim_macro==2
	Complex mul0 = fft0_der[ x_t[0]] * fft1_mean[x_t[1]];
	Complex mul1 = fft0_mean[x_t[0]] * fft1_der[ x_t[1]];
	phi += mul0*eta_t[2*n_t] + mul1*eta_t[2*n_t+1];
	const Scalar lap = Scalar(1)+norm2(mul0)+norm2(mul1);
	phi /= lap;
#elif ndim_macro==3
	Complex mul0 = fft0_der[ x_t[0]] * fft1_mean[x_t[1]] * fft2_mean[x_t[2]];
	Complex mul1 = fft0_mean[x_t[0]] * fft1_der[ x_t[1]] * fft2_mean[x_t[2]];
	Complex mul2 = fft0_mean[x_t[0]] * fft1_mean[x_t[1]] * fft2_der[ x_t[2]];
	phi += mul0*eta_t[3*n_t] + mul1*eta_t[3*n_t+1] + mul2*eta_t[3*n_t+2];
	const Scalar lap = Scalar(1)+norm2(mul0)+norm2(mul1)+norm2(mul2);
	phi /= lap;
#endif

	phi_t[n_t] = phi;
}

/**
Computes a finite differences gradient on a staggered grid.
*/
__global__ void stag_gradient(
	const Scalar * __restrict__ phi_t,
	      Scalar * __restrict__ eta_t
	){
	const int n_i = threadIdx.x;
	const int n_o = blockIdx.x;
	__shared__ int x_o[ndim];
	if(n_i==0){Grid::Position(n_o,shape_o,x_o);}
	__syncthreads();

	// Load values associated to an extended neighborhood in a shared array
	__shared__ Scalar phi_e[size_e];
	for(int i=0; i<1+(size_e-1)/size_i; ++i){
		const int n_e = n_i + i*size_i;
		if(n_e>=size_e) break;
		int x_e[ndim];
		Grid::Position(n_e,shape_e,x_e);
		int x_t[ndim];
		// We actually only need to wrap around by 1 pixel, but these are edge cases
		for(int k=0; k<ndim; ++k){x_t[k] = (x_o[k]*shape_i[k]+x_e[k])%shape_tot[k];}
		const int n_t = Grid::Index(x_t,shape_tot);
		phi_e[n_e] = phi_t[n_t];
	}
	__syncthreads();
	// Find the index in the global array
	int x_i[ndim];
	Grid::Position(n_i,shape_i,x_i);
	int x_t[ndim];
	for(int k=0; k<ndim; ++k){x_t[k]=x_o[k]*shape_i[k]+x_i[k];}
	if(!Grid::InRange(x_t,shape_tot)) return;
	const int n_t = Grid::Index(x_t,shape_tot);

	// Find the index in the local array
	const int n_e = Grid::Index(x_i,shape_e);

#if ndim_macro==1
	eta_t[n_t] = idx[0]*(phi_e[n_e+1]-phi_e[n_e]);
#elif ndim_macro==2
	// Note : we use indexing = 'ij', hence x is the slow variable, and y the fast one
	const int n00 = n_e, n01 = n_e+1, n10 = n_e+shape_e[1], n11 = n10+1;
	const Scalar p00 = phi_e[n00], p01 = phi_e[n01], p10=phi_e[n10], p11 = phi_e[n11];
	eta_t[ndim*n_t  ] = Scalar(0.5)*idx[0]*(
		  p11 + p10
		- p01 - p00);

	eta_t[ndim*n_t+1] = Scalar(0.5)*idx[1]*(
		  p11 - p10
		+ p01 - p00);
#elif ndim_macro==3
	const int 
	n000 = n_e, n001 = n_e+1, n010 = n_e+shape_e[2], n011 = n010+1,
	n100 = n_e+shape_e[1]*shape_e[2], n101=n100+1, n110 = n100+shape_e[2], n111 = n110+1;
	const Scalar 
	p000 = phi_e[n000], p001 = phi_e[n001], p010=phi_e[n010], p011 = phi_e[n011],
	p100 = phi_e[n100], p101 = phi_e[n101], p110=phi_e[n110], p111 = phi_e[n111];

	eta_t[ndim*n_t  ] = Scalar(0.25)*idx[0]*(
		  p111 + p110
		+ p101 + p100

		- p011 - p010
		- p001 - p000);

	eta_t[ndim*n_t+1] = Scalar(0.25)*idx[1]*(
		  p111 + p110
		- p101 - p100

		+ p011 + p010
		- p001 - p000);

	eta_t[ndim*n_t+2] = Scalar(0.25)*idx[2]*(
		  p111 - p110
		+ p101 - p100

		+ p011 - p010
		+ p001 - p000);
#endif
}

/**
Implements the proximal operator associated with the boundary conditions.
(Pointwise operation)
*/
__global__ void prox_bc(
	const Scalar * __restrict__ xpu_t,
	      Scalar * __restrict__ u_t,
	      Scalar * __restrict__ zmu_t,
	const int8   * __restrict__ bc_t
	){

	const Int n_t = blockIdx.x*blockDim.x + threadIdx.x;
	if(n_t>=size_tot) {return;}

	const int8 bc = bc_t[n_t];
	const Scalar xpu = xpu_t[n_t];
	const Scalar z = bc==2 ? xpu : Scalar(bc); // The prox value
	const Scalar u = xpu-z;
	u_t[n_t] = u;
	zmu_t[n_t] = z-u;
}	

/**
Implements the proximal operator associated to the metric.
(Pointwise complex operation)
*/
__global__ void prox_metric(
	const Scalar * __restrict__ eta_t,
		  Scalar * __restrict__ u_t,
		  Scalar * __restrict__ zmu_t,
#if   metric_type_macro == metric_type_iso
	const Scalar * __restrict__ a_t,
#elif metric_type_macro == metric_type_iso_asym
	const Scalar * __restrict__ a_t,
	const Scalar * __restrict__ w_t,
#elif metric_type_macro == metric_type_riemann
	const Scalar * __restrict__ lambda_t,
	const Scalar * __restrict__ v_t,
#elif metric_type_macro == metric_type_riemann_asym
	const Scalar * __restrict__ lambda0_t,
	const Scalar * __restrict__ v0_t,
	const Scalar * __restrict__ lambda1_t,
	const Scalar * __restrict__ v1_t,
	const Scalar * __restrict__ w_t,
#endif
	const Scalar * __restrict__ w_rander_t
	){

	const Int n_t = blockIdx.x*blockDim.x + threadIdx.x;
	if(n_t>=size_tot) {return;}

	Scalar eta[ndim], eta_ref[ndim];
	for(int i=0; i<ndim; ++i){eta[i]  = eta_t[ndim*n_t+i];}
	copy_vV(eta,eta_ref);
	mul_kV(itau,eta);

#if rander_macro
	for(int i=0; i<ndim; ++i){eta[i] -= w_rander_t[ndim*n_t+i];}
#endif

	Scalar sol[ndim]; // The prox value

#if metric_type_macro == metric_type_iso
	const Scalar a = a_t[n_t];
	prox_iso(eta,a,sol);

#elif metric_type_macro == metric_type_iso_asym

	const Scalar a = a_t[n_t];
	Scalar w[ndim];
	for(int i=0;i<ndim;++i){w[i] = w_t[ndim*n_t+i];}

	prox_iso_asym(eta,a,w,sol);

#elif metric_type_macro == metric_type_riemann
	Scalar lambda[ndim];
	Scalar v[ndim][ndim];
	for(int i=0;i<ndim;++i){lambda[i] = lambda_t[ndim*n_t+i];}
	copy_eigenvectors(v_t+n_t*qdim,v);
	prox_riemann(eta,lambda,v,sol);

#elif metric_type_macro == metric_type_riemann_asym
	Scalar lambda0[ndim];
	Scalar v0[ndim][ndim];
	for(int i=0;i<ndim;++i){lambda0[i] = lambda0_t[ndim*n_t+i];}
	copy_eigenvectors(v0_t+n_t*qdim,v0);
	prox_riemann(eta,lambda0,v0,sol);

	Scalar lambda1[ndim];
	Scalar v1[ndim][ndim];
	Scalar sol1[ndim];
	for(int i=0;i<ndim;++i){lambda1[i] = lambda1_t[ndim*n_t+i];}
	copy_eigenvectors(v1_t+n_t*qdim,v1);
	prox_riemann(eta,lambda1,v1,sol1);

	Scalar w[ndim];
	for(int i=0;i<ndim;++i){w[i] = w_t[ndim*n_t+i];}
	if(scal_vv(sol,w)>0){copy_vV(sol1,sol);}
#endif
	mul_kV(tau,sol);

	// Compute the variables used in the ADMM algorithm
	// eta_ref = xpu, sol = z
	Scalar u[ndim], zmu[ndim]; 
	sub_vv(eta_ref,sol,u); // u = xpu-z;
	sub_vv(sol,u,zmu); // z-u

	for(int i=0; i<ndim; ++i){u_t[  ndim*n_t+i] = u[i];}
	for(int i=0; i<ndim; ++i){zmu_t[ndim*n_t+i] = zmu[i];}
}


} // extern "C"