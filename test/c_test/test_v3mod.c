#include "tpm/vec.h"
#include <stdio.h>

int main(void){
  V3 v3;
  double x;

  v3SetType(v3, CARTESIAN);
  v3SetX(v3, 1123.4556);
  v3SetY(v3, 4556.1123);
  v3SetZ(v3, 9876.1267);

  x = v3mod(v3);

  printf("%f\n", x);
}
