#include "tpm/times.h"
#include <stdio.h>

int main(){
  HMS hms;
  #define L 8
  double hh[L][3] = {
    {23.345, 0.0, 0.0},
    {25.0, 0.0, 0.0},
    {6.0,128.0,2000.0},
    {12.456, 0.0,0.0},
    {-12.456, 0.0,0.0},
    {-25.0,0.0,0.0},
    {-1.0,-1.0,-1.0},
    {-100.0,0.0,0.0},
  };

  for(int i=0; i < L; i++){
    hmsSetHours(hms, hh[i][0]);
    hmsSetMinutes(hms, hh[i][1]);
    hmsSetSeconds(hms, hh[i][2]);
    printf("%06.4f %6.4f %6.4f ", hmsGetHours(hms), hmsGetMinutes(hms),
           hmsGetSeconds(hms));
    hms = hms2hms(hms);
    printf("%06.4f %6.4f %6.4f\n", hmsGetHours(hms), hmsGetMinutes(hms),
           hmsGetSeconds(hms));

  }
}
