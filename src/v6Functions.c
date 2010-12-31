#include "v6Functions.h"
/* Functions to access V6 vectors.
   
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
/* POS index of position vector and VEL index of velocity vector     */

/*********************************************************************/
/* Get and set position and velocity components of V6 vector.        */
/*********************************************************************/
V3 v6GetPosf(const V6 *const v6){
  return v6->v[POS];
}

V3 v6GetVelf(const V6 *const v6){
  return v6->v[VEL];
}

void v6SetPosf(V6 *const v6, const V3 v3){
  v6->v[POS] = v3;
}

void v6SetVelf(V6 *const v6, const V3 v3){
  v6->v[VEL] = v3;
}

/*********************************************************************/
/* Decrement positions and velocities of a V6 vector.                */
/*********************************************************************/
void v6DecXf(V6 *const v6, double x){
  v6->v[POS].v[0] -= x;
}

void v6DecYf(V6 *const v6, double x){
  v6->v[POS].v[1] -= x;
}

void v6DecZf(V6 *const v6, double x){
  v6->v[POS].v[2] -= x;
}

void v6DecXDotf(V6 *const v6, double x){
  v6->v[VEL].v[0] -= x;
}

void v6DecYDotf(V6 *const v6, double x){
  v6->v[VEL].v[1] -= x;
}

void v6DecZDotf(V6 *const v6, double x){
  v6->v[VEL].v[2] -= x;
}

void v6DecRf(V6 *const v6, double x){
  v6->v[POS].v[0] -= x;
}

void v6DecAlphaf(V6 *const v6, double x){
  v6->v[POS].v[1] -= x;
}

void v6DecDeltaf(V6 *const v6, double x){
  v6->v[POS].v[2] -= x;
}

void v6DecRDotf(V6 *const v6, double x){
  v6->v[VEL].v[0] -= x;
}

void v6DecAlphaDotf(V6 *const v6, double x){
  v6->v[VEL].v[1] -= x;
}

void v6DecDeltaDotf(V6 *const v6, double x){
  v6->v[VEL].v[2] -= x;
}

/*********************************************************************/
/* Divide positions and velocities of a V6 vector.                   */
/*********************************************************************/
void v6DivXf(V6 *const v6, double x){
  v6->v[POS].v[0] /= x;
}

void v6DivYf(V6 *const v6, double x){
  v6->v[POS].v[1] /= x;
}

void v6DivZf(V6 *const v6, double x){
  v6->v[POS].v[2] /= x;
}

void v6DivXDotf(V6 *const v6, double x){
  v6->v[VEL].v[0] /= x;
}

void v6DivYDotf(V6 *const v6, double x){
  v6->v[VEL].v[1] /= x;
}

void v6DivZDotf(V6 *const v6, double x){
  v6->v[VEL].v[2] /= x;
}

void v6DivRf(V6 *const v6, double x){
  v6->v[POS].v[0] /= x;
}

void v6DivAlphaf(V6 *const v6, double x){
  v6->v[POS].v[1] /= x;
}

void v6DivDeltaf(V6 *const v6, double x){
  v6->v[POS].v[2] /= x;
}

void v6DivRDotf(V6 *const v6, double x){
  v6->v[VEL].v[0] /= x;
}

void v6DivAlphaDotf(V6 *const v6, double x){
  v6->v[VEL].v[1] /= x;
}

void v6DivDeltaDotf(V6 *const v6, double x){
  v6->v[VEL].v[2] /= x;
}

/*********************************************************************/
/* Get positions and velocities of a V6 vector.                      */
/*********************************************************************/
int v6GetTypef(const V6 v6){
  /* V6 type is type of v[POS] not v[VEL]. But they should be the same*/
  return v6.v[POS].type;
}

double v6GetXf(const V6 v6){
  return v6.v[POS].v[0];
}

double v6GetYf(const V6 v6){
  return v6.v[POS].v[1];
}

double v6GetZf(const V6 v6){
  return v6.v[POS].v[2];
}

double v6GetXDotf(const V6 v6){
  return v6.v[VEL].v[0];
}

double v6GetYDotf(const V6 v6){
  return v6.v[VEL].v[1];
}

double v6GetZDotf(const V6 v6){
  return v6.v[VEL].v[2];
}

double v6GetRf(const V6 v6){
  return v6.v[POS].v[0];
}

double v6GetAlphaf(const V6 v6){
  return v6.v[POS].v[1];
}

double v6GetDeltaf(const V6 v6){
  return v6.v[POS].v[2];
}

double v6GetRDotf(const V6 v6){
  return v6.v[VEL].v[0];
}

double v6GetAlphaDotf(const V6 v6){
  return v6.v[VEL].v[1];
}

double v6GetDeltaDotf(const V6 v6){
  return v6.v[VEL].v[2];
}

/*********************************************************************/
/* Increment positions and velocities of a V6 vector.                */
/*********************************************************************/
void v6IncXf(V6 *const v6, double x){
  v6->v[POS].v[0] += x;
}

void v6IncYf(V6 *const v6, double x){
  v6->v[POS].v[1] += x;
}

void v6IncZf(V6 *const v6, double x){
  v6->v[POS].v[2] += x;
}

void v6IncXDotf(V6 *const v6, double x){
  v6->v[VEL].v[0] += x;
}

void v6IncYDotf(V6 *const v6, double x){
  v6->v[VEL].v[1] += x;
}

void v6IncZDotf(V6 *const v6, double x){
  v6->v[VEL].v[2] += x;
}

void v6IncRf(V6 *const v6, double x){
  v6->v[POS].v[0] += x;
}

void v6IncAlphaf(V6 *const v6, double x){
  v6->v[POS].v[1] += x;
}

void v6IncDeltaf(V6 *const v6, double x){
  v6->v[POS].v[2] += x;
}

void v6IncRDotf(V6 *const v6, double x){
  v6->v[VEL].v[0] += x;
}

void v6IncAlphaDotf(V6 *const v6, double x){
  v6->v[VEL].v[1] += x;
}

void v6IncDeltaDotf(V6 *const v6, double x){
  v6->v[VEL].v[2] += x;
}

/*********************************************************************/
/* Multiply positions and velocities of a V6 vector.                 */
/*********************************************************************/
void v6MulXf(V6 *const v6, double x){
  v6->v[POS].v[0] *= x;
}

void v6MulYf(V6 *const v6, double x){
  v6->v[POS].v[1] *= x;
}

void v6MulZf(V6 *const v6, double x){
  v6->v[POS].v[2] *= x;
}

void v6MulXDotf(V6 *const v6, double x){
  v6->v[VEL].v[0] *= x;
}

void v6MulYDotf(V6 *const v6, double x){
  v6->v[VEL].v[1] *= x;
}

void v6MulZDotf(V6 *const v6, double x){
  v6->v[VEL].v[2] *= x;
}

void v6MulRf(V6 *const v6, double x){
  v6->v[POS].v[0] *= x;
}

void v6MulAlphaf(V6 *const v6, double x){
  v6->v[POS].v[1] *= x;
}

void v6MulDeltaf(V6 *const v6, double x){
  v6->v[POS].v[2] *= x;
}

void v6MulRDotf(V6 *const v6, double x){
  v6->v[VEL].v[0] *= x;
}

void v6MulAlphaDotf(V6 *const v6, double x){
  v6->v[VEL].v[1] *= x;
}

void v6MulDeltaDotf(V6 *const v6, double x){
  v6->v[VEL].v[2] *= x;
}

/*********************************************************************/
/* Set positions and velocities of a V6 vector.                      */
/*********************************************************************/
void v6SetTypef(V6 *const v6, int t){
  /* Type of the V6 vector is that of POS; but it should have the
     same value as that of VEL vector. */
  v6->v[POS].type = t;
  v6->v[VEL].type = t;
}

void v6SetXf(V6 *const v6, double x){
  v6->v[POS].v[0] = x;
}

void v6SetYf(V6 *const v6, double x){
  v6->v[POS].v[1] = x;
}

void v6SetZf(V6 *const v6, double x){
  v6->v[POS].v[2] = x;
}

void v6SetXDotf(V6 *const v6, double x){
  v6->v[VEL].v[0] = x;
}

void v6SetYDotf(V6 *const v6, double x){
  v6->v[VEL].v[1] = x;
}

void v6SetZDotf(V6 *const v6, double x){
  v6->v[VEL].v[2] = x;
}

void v6SetRf(V6 *const v6, double x){
  v6->v[POS].v[0] = x;
}

void v6SetAlphaf(V6 *const v6, double x){
  v6->v[POS].v[1] = x;
}

void v6SetDeltaf(V6 *const v6, double x){
  v6->v[POS].v[2] = x;
}

void v6SetRDotf(V6 *const v6, double x){
  v6->v[VEL].v[0] = x;
}

void v6SetAlphaDotf(V6 *const v6, double x){
  v6->v[VEL].v[1] = x;
}

void v6SetDeltaDotf(V6 *const v6, double x){
  v6->v[VEL].v[2] = x;
}

/**********************************************************************/
/* Some astro convenience macros                                      */
/**********************************************************************/
/*#define v6DecRA(f,x)		(v6DecAlpha(f,x))*/
void v6DecRAf(V6 *const v6, double x){
  v6DecAlphaf(v6, x);
}

void v6DecPMRAf(V6 *const v6, double x){
  v6DecAlphaDotf(v6, x);
}

void v6DecDecf(V6 *const v6, double x){
  v6DecDeltaf(v6, x);
}

void v6DecPMDecf(V6 *const v6, double x){
  v6DecDeltaDotf(v6, x);
}

void v6DivRAf(V6 *const v6, double x){
  v6DivAlphaf(v6, x);
}

void v6DivPMRAf(V6 *const v6, double x){
  v6DivAlphaDotf(v6, x);
}

void v6DivDecf(V6 *const v6, double x){
  v6DivDeltaf(v6, x);
}

void v6DivPMDecf(V6 *const v6, double x){
  v6DivDeltaDotf(v6, x);
}

double v6GetRAf(const V6 v6){
  return v6GetAlphaf(v6);
}

double v6GetPMRAf(const V6 v6){
  return v6GetAlphaDotf(v6);
}

double v6GetDecf(V6 v6){
  return v6GetDeltaf(v6);
}

double v6GetPMDecf(V6 v6){
  return v6GetDeltaDotf(v6);
}

void v6IncRAf(V6 *const v6, double x){
  v6IncAlphaf(v6, x);
}

void v6IncPMRAf(V6 *const v6, double x){
  v6IncAlphaDotf(v6, x);
}

void v6IncDecf(V6 *const v6, double x){
  v6IncDeltaf(v6, x);
}

void v6IncPMDecf(V6 *const v6, double x){
  v6IncDeltaDotf(v6, x);
}

void v6MulRAf(V6 *const v6, double x){
  v6MulAlphaf(v6, x);
}

void v6MulPMRAf(V6 *const v6, double x){
  v6MulAlphaDotf(v6, x);
}

void v6MulDecf(V6 *const v6, double x){
  v6MulDeltaf(v6, x);
}

void v6MulPMDecf(V6 *const v6, double x){
  v6MulDeltaDotf(v6, x);
}

void v6SetRAf(V6 *const v6, double x){
  v6SetAlphaf(v6, x);
}

void v6SetPMRAf(V6 *const v6, double x){
  v6SetAlphaDotf(v6, x);
}

void v6SetDecf(V6 *const v6, double x){
  v6SetDeltaf(v6, x);
}

void v6SetPMDecf(V6 *const v6, double x){
  v6SetDeltaDotf(v6, x);
}

