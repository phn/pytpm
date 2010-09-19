/* Declaration for functions to access V3 vectors, defined in v3Functions.c
   
   In TPM these are defined as macros, which SWIG doesn't wrap. To
   get the same functionality from within python, we define the
   following functions and wrap them using SWIG.

   Author: Prasanth Nair
   Contact: prasanthhn@gmail.com
*/
#ifndef V3_INCLUDE
#include "tpm/v3.h"
#endif

/*#define v3DecX(v3,x)		(v3.v[0] -= (x))*/
void v3DecXf(V3 *const v3, double x); 
/*#define v3DecY(v3,x)		(v3.v[1] -= (x))*/
void v3DecYf(V3 *const v3, double x);
/*#define v3DecZ(v3,x)		(v3.v[2] -= (x))*/
void v3DecZf(V3 *const v3, double x);
/*#define v3DecR(v3,x)		(v3.v[0] -= (x))*/
void v3DecRf(V3 *const v3, double x);
/*#define v3DecAlpha(v3,x)	(v3.v[1] -= (x))*/
void v3DecAlphaf(V3 *const v3, double x);
/*#define v3DecDelta(v3,x)	(v3.v[2] -= (x))*/
void v3DecDeltaf(V3 *const v3, double x);
/*#define v3DivX(v3,x)		(v3.v[0] /= (x))*/
void v3DivXf(V3 *const v3, double x);
/*#define v3DivY(v3,x)		(v3.v[1] /= (x))*/
void v3DivYf(V3 *const v3, double x);
/*#define v3DivZ(v3,x)		(v3.v[2] /= (x))*/
void v3DivZf(V3 *const v3, double x);
/*#define v3DivR(v3,x)		(v3.v[0] /= (x))*/
void v3DivRf(V3 *const v3, double x);
/*#define v3DivAlpha(v3,x)	(v3.v[1] /= (x))*/
void v3DivAlphaf(V3 *const v3, double x);
/*#define v3DivDelta(v3,x)	(v3.v[2] /= (x))*/
void v3DivDeltaf(V3 *const v3, double x);

/*#define v3GetType(v3)		(v3.type)*/
int v3GetTypef(const V3 v3);
/*#define v3GetX(v3)		(v3.v[0])*/
double v3GetXf(const V3 v3);
/*#define v3GetY(v3)		(v3.v[1])*/
double v3GetYf(const V3 v3);
/*#define v3GetZ(v3)		(v3.v[2])*/
double v3GetZf(const V3 v3);
/*#define v3GetR(v3)		(v3.v[0])*/
double v3GetRf(const V3 v3);
/*#define v3GetAlpha(v3)		(v3.v[1])*/
double v3GetAlphaf(const V3 v3);
/*#define v3GetDelta(v3)		(v3.v[2])*/
double v3GetDeltaf(const V3 v3);

/*#define v3IncX(v3,x)		(v3.v[0] += (x))*/
void v3IncXf(V3 *const v3, double x);
/*#define v3IncY(v3,x)		(v3.v[1] += (x))*/
void v3IncYf(V3 *const v3, double x);
/*#define v3IncZ(v3,x)		(v3.v[2] += (x))*/
void v3IncZf(V3 *const v3, double x);
/*#define v3IncR(v3,x)		(v3.v[0] += (x))*/
void v3IncRf(V3 *const v3, double x);
/*#define v3IncAlpha(v3,x)	(v3.v[1] += (x))*/
void v3IncAlphaf(V3 *const v3, double x);
/*#define v3IncDelta(v3,x)	(v3.v[2] += (x))*/
void v3IncDeltaf(V3 *const v3, double x);

/*#define v3MulX(v3,x)		(v3.v[0] *= (x))*/
void v3MulXf(V3 *const v3, double x);
/*#define v3MulY(v3,x)		(v3.v[1] *= (x))*/
void v3MulYf(V3 *const v3, double x);
/*#define v3MulZ(v3,x)		(v3.v[2] *= (x))*/
void v3MulZf(V3 *const v3, double x);
/*#define v3MulR(v3,x)		(v3.v[0] *= (x))*/
void v3MulRf(V3 *const v3, double x);
/*#define v3MulAlpha(v3,x)	(v3.v[1] *= (x))*/
void v3MulAlphaf(V3 *const v3, double x);
/*#define v3MulDelta(v3,x)	(v3.v[2] *= (x))*/
void v3MulDeltaf(V3 *const v3, double x);

/*#define v3SetType(v3,x)		(v3.type = (x))*/
void v3SetTypef(V3 *const v3, int t);
/*#define v3SetX(v3,x)		(v3.v[0] = (x))*/
void v3SetXf(V3 *v3, double x); 
/*#define v3SetY(v3,x)		(v3.v[1] = (x))*/
void v3SetYf(V3 *v3, double y); 
/*#define v3SetZ(v3,x)		(v3.v[2] = (x))*/
void v3SetZf(V3 *v3, double z); 
/*#define v3SetR(v3,x)		(v3.v[0] = (x))*/
void v3SetRf(V3 *v3, double r); 
/*#define v3SetAlpha(v3,x)	(v3.v[1] = (x))*/
void v3SetAlphaf(V3 *v3, double alpha); 
/*#define v3SetDelta(v3,x)	(v3.v[2] = (x))*/
void v3SetDeltaf(V3 *v3, double delta); 

/* some astro convenience macros */

/*#define v3DecRA(f,x)		(v3DecAlpha(f,x))*/
void v3DecRAf(V3 *const v3, double x);
/*#define v3DecDec(f,x)		(v3DecDelta(f,x))*/
void v3DecDecf(V3 *const v3, double x);

/*#define v3DivRA(f,x)		(v3DivAlpha(f,x))*/
void v3DivRAf(V3 *const v3, double x);
/*#define v3DivDec(f,x)		(v3DivDelta(f,x))*/
void v3DivDecf(V3 *const v3, double x);

/*#define v3GetRA(f)		(v3GetAlpha(f))*/
double v3GetRAf(const V3 v3);
/*#define v3GetDec(f)		(v3GetDelta(f))*/
double v3GetDecf(const V3 v3);

/*#define v3IncRA(f,x)		(v3IncAlpha(f,x))*/
void v3IncRAf(V3 *const v3, double x);
/*#define v3IncDec(f,x)		(v3IncDelta(f,x))*/
void v3IncDecf(V3 *const v3, double x);

/*#define v3MulRA(f,x)		(v3MulAlpha(f,x))*/
void v3MulRAf(V3 *const v3, double x);
/*#define v3MulDec(f,x)		(v3MulDelta(f,x))*/
void v3MulDecf(V3 *const v3, double x);

/*#define v3SetRA(f,x)		(v3SetAlpha(f,x))*/
void v3SetRAf(V3 *const v3, double ra);
/*#define v3SetDec(f,x)		(v3SetDelta(f,x))*/
void v3SetDecf(V3 *const v3, double dec);
