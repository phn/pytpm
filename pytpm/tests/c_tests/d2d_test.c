#include "tpm/times.h"
#include <stdio.h>

int main(){
  #define L 12
  double d[L] = {
    0.0, -0.0, 360.0, -360.0, 12.3, -12.3,
    361.0, -361.0,  710.0, -710.0, 730.0, -730.0
  };

  for(int i=0; i < L; i++){
    printf("%8.4f %8.4f\n", d[i], d2d(d[i]));
  }

  return 0;
}
