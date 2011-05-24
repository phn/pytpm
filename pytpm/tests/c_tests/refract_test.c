#include <stdio.h>
#include "tpm/astro.h"

int main(){
  #define L 1
  double zx[L] = {M_PI/6.0};
  double refa = 0.0, refb = 0.0, z = 0.0;
  refco(M_PI/3.0, 2093.093, 273.15, 1013.25, 0.0, 0.550, 1e-8,
        &refa, &refb);
  for (int i=0; i < L; i++){
    z = refract(zx[i], refa, refb, 1);
    printf("%.10f %.10f %.9f\n", refa, refb, z);
  }
  
  return 0;
}
