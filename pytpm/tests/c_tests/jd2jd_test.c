#include "tpm/times.h"
#include <stdio.h>

int main(){
  JD jd;
  #define L 3
  double j[L][4] = {
    {2451545.0, 25.0, 0.0, 0.0},
    {2451545.0, -12.0, 0.0, 0.0},
    {2441230.0, 0.0, 12345678.0, 12345.0345}
  };

  for(int i=0; i < L; i++){
    jdSetDay(jd, j[i][0]);
    jdSetHours(jd, j[i][1]);
    jdSetMinutes(jd, j[i][2]);
    jdSetSeconds(jd, j[i][3]);
    printf("%16.8f %8.4f %8.4f %8.4f ", jdGetDay(jd), jdGetHours(jd),
           jdGetMinutes(jd), jdGetSeconds(jd));
    jd = jd2jd(jd);
    printf("%16.8f %8.4f %8.4f %8.4f\n", jdGetDay(jd), jdGetHours(jd),
           jdGetMinutes(jd), jdGetSeconds(jd));

  }

  return 0;
}
