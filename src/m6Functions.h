/* Declaration for functions to access V6 vectors, defined in v6Functions.c
   
   In TPM these are defined as macros, which SWIG doesn't wrap. To
   get the same functionality from within python, we define the
   following functions and wrap them using SWIG.

   Author: Prasanth Nair
   Contact: prasanthhn@gmail.com
*/
#ifndef M3_INCLUDE
#include "tpm/m3.h"
#endif
#ifndef M6_INCLUDE
#include "tpm/m6.h"
#endif


/*#define m6GetPP(m6)	(m6.m[0][0])*/
M3 m6GetPPf(const M6 *const m6);
/*#define m6GetPV(m6)	(m6.m[0][1])*/
M3 m6GetPVf(const M6 *const m6);
/*#define m6GetVP(m6)	(m6.m[1][0])*/
M3 m6GetVPf(const M6 *const m6);
/*#define m6GetVV(m6)	(m6.m[1][1])*/
M3 m6GetVVf(const M6 *const m6);

/*#define m6SetPP(m6,m3)	(m6.m[0][0] = (m3))*/
void m6SetPPf(M6 *const m6, M3 m3);
/*#define m6SetPV(m6,m3)	(m6.m[0][1] = (m3))*/
void m6SetPVf(M6 *const m6, M3 m3);
/*#define m6SetVP(m6,m3)	(m6.m[1][0] = (m3))*/
void m6SetVPf(M6 *const m6, M3 m3);
/*#define m6SetVV(m6,m3)	(m6.m[1][1] = (m3))*/
void m6SetVVf(M6 *const m6, M3 m3);

/* EXTERN_START */
/* EXTERN_STOP */

/*#endif*/
