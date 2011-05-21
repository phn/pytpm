#include <stdio.h>
#include "tpm/astro.h"

/* Simple test of aberrate function: just add the velocity of second to
   first. */
int main(){
  V6 v61, v62, v6;
  v6SetType(v61, CARTESIAN);
  v6SetX(v61, 1.0);
  v6SetY(v61, 2.0);
  v6SetZ(v61, 3.0);
  v6SetXDot(v61, 0.0);
  v6SetYDot(v61, 0.0);
  v6SetZDot(v61, 0.0);
  v6SetType(v62, CARTESIAN);
  v6SetX(v62, 0.0);
  v6SetY(v62, 0.0);
  v6SetZ(v62, 0.0);
  v6SetXDot(v62, -0.5);
  v6SetYDot(v62, -0.6);
  v6SetZDot(v62, -0.00345);

  v6 = aberrate(v61, v62, 1);
  printf("X %.9f \tY %.9f \tZ %.9f \nXDOT %.9f \tYDOT %.9f \tZDOT %.9f\n",
         v6GetX(v6), v6GetY(v6), v6GetZ(v6), v6GetXDot(v6),
         v6GetYDot(v6), v6GetZDot(v6));
  v6 = aberrate(v61, v62, -1);
  printf("X %.9f \tY %.9f \tZ %.9f \nXDOT %.9f \tYDOT %.9f \tZDOT %.9f\n",
         v6GetX(v6), v6GetY(v6), v6GetZ(v6), v6GetXDot(v6),
         v6GetYDot(v6), v6GetZDot(v6));
 
  return 0;
}
