#include <stdio.h>
#include "tpm/astro.h"

int main(){
  #define L 2
  double ep[L] = {J2000, J1984};
  for(int i=0; i < L; i++){
    printf("Ep %.10f E %.10f Edot %.10f\n", ep[i], obliquity(ep[i]),
           obliquity_dot(ep[i]));
  }

  return 0;
}
