#include "tpm/times.h"
#include <stdio.h>



int main(){
  
  DMS dms;
  #define L 9
  double d[L] = {-12.245, 361.123, -358.0, -361.0, -360.0, 360.0, -710.0, 710,
                 -730.0};
  double m[L] = {0.0    ,   0.0  , 0.0   , 0.0,    0.0   , 0.0  , 0.0,    0.0,  
                 0.0};
  double s[L] = {0.0    ,   0.0  , 0.0   , 0.0,    0.0   , 0.0  , 0.0,    0.0,  
                 0.0};
  
  for(int i=0; i < L; i++){
    dmsSetDegrees(dms, d[i]);
    dmsSetMinutes(dms, m[i]);
    dmsSetSeconds(dms, s[i]);
    printf("%8.4f %8.4f %8.4f ", dmsGetDegrees(dms),
           dmsGetMinutes(dms), dmsGetSeconds(dms));
    dms = dms2dms(dms);
     
    printf("%8.4f %8.4f %8.4f\n", dmsGetDegrees(dms),
           dmsGetMinutes(dms), dmsGetSeconds(dms));

  }
  
  return 0;
}
