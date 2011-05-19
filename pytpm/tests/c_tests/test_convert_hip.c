#include <stdio.h>
#include <stdlib.h>
#include "tpm/astro.h"

int main(){
  #define NUMDATA 1180
  double ra[NUMDATA];
  double de[NUMDATA];
  double ra1_d, de1_d;
  double ep = J2000;
  double eq = J2000;
  V6 v6;
  V6 pvec[N_TPM_STATES];
  TPM_TSTATE tstate;
  int s1, s2, c, i;
  FILE *fp;
  char * fname = "../data/hip.txt";

  /* Read data in: CHANGE THIS AS REQUIRED, REDIRECT OUTPUT. 
     Order in the above file is : 1991, j2000, b1950, gal, ecl.
     In the fscanf line put add * to all fields no required. For example
     to read in J2000 ra and dec remove * from 3rd and 4th %lf in fscanf.
     Then change s1, s2, ep and eq, if necessary.
     Redirect the output to a file, for example: hip_fk5j2000_gal.txt.
   */

  fp = fopen(fname,"r");
    if (fp == NULL){
    exit(1);
  }

  for (i=0; i < NUMDATA; i++){
    c = fscanf(fp,"%*lf %*lf %lf %lf %*lf %*lf %*lf %*lf %*lf %*lf",ra+i, de+i);
    if (c == EOF)
      break;
  }
  fclose(fp);
  
  s1 = TPM_S06;
  s2 = TPM_S05;
  ep = J2000;
  eq = J2000;

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
     
    ra1_d = r2d(r2r(v6GetAlpha(v6)));
    de1_d = r2d(v6GetDelta(v6));
    
    printf("%.8f %.8f\n", ra1_d, de1_d);

  }

  return 0;

}
