#include "tpm/times.h"
#include <stdio.h>

int main(){
  #define L 12
  double h[L] = {
    0.0, -0.0, 13.45, -13.45, 24.0, -24.0, 
      25.0, -25.0, 50.0, -50.0, 64.123, -64.123
  };

  for(int i=0; i < L; i++){
    printf("%8.4f %8.4f\n", h[i], h2h(h[i]));
  }

  return 0;
}
