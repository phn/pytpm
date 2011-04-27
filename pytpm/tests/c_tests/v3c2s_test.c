#include "tpm/vec.h"
#include <stdio.h>

int main(void){
  V3 v3;

  v3SetType(v3, CARTESIAN);
  v3SetX(v3, 1123.4556);
  v3SetY(v3, 4556.1123);
  v3SetZ(v3, 9876.1267);

  v3 = v3c2s(v3);

  printf("%d %.8f %.10f %.10f\n", v3GetType(v3), v3GetR(v3), v3GetAlpha(v3),
         v3GetDelta(v3));

  return 0;
}
