#include <stdio.h>
#include "tpm/astro.h"

int main(){
  V6 v6;
  v6 = v6init(SPHERICAL);
  v6SetR(v6, 1.0);
  v6SetAlpha(v6, M_PI/4.0);
  v6SetDelta(v6, M_PI/4.0);
  v6 = v6s2c(v6);
  v6SetXDot(v6, -0.034);
  v6SetYDot(v6, -0.12);
  v6SetZDot(v6, -0.9);

  v6 = ecl2equ(v6, d2r(23.7));

  printf("X %.9f \tY %.9f \tZ %.9f \nXDOT %.9f \tYDOT %.9f \tZDOT %.9f\n",
         v6GetX(v6), v6GetY(v6), v6GetZ(v6), v6GetXDot(v6),
         v6GetYDot(v6), v6GetZDot(v6));

  return 0;
}
