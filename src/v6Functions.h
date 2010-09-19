/* Declaration for functions to access V6 vectors, defined in v6Functions.c
   
   In TPM these are defined as macros, which SWIG doesn't wrap. To
   get the same functionality from within python, we define the
   following functions and wrap them using SWIG.

   Author: Prasanth Nair
   Contact: prasanthhn@gmail.com
*/
#ifndef V3_INCLUDE
#include "tpm/v3.h"
#endif
#ifndef V6_INCLUDE
#include "tpm/v6.h"
#endif

/*#define v6GetPos(v6)	(v6.v[POS])*/
V3 v6GetPosf(const V6 *const v6); 
/*#define v6GetVel(v6)	(v6.v[VEL])*/
V3 v6GetVelf(const V6 *const v6);
/*#define v6SetPos(v6,v3)	(v6.v[POS] = (v3))*/
void v6SetPosf(V6 *const v6, const V3 v3);
/*#define v6SetVel(v6,v3)	(v6.v[VEL] = (v3))*/
void v6SetVelf(V6 *const v6, const V3 v3);

/*#define v6DecX(v6,x)		(v6.v[POS].v[0] -= (x))*/
void v6DecXf(V6 *const v6, double x);
/*#define v6DecY(v6,x)		(v6.v[POS].v[1] -= (x))*/
void v6DecYf(V6 *const v6, double x);
/*#define v6DecZ(v6,x)		(v6.v[POS].v[2] -= (x))*/
void v6DecZf(V6 *const v6, double x);
/*#define v6DecXDot(v6,x)		(v6.v[VEL].v[0] -= (x))*/
void v6DecXDotf(V6 *const v6, double x);
/*#define v6DecYDot(v6,x)		(v6.v[VEL].v[1] -= (x))*/
void v6DecYDotf(V6 *const v6, double x);
/*#define v6DecZDot(v6,x)		(v6.v[VEL].v[2] -= (x))*/
void v6DecZDotf(V6 *const v6, double x);
/*#define v6DecR(v6,x)		(v6.v[POS].v[0] -= (x))*/
void v6DecRf(V6 *const v6, double x);
/*#define v6DecAlpha(v6,x)	(v6.v[POS].v[1] -= (x))*/
void v6DecAlphaf(V6 *const v6, double x);
/*#define v6DecDelta(v6,x)	(v6.v[POS].v[2] -= (x))*/
void v6DecDeltaf(V6 *const v6, double x);
/*#define v6DecRDot(v6,x)		(v6.v[VEL].v[0] -= (x))*/
void v6DecRDotf(V6 *const v6, double x);
/*#define v6DecAlphaDot(v6,x)	(v6.v[VEL].v[1] -= (x))*/
void v6DecAlphaDotf(V6 *const v6, double x);
/*#define v6DecDeltaDot(v6,x)	(v6.v[VEL].v[2] -= (x))*/
void v6DecDeltaDotf(V6 *const v6, double x);

/*#define v6DivX(v6,x)		(v6.v[POS].v[0] /= (x))*/
void v6DivXf(V6 *const v6, double x);
/*#define v6DivY(v6,x)		(v6.v[POS].v[1] /= (x))*/
void v6DivYf(V6 *const v6, double x);
/*#define v6DivZ(v6,x)		(v6.v[POS].v[2] /= (x))*/
void v6DivZf(V6 *const v6, double x);
/*#define v6DivXDot(v6,x)		(v6.v[VEL].v[0] /= (x))*/
void v6DivXDotf(V6 *const v6, double x);
/*#define v6DivYDot(v6,x)		(v6.v[VEL].v[1] /= (x))*/
void v6DivYDotf(V6 *const v6, double x);
/*#define v6DivZDot(v6,x)		(v6.v[VEL].v[2] /= (x))*/
void v6DivZDotf(V6 *const v6, double x);
/*#define v6DivR(v6,x)		(v6.v[POS].v[0] /= (x))*/
void v6DivRf(V6 *const v6, double x);
/*#define v6DivAlpha(v6,x)	(v6.v[POS].v[1] /= (x))*/
void v6DivAlphaf(V6 *const v6, double x);
/*#define v6DivDelta(v6,x)	(v6.v[POS].v[2] /= (x))*/
void v6DivDeltaf(V6 *const v6, double x);
/*#define v6DivRDot(v6,x)		(v6.v[VEL].v[0] /= (x))*/
void v6DivRDotf(V6 *const v6, double x);
/*#define v6DivAlphaDot(v6,x)	(v6.v[VEL].v[1] /= (x))*/
void v6DivAlphaDotf(V6 *const v6, double x);
/*#define v6DivDeltaDot(v6,x)	(v6.v[VEL].v[2] /= (x))*/
void v6DivDeltaDotf(V6 *const v6, double x);

/*#define v6GetType(v6)		(v6.v[POS].type)*/
int v6GetTypef(const V6 v6);
/*#define v6GetX(v6)		(v6.v[POS].v[0])*/
double v6GetXf(const V6 v6);
/*#define v6GetY(v6)		(v6.v[POS].v[1])*/
double v6GetYf(const V6 v6);
/*#define v6GetZ(v6)		(v6.v[POS].v[2])*/
double v6GetZf(const V6 v6);
/*#define v6GetXDot(v6)		(v6.v[VEL].v[0])*/
double v6GetXDotf(const V6 v6);
/*#define v6GetYDot(v6)		(v6.v[VEL].v[1])*/
double v6GetYDotf(const V6 v6);
/*#define v6GetZDot(v6)		(v6.v[VEL].v[2])*/
double v6GetZDotf(const V6 v6);
/*#define v6GetR(v6)		(v6.v[POS].v[0])*/
double v6GetRf(const V6 v6);
/*#define v6GetAlpha(v6)		(v6.v[POS].v[1])*/
double v6GetAlphaf(const V6 v6);
/*#define v6GetDelta(v6)		(v6.v[POS].v[2])*/
double v6GetDeltaf(const V6 v6);
/*#define v6GetRDot(v6)		(v6.v[VEL].v[0])*/
double v6GetRDotf(const V6 v6);
/*#define v6GetAlphaDot(v6)	(v6.v[VEL].v[1])*/
double v6GetAlphaDotf(const V6 v6);
/*#define v6GetDeltaDot(v6)	(v6.v[VEL].v[2])*/
double v6GetDeltaDotf(const V6 v6);

/*#define v6IncX(v6,x)		(v6.v[POS].v[0] += (x))*/
void v6IncXf(V6 *const v6, double x);
/*#define v6IncY(v6,x)		(v6.v[POS].v[1] += (x))*/
void v6IncYf(V6 *const v6, double x);
/*#define v6IncZ(v6,x)		(v6.v[POS].v[2] += (x))*/
void v6IncZf(V6 *const v6, double x);
/*#define v6IncXDot(v6,x)		(v6.v[VEL].v[0] += (x))*/
void v6IncXDotf(V6 *const v6, double x);
/*#define v6IncYDot(v6,x)		(v6.v[VEL].v[1] += (x))*/
void v6IncYDotf(V6 *const v6, double x);
/*#define v6IncZDot(v6,x)		(v6.v[VEL].v[2] += (x))*/
void v6IncZDotf(V6 *const v6, double x);
/*#define v6IncR(v6,x)		(v6.v[POS].v[0] += (x))*/
void v6IncRf(V6 *const v6, double x);
/*#define v6IncAlpha(v6,x)	(v6.v[POS].v[1] += (x))*/
void v6IncAlphaf(V6 *const v6, double x);
/*#define v6IncDelta(v6,x)	(v6.v[POS].v[2] += (x))*/
void v6IncDeltaf(V6 *const v6, double x);
/*#define v6IncRDot(v6,x)		(v6.v[VEL].v[0] += (x))*/
void v6IncRDotf(V6 *const v6, double x);
/*#define v6IncAlphaDot(v6,x)	(v6.v[VEL].v[1] += (x))*/
void v6IncAlphaDotf(V6 *const v6, double x);
/*#define v6IncDeltaDot(v6,x)	(v6.v[VEL].v[2] += (x))*/
void v6IncDeltaDotf(V6 *const v6, double x);

/*#define v6MulX(v6,x)		(v6.v[POS].v[0] *= (x))*/
void v6MulXf(V6 *const v6, double x);
/*#define v6MulY(v6,x)		(v6.v[POS].v[1] *= (x))*/
void v6MulYf(V6 *const v6, double x);
/*#define v6MulZ(v6,x)		(v6.v[POS].v[2] *= (x))*/
void v6MulZf(V6 *const v6, double x);
/*#define v6MulXDot(v6,x)		(v6.v[VEL].v[0] *= (x))*/
void v6MulXDotf(V6 *const v6, double x);
/*#define v6MulYDot(v6,x)		(v6.v[VEL].v[1] *= (x))*/
void v6MulYDotf(V6 *const v6, double x);
/*#define v6MulZDot(v6,x)		(v6.v[VEL].v[2] *= (x))*/
void v6MulZDotf(V6 *const v6, double x);
/*#define v6MulR(v6,x)		(v6.v[POS].v[0] *= (x))*/
void v6MulRf(V6 *const v6, double x);
/*#define v6MulAlpha(v6,x)	(v6.v[POS].v[1] *= (x))*/
void v6MulAlphaf(V6 *const v6, double x);
/*#define v6MulDelta(v6,x)	(v6.v[POS].v[2] *= (x))*/
void v6MulDeltaf(V6 *const v6, double x);
/*#define v6MulRDot(v6,x)		(v6.v[VEL].v[0] *= (x))*/
void v6MulRDotf(V6 *const v6, double x);
/*#define v6MulAlphaDot(v6,x)	(v6.v[VEL].v[1] *= (x))*/
void v6MulAlphaDotf(V6 *const v6, double x);
/*#define v6MulDeltaDot(v6,x)	(v6.v[VEL].v[2] *= (x))*/
void v6MulDeltaDotf(V6 *const v6, double x);

/*#define v6SetType(v6,t)		(v6.v[POS].type = v6.v[VEL].type = (t))*/
void v6SetTypef(V6 *const v6, int t);
/*#define v6SetX(v6,x)		(v6.v[POS].v[0] = (x))*/
void v6SetXf(V6 *const v6, double x);
/*#define v6SetY(v6,x)		(v6.v[POS].v[1] = (x))*/
void v6SetYf(V6 *const v6, double x);
/*#define v6SetZ(v6,x)		(v6.v[POS].v[2] = (x))*/
void v6SetZf(V6 *const v6, double x);
/*#define v6SetXDot(v6,x)		(v6.v[VEL].v[0] = (x))*/
void v6SetXDotf(V6 *const v6, double x);
/*#define v6SetYDot(v6,x)		(v6.v[VEL].v[1] = (x))*/
void v6SetYDotf(V6 *const v6, double x);
/*#define v6SetZDot(v6,x)		(v6.v[VEL].v[2] = (x))*/
void v6SetZDotf(V6 *const v6, double x);
/*#define v6SetR(v6,x)		(v6.v[POS].v[0] = (x))*/
void v6SetRf(V6 *const v6, double x);
/*#define v6SetAlpha(v6,x)	(v6.v[POS].v[1] = (x))*/
void v6SetAlphaf(V6 *const v6, double x);
/*#define v6SetDelta(v6,x)	(v6.v[POS].v[2] = (x))*/
void v6SetDeltaf(V6 *const v6, double x);
/*#define v6SetRDot(v6,x)		(v6.v[VEL].v[0] = (x))*/
void v6SetRDotf(V6 *const v6, double x);
/*#define v6SetAlphaDot(v6,x)	(v6.v[VEL].v[1] = (x))*/
void v6SetAlphaDotf(V6 *const v6, double x);
/*#define v6SetDeltaDot(v6,x)	(v6.v[VEL].v[2] = (x))*/
void v6SetDeltaDotf(V6 *const v6, double x);

/* some astro convenience macros */

/*#define v6DecRA(f,x)		(v6DecAlpha(f,x))*/
void v6DecRAf(V6 *const v6, double x);
/*#define v6DecPMRA(f,x)		(v6DecAlphaDot(f,x))*/
void v6DecPMRAf(V6 *const v6, double x);
/*#define v6DecDec(f,x)		(v6DecDelta(f,x))*/
void v6DecDecf(V6 *const v6, double x);
/*#define v6DecPMDec(f,x)		(v6DecDeltaDot(f,x))*/
void v6DecPMDecf(V6 *const v6, double x);

/*#define v6DivRA(f,x)		(v6DivAlpha(f,x))*/
void v6DivRAf(V6 *const v6, double x);
/*#define v6DivPMRA(f,x)		(v6DivAlphaDot(f,x))*/
void v6DivPMRAf(V6 *const v6, double x);
/*#define v6DivDec(f,x)		(v6DivDelta(f,x))*/
void v6DivDecf(V6 *const v6, double x);
/*#define v6DivPMDec(f,x)		(v6DivDeltaDot(f,x))*/
void v6DivPMDecf(V6 *const v6, double x);

/*#define v6GetRA(f)		(v6GetAlpha(f))*/
double v6GetRAf(const V6 v6);
/*#define v6GetPMRA(f)		(v6GetAlphaDot(f))*/
double v6GetPMRAf(const V6 v6);
/*#define v6GetDec(f)		(v6GetDelta(f))*/
double v6GetDecf(const V6 v6);
/*#define v6GetPMDec(f)		(v6GetDeltaDot(f))*/
double v6GetPMDecf(const V6 v6);

/*#define v6IncRA(f,x)		(v6IncAlpha(f,x))*/
void v6IncRAf(V6 *const v6, double x);
/*#define v6IncPMRA(f,x)		(v6IncAlphaDot(f,x))*/
void v6IncPMRAf(V6 *const v6, double x);
/*#define v6IncDec(f,x)		(v6IncDelta(f,x))*/
void v6IncDecf(V6 *const v6, double x);
/*#define v6IncPMDec(f,x)		(v6IncDeltaDot(f,x))*/
void v6IncPMDecf(V6 *const v6, double x);

/*#define v6MulRA(f,x)		(v6MulAlpha(f,x))*/
void v6MulRAf(V6 *const v6, double x);
/*#define v6MulPMRA(f,x)		(v6MulAlphaDot(f,x))*/
void v6MulPMRAf(V6 *const v6, double x);
/*#define v6MulDec(f,x)		(v6MulDelta(f,x))*/
void v6MulDecf(V6 *const v6, double x);
/*#define v6MulPMDec(f,x)		(v6MulDeltaDot(f,x))*/
void v6MulPMDecf(V6 *const v6, double x);

/*#define v6SetRA(f,x)		(v6SetAlpha(f,x))*/
void v6SetRAf(V6 *const v6, double x);
/*#define v6SetPMRA(f,x)		(v6SetAlphaDot(f,x))*/
void v6SetPMRAf(V6 *const v6, double x);
/*#define v6SetDec(f,x)		(v6SetDelta(f,x))*/
void v6SetDecf(V6 *const v6, double x);
/*#define v6SetPMDec(f,x)		(v6SetDeltaDot(f,x))*/
void v6SetPMDecf(V6 *const v6, double x);
