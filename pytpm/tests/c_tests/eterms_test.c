#include <stdio.h>
#include "tpm/astro.h"

/* Simple test of aberrate function: just add the velocity of second to
   first. */
int main(){
  V6 v6;
  #define L 2
  double ep[L] = {J2000, J1984};
  v6 = v6init(CARTESIAN);
  
  for(int i=0; i < L; i++){
    v6 = eterms(ep[i]);
    
    printf("X %.10f \tY %.10f \tZ %.10f \nXDOT %.10f \tYDOT %.10f \tZDOT %.10f\n",
           v6GetX(v6), v6GetY(v6), v6GetZ(v6), v6GetXDot(v6),
           v6GetYDot(v6), v6GetZDot(v6));
    
  }

 
  return 0;
}
