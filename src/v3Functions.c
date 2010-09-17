#include "v3Functions.h"
/* Functions to access V3 vectors.
   
   In TPM these are defined as macros, which SWIG doesn't wrap. To
   get the same functionality from within python, we define the
   following functions and wrap them using SWIG.

   Author: Prasanth Nair
   Contact: prasanthhn@gmail.com
*/

/**********************************************************************/
/* Decrement components of a V3 vector by the given amount.           */
/**********************************************************************/
void v3DecXf(V3 *const v3, double x){
  v3->v[0] -= x;
}

void v3DecYf(V3 *const v3, double x){
  v3->v[1] -= x;
}

void v3DecZf(V3 *const v3, double x){
  v3->v[2] -= x;
}

void v3DecRf(V3 *const v3, double x){
  v3->v[0] -= x;
}

void v3DecAlphaf(V3 *const v3, double x){
  v3->v[1] -= x;
}

void v3DecDeltaf(V3 *const v3, double x){
  v3->v[2] -= x;
}
/**********************************************************************/
/* Divide components of a V3 vector by the given factor.              */
/**********************************************************************/
void v3DivXf(V3 *const v3, double x){
  v3->v[0] /= x;
}

void v3DivYf(V3 *const v3, double x){
  v3->v[1] /= x;
}

void v3DivZf(V3 *const v3, double x){
  v3->v[2] /= x;
}

void v3DivRf(V3 *const v3, double x){
  v3->v[0] /= x;
}

void v3DivAlphaf(V3 *const v3, double x){
  v3->v[1] /= x;
}

void v3DivDeltaf(V3 *const v3, double x){
  v3->v[2] /= x;
}

/**********************************************************************/
/* Retrive values of components of a V3 vector.                       */
/**********************************************************************/
int v3GetTypef(const V3 v3){
  return v3.type;
}

double v3GetXf(const V3 v3){
  return v3.v[0];
}

double v3GetYf(const V3 v3){
  return v3.v[1];
}

double v3GetZf(const V3 v3){
  return v3.v[2];
}

double v3GetRf(const V3 v3){
  return v3.v[0];
}

double v3GetAlphaf(const V3 v3){
  return v3.v[1];
}

double v3GetDeltaf(const V3 v3){
  return v3.v[2];
}

/**********************************************************************/
/* Increment components of a V3 vector by the given value.            */
/**********************************************************************/
void v3IncXf(V3 *const v3, double x){
  v3->v[0] += x;
}

void v3IncYf(V3 *const v3, double x){
  v3->v[1] += x;
}

void v3IncZf(V3 *const v3, double x){
  v3->v[2] += x;
}

void v3IncRf(V3 *const v3, double x){
  v3->v[0] += x;
}

void v3IncAlphaf(V3 *const v3, double x){
  v3->v[1] += x;
}

void v3IncDeltaf(V3 *const v3, double x){
  v3->v[2] += x;
}

/**********************************************************************/
/* Multiply the components of a V3 vector by the given factor.        */
/**********************************************************************/
void v3MulXf(V3 *const v3, double x){
  v3->v[0] *= x;
}

void v3MulYf(V3 *const v3, double x){
  v3->v[1] *= x;
}

void v3MulZf(V3 *const v3, double x){
  v3->v[2] *= x;
}

void v3MulRf(V3 *const v3, double x){
  v3->v[0] *= x;
}

void v3MulAlphaf(V3 *const v3, double x){
  v3->v[1] *= x;
}

void v3MulDeltaf(V3 *const v3, double x){
  v3->v[2] *= x;
}

/**********************************************************************/
/* Set the components of a V3 vector.                                 */
/**********************************************************************/
void v3SetTypef(V3 *const v3, int t){
  v3->type = t;
}

void v3SetXf(V3 *v3, double x){
  v3->v[0] = x;
}

void v3SetYf(V3 *v3, double y){
  v3->v[1] = y;
}

void v3SetZf(V3 *v3, double z){
  v3->v[2] = z;
}

void v3SetRf(V3 *v3, double r){
  v3->v[0] = r;
}

void v3SetAlphaf(V3 *v3, double alpha){
  v3->v[1] = alpha;
}

void v3SetDeltaf(V3 *v3, double delta){
  v3->v[2] = delta;
}

/**********************************************************************/
/* Some astro convenience functions.                                  */
/**********************************************************************/
void v3DecRAf(V3 *const v3, double x){
  v3DecAlphaf(v3,x);
}

void v3DecDecf(V3 *const v3, double x){
  v3DecDeltaf(v3,x);
}

void v3DivRAf(V3 *const v3, double x){
  v3DivAlphaf(v3, x);
}

void v3DivDecf(V3 *const v3, double x){
  v3DivDeltaf(v3, x);
}

double v3GetRAf(const V3 v3){
  return v3GetAlphaf(v3);
}

double v3GetDecf(const V3 v3){
  return v3GetDeltaf(v3);
}

void v3IncRAf(V3 *const v3, double x){
  v3IncAlphaf(v3, x);
}

void v3IncDecf(V3 *const v3, double x){
  v3IncDeltaf(v3, x);
}

void v3MulRAf(V3 *const v3, double x){
  v3MulAlphaf(v3, x);
}

void v3MulDecf(V3 *const v3, double x){
  v3MulDeltaf(v3, x);
}

void v3SetRAf(V3 *const v3, double ra){
  v3SetAlphaf(v3, ra);
}

void v3SetDecf(V3 *const v3, double dec){
  v3SetDeltaf(v3, dec);
}

