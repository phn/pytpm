#include <stdio.h>
#include "tpm/astro.h"

int main(){
  V6 v6;

  v6 = v6init(SPHERICAL);
  v6SetR(v6, 1e9);
  v6SetAlpha(v6, d2r(23.15678));
  v6SetDelta(v6, d2r(54.3892));
  
  v6 = v6s2c(v6);

  v6 = fk425(v6);
  v6 = v6c2s(v6);

  printf("R %.10f \tα %.10f \tZ %.10f \nXDOT %.10f \tYDOT %.10f \tZDOT %.10f\n",
         v6GetR(v6), r2d(r2r(v6GetAlpha(v6))), r2d(r2r(v6GetDelta(v6))),
         v6GetRDot(v6), v6GetAlphaDot(v6), v6GetDeltaDot(v6));

}
