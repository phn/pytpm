#include "tpm/times.h"
#include <stdio.h>

int main() {
  printf("%f %s\n", 1.23, fmt_r(1.23));
  printf("%f %s\n", -1.23, fmt_r(-1.23));

  return 0;
}
