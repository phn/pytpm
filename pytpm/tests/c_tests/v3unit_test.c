#include "tpm/vec.h"
#include <stdio.h>

int main(){
  V3 v3, v3_1;
  v3 = v3init(CARTESIAN);
  v3SetX(v3, 12.34567);
  v3SetY(v3, 34.56712);
  v3SetZ(v3, 56.71234);
  v3_1 = v3unit(v3);

  printf("%d %0.8f %0.8f %0.8f\n", v3GetType(v3_1), v3GetX(v3_1), v3GetY(v3_1),
         v3GetZ(v3_1));
      
  return 0;

}
