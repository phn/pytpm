#include "tpm/astro.h"
#include <stdio.h>
#include <math.h>

/* Take a coordinate through all states. */
/* Coordinates for M100 from SIMBAD. */

int main(){
  double ra = (12+22/60.0+54.899/3600.0) * (2*M_PI/24.0);
  double de = (15+49/60.0+20.57/3600.0) * (2*M_PI/360.0);
  double ra1, ra1_d, de1, de1_d;
  double ep = J2000;
  double eq = J2000;
  DMS ra_dms, de_dms;
  V6 v6;
  V6 pvec[N_TPM_STATES];
  TPM_TSTATE tstate;
  int s1 = TPM_S06; /* Heliocentric mean J2000 FK5 ~~ ICRS */
  int s2 = TPM_S00; /* Assign required states. */

  for(int i=TPM_S00; i < N_TPM_STATES; i ++){
    tpm_data(&tstate, TPM_INIT);
    tstate.utc = J2000;
    tstate.lon = d2r(-111.598333);
    tstate.lat = d2r(31.956389);
    tstate.alt = 2093.093;
    tstate.delta_ut = delta_UT(tstate.utc);
    tpm_data(&tstate, TPM_ALL);
     
    v6 = v6init(SPHERICAL);
    v6SetR(v6, 1e9);
    v6SetAlpha(v6, ra);
    v6SetDelta(v6, de);
     
    pvec[s1] = v6s2c(v6);
    s2 = i;
    tpm(pvec, s1, s2, ep, eq, &tstate);
    v6 = v6c2s(pvec[s2]);
     
    ra_dms = dms2dms(r2dms(v6GetAlpha(v6)));
    de_dms = dms2dms(r2dms(v6GetDelta(v6)));
    
    printf("%02d-%02d %7.2f %7.2f %8.4f %7.2f %7.2f %8.4f\n", 
           s1, s2, ra_dms.dd, ra_dms.mm, ra_dms.ss, 
           de_dms.dd, de_dms.mm, de_dms.ss);

  }
  return 0;
}
