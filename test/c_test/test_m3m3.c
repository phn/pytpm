#include "tpm/vec.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv){

  int row, col;
  M3 m3_1, m3_2, m;
  m3_1 = m3I(1.0);
  m3_2 = m3I(2.0);

  for(row = 0; row < 3; row++){
    for(col = 0; col < 3; col++){
      m3_1.m[row][col] += drand48();
      m3_2.m[row][col] += drand48();
    }
  }

  m = m3m3(m3_1, m3_2);

  for(row = 0; row < 3; row++){
    for(col = 0; col < 3; col++){
      printf("%f %f %f\n",m.m[row][col], m3_1.m[row][col],
             m3_2.m[row][col]);
      }
  }

  return 0;
}
