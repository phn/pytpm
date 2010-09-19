#include "m3Functions.h"
/* Functions to access M3 vectors.
   
   In TPM these are defined as macros, which SWIG doesn't wrap. To
   get the same functionality from within python, we define the
   following functions and wrap them using SWIG.

   Author: Prasanth Nair
   Contact: prasanthhn@gmail.com
*/

void m3DecXXf(M3 *const m3, double x){
  m3->m[0][0] -= x;
}

void m3DecXYf(M3 *const m3, double x){
  m3->m[0][1] -= x;
}

void m3DecXZf(M3 *const m3, double x){
  m3->m[0][2] -= x;
}

void m3DecYXf(M3 *const m3, double x){
  m3->m[1][0] -= x;
}

void m3DecYYf(M3 *const m3, double x){
  m3->m[1][1] -= x;
}

void m3DecYZf(M3 *const m3, double x){
  m3->m[1][2] -= x;
}

void m3DecZXf(M3 *const m3, double x){
  m3->m[2][0] -= x;
}

void m3DecZYf(M3 *const m3, double x){
  m3->m[2][1] -= x;
}

void m3DecZZf(M3 *const m3, double x){
  m3->m[2][2] -= x;
}

void m3DivXXf(M3 *const m3, double x){
  m3->m[0][0] /= x;
}

void m3DivXYf(M3 *const m3, double x){
  m3->m[0][1] /= x;
}

void m3DivXZf(M3 *const m3, double x){
  m3->m[0][2] /= x;
}

void m3DivYXf(M3 *const m3, double x){
  m3->m[1][0] /= x;
}

void m3DivYYf(M3 *const m3, double x){
  m3->m[1][1] /= x;
}

void m3DivYZf(M3 *const m3, double x){
  m3->m[1][2] /= x;
}

void m3DivZXf(M3 *const m3, double x){
  m3->m[2][0] /= x;
}

void m3DivZYf(M3 *const m3, double x){
  m3->m[2][1] /= x;
}

void m3DivZZf(M3 *const m3, double x){
  m3->m[2][2] /= x;
}

double m3GetXXf(const M3 *const m3){
  return m3->m[0][0];
}

double m3GetXYf(const M3 *const m3){
  return m3->m[0][1];
}

double m3GetXZf(const M3 *const m3){
  return m3->m[0][2];
}

double m3GetYXf(const M3 *const m3){
  return m3->m[1][0];
}

double m3GetYYf(const M3 *const m3){
  return m3->m[1][1];
}

double m3GetYZf(const M3 *const m3){
  return m3->m[1][2];
}

double m3GetZXf(const M3 *const m3){
  return m3->m[2][0];
}

double m3GetZYf(const M3 *const m3){
  return m3->m[2][1];
}

double m3GetZZf(const M3 *const m3){
  return m3->m[2][2];
}

void m3IncXXf(M3 *const m3, double x){
  m3->m[0][0] += x;
}

void m3IncXYf(M3 *const m3, double x){
  m3->m[0][1] += x;
}

void m3IncXZf(M3 *const m3, double x){
  m3->m[0][2] += x;
}

void m3IncYXf(M3 *const m3, double x){
  m3->m[1][0] += x;
}

void m3IncYYf(M3 *const m3, double x){
  m3->m[1][1] += x;
}

void m3IncYZf(M3 *const m3, double x){
  m3->m[1][2] += x;
}

void m3IncZXf(M3 *const m3, double x){
  m3->m[2][0] += x;
}

void m3IncZYf(M3 *const m3, double x){
  m3->m[2][1] += x;
}

void m3IncZZf(M3 *const m3, double x){
  m3->m[2][2] += x;
}

void m3MulXXf(M3 *const m3, double x){
  m3->m[0][0] *= x;
}

void m3MulXYf(M3 *const m3, double x){
  m3->m[0][1] *= x;
}

void m3MulXZf(M3 *const m3, double x){
  m3->m[0][2] *= x;
}

void m3MulYXf(M3 *const m3, double x){
  m3->m[1][0] *= x;
}

void m3MulYYf(M3 *const m3, double x){
  m3->m[1][1] *= x;
}

void m3MulYZf(M3 *const m3, double x){
  m3->m[1][2] *= x;
}

void m3MulZXf(M3 *const m3, double x){
  m3->m[2][0] *= x;
}

void m3MulZYf(M3 *const m3, double x){
  m3->m[2][1] *= x;
}

void m3MulZZf(M3 *const m3, double x){
  m3->m[2][2] *= x;
}

void m3SetXXf(M3 *const m3, double x){
  m3->m[0][0] = x;
}

void m3SetXYf(M3 *const m3, double x){
  m3->m[0][1] = x;
}

void m3SetXZf(M3 *const m3, double x){
  m3->m[0][2] = x;
}

void m3SetYXf(M3 *const m3, double x){
  m3->m[1][0] = x;
}

void m3SetYYf(M3 *const m3, double x){
  m3->m[1][1] = x;
}

void m3SetYZf(M3 *const m3, double x){
  m3->m[1][2] = x;
}

void m3SetZXf(M3 *const m3, double x){
  m3->m[2][0] = x;
}

void m3SetZYf(M3 *const m3, double x){
  m3->m[2][1] = x;
}

void m3SetZZf(M3 *const m3, double x){
  m3->m[2][2] = x;
}

