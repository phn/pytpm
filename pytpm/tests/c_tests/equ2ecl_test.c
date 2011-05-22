#include <stdio.h>
#include "tpm/astro.h"

int main(){
  V6 v6;
  v6 = v6init(CARTESIAN);
  v6SetX(v6, 0.5);
  v6SetY(v6, 0.173611298);
  v6SetZ(v6, 0.84844511);
  v6SetXDot(v6, -0.034000000);
  v6SetYDot(v6, 0.251873488);
  v6SetZDot(v6, -0.872330067);

  v6 = equ2ecl(v6, d2r(23.7));

  printf("X %.9f \tY %.9f \tZ %.9f \nXDOT %.9f \tYDOT %.9f \tZDOT %.9f\n",
         v6GetX(v6), v6GetY(v6), v6GetZ(v6), v6GetXDot(v6),
         v6GetYDot(v6), v6GetZDot(v6));

  return 0;
}
