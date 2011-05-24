#include <stdio.h>
#include "tpm/astro.h"

int main(){
  #define L 1
  double ep[L] = {J2000};
  for(int i=0; i < L; i++){
    printf("Ep %.10f SP %.10f SPdot %.10f\n", ep[i], solar_perigee(ep[i]),
           solar_perigee_dot(ep[i]));
  }

  return 0;
}
