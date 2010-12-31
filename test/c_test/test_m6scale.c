#include "tpm/vec.h"
#include <stdio.h>

int main(int argc, char const *argv){
  M6 m6_1, m6;
  M3 m;
  
  int row, col, i, j;
  
  m6_1 = m6Qx(1.23456789, 0.34567);
  m6 = m6scale(m6_1, 7.65432);

  for(i = 0; i <= 1; i++){
    for (j = 0; j <= 1; j++){
      printf("m6[%d][%d]\n",i,j);
      m = m6.m[i][j];
      for(row = 0; row < 3; row++){
        for(col = 0; col < 3; col++){
          printf("m3[%d][%d]\t %f ",row, col, m.m[row][col]);
        }
        printf("\n");
      }
    }
  }
  
  
  return 0;
}
