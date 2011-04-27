#include "tpm/times.h"
#include <stdio.h>

int main(){
  YMD ymd;
  JD jd;
  #define L 4
  double j[L] = {MJD_0, B1950, J2000, J1984};
  
  for(int i=0; i < L; i++){
    jd = j2jd(j[i]);
    ymd = jd2ymd(jd);
    printf("%16.8f %10.6f %10.6f %10.6f ", jdGetDay(jd), jdGetHours(jd),
           jdGetMinutes(jd), jdGetSeconds(jd));
    printf("%4d %2d %10.6f %10.6f %10.6f %10.6f\n", ymdGetYear(ymd),
           ymdGetMonth(ymd), ymdGetDay(ymd), ymdGetHours(ymd),
           ymdGetMinutes(ymd), ymdGetSeconds(ymd));
  }

  return 0;
}
