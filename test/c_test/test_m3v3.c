#include "tpm/vec.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv){

  int row, col;
  M3 m3_1;
  V3 v3;
  
  m3_1 = m3I(1.0);
  v3 = v3init(0);

  for(row = 0; row < 3; row++){
    v3.v[row] = drand48();
    printf("%f\n", v3.v[row]);
    for(col = 0; col < 3; col++){
      m3_1.m[row][col] += drand48();
      printf("%d %d %f\n", row, col, m3_1.m[row][col]);
    }
  }

  v3 = m3v3(m3_1, v3);
  for(row = 0; row < 3; row++){
    printf("%f\n", v3.v[row]);
  }

  return 0;
}
