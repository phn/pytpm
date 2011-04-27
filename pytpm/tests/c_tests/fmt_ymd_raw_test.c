#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
  YMD ymd;
  #define L 2
  double y[L][6] = {
    {2010.0, 10.0, 16.789, 15.654, 1.345, 9.45},
    {-1.0, 10.0, 1.0, 23.9999, 54.0, 9.45}
  };

  for(int i=0; i < L; i++){
    
    ymdSetYear(ymd, (int)y[i][0]);
    ymdSetMonth(ymd, (int)y[i][1]);
    ymdSetDay(ymd, y[i][2]);
    ymdSetHours(ymd, y[i][3]);
    ymdSetMinutes(ymd, y[i][4]);
    ymdSetSeconds(ymd, y[i][5]);
   
    printf("%s\n", fmt_ymd_raw(ymd));

  }
  
  return 0;
}
