#include <stdio.h>
#include "tpm/astro.h"

int main(){
  /* Calculate "Deltas" in various time scales for a set of UTC values.*/
  #define L 5
  double utc[L] = {MJD_0, B1950, J2000, J1984, 2455667.9002314815};
  double ut1 = 0.0;

  for(int i=0; i < L; i++){
    printf("***********************************\n");
    printf("UTC:      %-.12f\n", utc[i]);
    printf("Delta AT: %-.1f\n", delta_AT(utc[i]));
    printf("Delta UT: %-.12f\n", delta_UT(utc[i]));
    ut1 = utc[i]+ delta_UT(utc[i]);
    printf("Delta T : %-.12f\n", delta_T(ut1));
    printf("Delta ET: %-.12f\n", delta_ET(utc[i]));
    printf("Delta TT: %-.12f\n", delta_TT(utc[i]));
  }

  return 0;
  
}
