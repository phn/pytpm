#include "tpm/times.h"
#include <stdio.h>

int main(){
  YMD ymd;
  #define L 5
  double y[L][6] = {
    {2000.0, 11.0, 366.0, 0.0, 0.0, 86400*365},
    {2000.0, 0.0, 0.0, 0.0, 0.0, 0.0},
    {2000.0, -3.0, 0.0, 0.0, 0.0, 0.0},
    {2000.0, 1.0, -365.0, 0.0, 0.0, 0.0},
    {2000.0, 1.0, 1.0, -24.0, 0.0, 0.0}
  };

    for(int i=0; i < L; i++){
    ymdSetYear(ymd, (int)y[i][0]);
    ymdSetMonth(ymd, (int)y[i][1]);
    ymdSetDay(ymd, y[i][2]);
    ymdSetHours(ymd, y[i][3]);
    ymdSetMinutes(ymd, y[i][4]);
    ymdSetSeconds(ymd, y[i][5]);

    printf("%4d %2d %10.6f %10.6f %10.6f %10.6f\n", ymdGetYear(ymd),
           ymdGetMonth(ymd), ymdGetDay(ymd), ymdGetHours(ymd),
           ymdGetMinutes(ymd), ymdGetSeconds(ymd));

    ymd = ymd2ymd(ymd);

    printf("%4d %2d %10.6f %10.6f %10.6f %10.6f\n\n", ymdGetYear(ymd),
           ymdGetMonth(ymd), ymdGetDay(ymd), ymdGetHours(ymd),
           ymdGetMinutes(ymd), ymdGetSeconds(ymd));

    }
}
