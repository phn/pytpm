#include "tpm/vec.h"
#include <stdio.h>

int main(void){
  V3 v3_1, v3_2;
  double x;
  
  v3SetType(v3_1, CARTESIAN);
  v3SetX(v3_1, 1123.4556);
  v3SetY(v3_1, 4556.1123);
  v3SetZ(v3_1, 9876.1267);

  v3SetType(v3_2, CARTESIAN);
  v3SetX(v3_2, 2.3456);
  v3SetY(v3_2, 6.7891);
  v3SetZ(v3_2, 7.8912);

  x = v3dot(v3_1, v3_2);

  printf("%f\n", x);

}
