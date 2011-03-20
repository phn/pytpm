#include "tpm/times.h"
#include <stdio.h>

int main(){
  YMD ymd;
  #define L 4
  double y[L][2] = {
    {1858.0, 321.0},
    {1949.0, 365.9234590},
    {2000.0, 1.5},
    {1984.0, 1.0}
  };

  for(int i=0; i < L; i++){

    printf("%4d %12.7f\n", (int)y[i][0], y[i][1]);
    ymd = ydd2ymd((int)y[i][0], y[i][1]);

    printf("%4d %2d %10.6f %10.6f %10.6f %10.6f\n", ymdGetYear(ymd),
           ymdGetMonth(ymd), ymdGetDay(ymd), ymdGetHours(ymd),
           ymdGetMinutes(ymd), ymdGetSeconds(ymd));
    
  }

  return 0;

}
