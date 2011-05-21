#include <stdio.h>
#include "tpm/astro.h"

int main(){
  V6 v6;
  #define L 3
  double ha, dec;
  double az[L] = {0, 90, 133.30805555555557};
  double el[L] = {90, -45, 59.086111111111116};

  v6 = v6init(SPHERICAL);
  v6SetR(v6, 1e9);
  for (int i=0; i < L; i++){
    v6SetAlpha(v6, d2r(az[i]));
    v6SetDelta(v6, d2r(el[i]));
    v6 = v6c2s(azel2hadec(v6s2c(v6), d2r(43.07833)));
    ha = r2d(r2r(v6GetAlpha(v6)));
    dec = r2d(r2r(v6GetDelta(v6)));
    printf("%.9f %.9f\n", ha, dec);
  }

  return 0;
}
