#include "m6Functions.h"
/* Functions to access M6 vectors.
   
   In TPM these are defined as macros, which SWIG doesn't wrap. To
   get the same functionality from within python, we define the
   following functions and wrap them using SWIG.

   Author: Prasanth Nair
   Contact: prasanthhn@gmail.com
*/

M3 m6GetPPf(const M6 *const m6){
  return m6->m[0][0];
}

M3 m6GetPVf(const M6 *const m6){
  return m6->m[0][1];
}

M3 m6GetVPf(const M6 *const m6){
  return m6->m[1][0];
}

M3 m6GetVVf(const M6 *const m6){
  return m6->m[1][1];
}

void m6SetPPf(M6 *const m6, M3 m3){
  m6->m[0][0] = m3;
}

void m6SetPVf(M6 *const m6, M3 m3){
  m6->m[0][1] = m3;
}

void m6SetVPf(M6 *const m6, M3 m3){
  m6->m[1][0] = m3;
}

void m6SetVVf(M6 *const m6, M3 m3){
  m6->m[1][1] = m3;
}

