#include "tpm/times.h"
#include <stdio.h>

int main(){
  YMD ymd;
  JD jd;
  #define L 4
  double y[L][6] = {
    {1858.0, 11.0, 17.0, 0.0, 0.0, 0.0},
    {1949.0, 12.0, 31.923459, 0.0, 0.0, 0.0},
    {2000.0, 1.0, 1.5, 0.0, 0.0, 0.0},
    {1984.0, 1.0, 1.0, 0.0, 0.0, 0.0}
  };

  for(int i=0; i < L; i++){
    ymdSetYear(ymd, (int)y[i][0]);
    ymdSetMonth(ymd, (int)y[i][1]);
    ymdSetDay(ymd, y[i][2]);
    ymdSetHours(ymd, y[i][3]);
    ymdSetMinutes(ymd, y[i][4]);
    ymdSetSeconds(ymd, y[i][5]);

    printf("%4d %2d %10.6f %10.6f %10.6f %10.6f ", ymdGetYear(ymd),
           ymdGetMonth(ymd), ymdGetDay(ymd), ymdGetHours(ymd),
           ymdGetMinutes(ymd), ymdGetSeconds(ymd));
    
    jd = ymd2jd(ymd);
    printf("%16.8f %10.6f %10.6f %10.6f\n", jdGetDay(jd), jdGetHours(jd),
           jdGetMinutes(jd), jdGetSeconds(jd));

  }
}
