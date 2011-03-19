#include "tpm/times.h"
#include <stdio.h>
#include <math.h>

int main(){
  #define L 12
  #define DEG (180.0/M_PI)
  double r[L] = {
    0.0, -0.0, M_PI/2.0, -M_PI/2.0, 2*M_PI, -2*M_PI,
    -3*M_PI, 3*M_PI, 4*M_PI, -4*M_PI, 4.2*M_PI, -4.2*M_PI
  };

  for(int i=0; i < L; i++){
    /*printf("%9.6f %10.6f %9.6f %10.6f\n", r[i], r[i]*DEG, r2r(r[i]), r2r(r[i])*DEG);*/
    printf("%12.8f %12.8f\n", r[i],r2r(r[i]));
  }

  return 0;
}
