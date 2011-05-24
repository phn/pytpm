#include <stdio.h>
#include "tpm/astro.h"

int main(){
  #define L 2
  V6 v6b, v6h;
  double tdt[L] = {J2000, J1984}; /* Take these as TT(TDT) */
  v6b = v6init(CARTESIAN);
  v6h = v6init(CARTESIAN);
  for (int i=0; i < L; i++){
    evp(tdt2tdb(tdt[i]),&v6b,&v6h);
    printf("V6B: X %.9f \tY %.9f \tZ %.9f \nXDOT %.9f \tYDOT %.9f\tZDOT %.9f\n",
         v6GetX(v6b), v6GetY(v6b), v6GetZ(v6b), v6GetXDot(v6b),
         v6GetYDot(v6b), v6GetZDot(v6b));
    printf("V6H: X %.9f \tY %.9f \tZ %.9f \nXDOT %.9f \tYDOT %.9f \tZDOT %.9f\n",
         v6GetX(v6h), v6GetY(v6h), v6GetZ(v6h), v6GetXDot(v6h),
         v6GetYDot(v6h), v6GetZDot(v6h));
    printf("\n");
  }

  return 0;
}
