#include "tpm/times.h"
#include <stdio.h>

int main(){
  JD jd;
  #define L 2
  double j[L] = {
    2451545.41666667, 2433143.09261968
  };

  for(int i=0; i < L; i++){

    printf("%16.8f\n\n", j[i]);    
    jd = j2jd(j[i]);
    printf("%16.8f %8.4f %8.4f %8.4f\n", jdGetDay(jd), jdGetHours(jd),
           jdGetMinutes(jd), jdGetSeconds(jd));
   
  }
  return 0;
}
