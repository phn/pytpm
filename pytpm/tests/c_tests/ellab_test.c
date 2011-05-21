#include <stdio.h>
#include "tpm/astro.h"

int main(){
  V6 v6;

  v6 = v6init(SPHERICAL);
  v6SetR(v6, 1e9);
  v6SetAlpha(v6, h2r(20.0));
  v6SetDelta(v6, d2r(40.0));
  v6 = v6s2c(v6);

  v6 = v6c2s(ellab(J2000, v6, -1));


  printf("X %.9f \tY %.9f \tZ %.9f \nXDOT %.9f \tYDOT %.9f \tZDOT %.9f\n",
         v6GetX(v6), r2h(r2r(v6GetY(v6))), r2d(r2r(v6GetZ(v6))), v6GetXDot(v6),
         v6GetYDot(v6), v6GetZDot(v6));

  return 0;
}
