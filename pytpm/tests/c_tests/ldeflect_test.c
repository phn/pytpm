#include <stdio.h>
#include "tpm/astro.h"

int main(){
  V6 v6h, v6, v61;
  v6h = v6init(CARTESIAN);
  v61 = v6init(CARTESIAN);
  v6 = v6init(CARTESIAN);
  
  evp(J2000, &v61, &v6h);

  v61 = v6init(SPHERICAL);
  v6SetR(v61, 1);
  v6SetAlpha(v61, d2r(34.56));
  v6SetDelta(v61, d2r(46.19));
  v61 = v6s2c(v61);
 
  v6 = ldeflect(v61, v6h, 1);
  v6 = v6c2s(v6);

  printf("R %.10f \tALPHA %.10f \tDELTA %.10f \nRDOT %.10f \tALPHADOT %.10f \tDELTADOT %.10f\n",
         v6GetR(v6), v6GetAlpha(v6), v6GetDelta(v6),
         v6GetRDot(v6), v6GetAlphaDot(v6), v6GetDeltaDot(v6));

  return 0;  
}
