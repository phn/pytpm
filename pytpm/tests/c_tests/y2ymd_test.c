#include "tpm/times.h"
#include <stdio.h>

int main(){
  YMD ymd;
  #define L 2
  double y[L] = {
    1858.879452054794, 1950.002530024794
  };
  for(int i=0; i < L; i++){
    ymd = y2ymd(y[i]);

    printf("%17.12f\n", y[i]);
    printf("%4d %2d %10.6f %10.6f %10.6f %10.6f\n", ymdGetYear(ymd),
           ymdGetMonth(ymd), ymdGetDay(ymd), ymdGetHours(ymd),
           ymdGetMinutes(ymd), ymdGetSeconds(ymd));
    
  }

  return 0;

}
