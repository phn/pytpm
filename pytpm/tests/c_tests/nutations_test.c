#include <stdio.h>
#include "tpm/astro.h"

int main(){
  double delta_phi, delta_eps;
  nutations(J2000, &delta_phi, &delta_eps);
  printf("%.10f %.10f %.10f\n", J2000, delta_phi, delta_eps);

  return 0;
}
