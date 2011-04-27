#include "tpm/times.h"
#include <stdio.h>

int main(){
  JD jd;
  double t =0.0;
  #define L 2
  double j[L][4] = {
    {2451545.0, 10.0, 0.0, 0.0},
    {2433142.678, 10.123, -10.345, 1.04}
  };

  for(int i=0; i < L; i++){
    jdSetDay(jd, j[i][0]);
    jdSetHours(jd, j[i][1]);
    jdSetMinutes(jd, j[i][2]);
    jdSetSeconds(jd, j[i][3]);
    printf("%16.8f %8.4f %8.4f %8.4f\n", jdGetDay(jd), jdGetHours(jd),
           jdGetMinutes(jd), jdGetSeconds(jd));
    t = jd2j(jd);

    printf("%16.8f\n\n", t);

  }
  return 0;
}
