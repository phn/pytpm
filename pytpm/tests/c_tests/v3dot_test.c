#include "tpm/vec.h"
#include <stdio.h>

int main(){
  V3 v3_1, v3_2;
  double x;
  #define L 2
  double z[L][3] = {
    {1.67, -1.234, 4.345},
    {178.5, -0.234, -5.432}
  };
  
  for(int i=0; i < L; i += 2){
    v3SetType(v3_1, SPHERICAL);
    v3SetR(v3_1, z[i][0]);
    v3SetAlpha(v3_1, z[i][1]);
    v3SetDelta(v3_1, z[i][2]);
    v3SetType(v3_2, SPHERICAL);
    v3SetR(v3_2, z[i+1][0]);
    v3SetAlpha(v3_2, z[i+1][1]);
    v3SetDelta(v3_2, z[i+1][2]);

    printf("%d %.8f %.10f %.10f\n", v3GetType(v3_1), v3GetR(v3_1), v3GetAlpha(v3_1),
         v3GetDelta(v3_1));
    printf("%d %.8f %.10f %.10f\n", v3GetType(v3_2), v3GetR(v3_2), v3GetAlpha(v3_2),
         v3GetDelta(v3_2));

    x = v3dot(v3_2, v3_1);
    printf("%0.8f\n", x);
  }
  return 0;
}
