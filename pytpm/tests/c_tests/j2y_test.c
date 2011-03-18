#include "tpm/times.h"
#include <stdio.h>

int main(){
  #define L 4
  double j[L] = {
    MJD_0, B1950, J2000, J1984
  };

  for(int i=0; i < L; i++){
    printf("%16.8f %13.12f\n", j[i], j2y(j[i]));
  }

  return 0;
}
