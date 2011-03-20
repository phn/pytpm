#include "tpm/times.h"
#include <stdio.h>

int main(){
  printf("%f %s\n", 2000.0, fmt_y(2000.0));
  printf("%f %s\n", 1984.0, fmt_y(1984.0));
  printf("%f %s\n", 1950.0, fmt_y(1950.0));

  return 0;
}
