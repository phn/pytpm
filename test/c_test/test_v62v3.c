#include "tpm/vec.h"
#include <stdio.h>

int main(void){
  V6 v6;
  V3 v3_1, v3_2;

  v3SetType(v3_1, CARTESIAN);
  v3SetX(v3_1, 1123.4556);
  v3SetY(v3_1, 4556.1123);
  v3SetZ(v3_1, 9876.1267);

  v3SetType(v3_2, CARTESIAN);
  v3SetX(v3_2, 2.3456);
  v3SetY(v3_2, 6.7891);
  v3SetZ(v3_2, 7.8912);

  v6SetPos(v6, v3_1);
  v6SetVel(v6, v3_2);

  v6SetType(v6, CARTESIAN);

  v3_1 = v62v3(v6, 1.234);
  
  printf("%d %f %f %f\n", v3GetType(v3_1), v3GetX(v3_1), v3GetY(v3_1),
         v3GetZ(v3_1));
}
