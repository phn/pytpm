#include <stdio.h>
#include "tpm/astro.h"

int main(){
  V6 v6;
  v6 = geod2geoc(d2r(30.567), d2r(46.713), 1500.0);

  printf("X %.9f \tY %.9f \tZ %.9f \nXDOT %.9f \tYDOT %.9f \tZDOT %.9f\n",
         v6GetX(v6), v6GetY(v6), v6GetZ(v6), v6GetXDot(v6),
         v6GetYDot(v6), v6GetZDot(v6));

  return 0;

}
