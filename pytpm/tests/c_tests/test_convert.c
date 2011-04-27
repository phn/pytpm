#include <stdio.h>
#include "tpm/astro.h"

int main(){
  #define NUMDATA 2
  /* HIP 118321, HIP 118322 RA J2000, DE J2000 */
  double ra[NUMDATA] = {359.97907800, 359.97945800};
  double de[NUMDATA] = {-65.57713200, -64.37231300};
  double ra1_d, de1_d;
  double ep = J2000;
  double eq = J2000;
  V6 v6;
  V6 pvec[N_TPM_STATES];
  TPM_TSTATE tstate;
  int s1 = TPM_S06; /* Heliocentric mean J2000 FK5 ~~ ICRS */
  int s2 = TPM_S04; /* Galactic. */

  tpm_data(&tstate, TPM_INIT);
  tstate.utc = J2000;
  tstate.lon = d2r(-111.598333);
  tstate.lat = d2r(31.956389);
  tstate.alt = 2093.093;
  tstate.delta_ut = delta_UT(tstate.utc);
  tpm_data(&tstate, TPM_ALL);
  
  for(int i=0; i < NUMDATA; i ++){   
    v6 = v6init(SPHERICAL);
    v6SetR(v6, 1e9);
    v6SetAlpha(v6, d2r(ra[i]));
    v6SetDelta(v6, d2r(de[i]));
     
    pvec[s1] = v6s2c(v6);
    tpm(pvec, s1, s2, ep, eq, &tstate);
    v6 = v6c2s(pvec[s2]);
     
    ra1_d = r2d(v6GetAlpha(v6));
    if(ra1_d < 0.0) ra1_d += 360.0;
    de1_d = r2d(v6GetDelta(v6));
    
    printf("%.8f %.8f\n", ra1_d, de1_d);

  }

  return 0;

}
