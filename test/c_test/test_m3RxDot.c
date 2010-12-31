#include "tpm/vec.h"
#include <stdio.h>

int main(int argc, char const *argv){
  M3 m3;
  m3 = m3RxDot(12.345, 1.2345);
  printf("%f %f %f %f\n", m3GetYY(m3), m3GetYZ(m3), m3GetZY(m3),
         m3GetZZ(m3));
  return 0;
}
