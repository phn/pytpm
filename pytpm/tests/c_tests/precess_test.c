#include <stdio.h>
#include "tpm/astro.h"

int main(){
  V6 v6;
   
  v6 = v6init(SPHERICAL);

  v6SetR(v6, 1e9);
  v6SetAlpha(v6, d2r(34.1592));
  v6SetDelta(v6, d2r(12.9638));
  v6SetRDot(v6, -0.123);
  v6SetAlphaDot(v6, 0.382);
  v6SetDeltaDot(v6, 1.0);

  v6 = v6s2c(v6);
  v6 = precess(J2000, J1984, v6, PRECESS_FK5);
  v6 = v6c2s(v6);

  printf("R %.10f \tALPHA %.10f \tDELTA %.10f \nRDOT %.10f \tALPHADOT %.10f \tDELTADOT %.10f\n",
         v6GetR(v6), v6GetAlpha(v6), v6GetDelta(v6),
         v6GetRDot(v6), v6GetAlphaDot(v6), v6GetDeltaDot(v6));

  return 0;  

    
}
