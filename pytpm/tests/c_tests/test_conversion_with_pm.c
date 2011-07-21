#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "tpm/astro.h"

int main(){
  #define NUMDATA 1180
  double ra[NUMDATA];
  double de[NUMDATA];
  double pmra[NUMDATA];
  double pmde[NUMDATA];
  double plx[NUMDATA];
  double ra1, de1, pmra1, pmde1, plx1, rv1;
  double ep, ep2;
  double eq;
  V6 v6;
  V6 pvec[N_TPM_STATES];
  TPM_TSTATE tstate;
  int s1, s2, c, i;
  FILE *fp;
  char * fname = "../data/hip_icrs.txt";

  fp = fopen(fname,"r");
    if (fp == NULL){
    exit(1);
  }

  for (i=0; i < NUMDATA; i++){
    /* File contains RA 1991.25, DE 1991.25, pmra, pmde*/
    c = fscanf(fp,"%lf %lf %lf %lf %lf",ra+i, de+i, pmra+i, pmde+i, plx+i);
    if (c == EOF)
      break;
    /* Convert pmra*cos(de) into pmra and change units from 
       milli-arcsec/year into arcsec/century.*/
    ra[i] = d2r(ra[i]);
    de[i] = d2r(de[i]);
    pmra[i] = ((pmra[i]/1000.0) / cos(de[i])) * 100.0;
    pmde[i] = (pmde[i]/1000.0) * 100.0;
  }
  fclose(fp);

  s1 = TPM_S06;
  ep = y2j(1991.25);
  eq = J2000; /* ICRS is approximately J2000 */
  /* Change s2,ep2 as required, redirect output to appropriate file.*/
  s2 = TPM_S13;
  ep2 = J2000;

  tpm_data(&tstate, TPM_INIT);
  tstate.utc = J2000;
  tstate.lon = d2r(-111.598333);
  tstate.lat = d2r(31.956389);
  tstate.alt = 2093.093;
  tstate.delta_at = delta_AT(tstate.utc);
  tstate.delta_ut = delta_UT(tstate.utc);
  tpm_data(&tstate, TPM_ALL);
  
  for(int i=0; i < NUMDATA; i ++){   
    v6 = cat2v6(ra[i], de[i], pmra[i], pmde[i], plx[i], 0.0, CJ);
    pvec[s1] = v6;
    tpm(pvec, s1, s2, ep, eq, &tstate);
    v6 = pvec[s2];

    /* Apply proper motion to required epoch. */
    proper_motion(v6, ep2, ep);

    v62cat(&ra1, &de1, &pmra1, &pmde1, &plx1, &rv1, v6, CJ);
    printf("%14.9f %14.9f %11.5f %11.5f %14.9f %14.9f\n", r2d(r2r(ra1)), 
           r2d(de1), pmra1, pmde1, plx1, rv1);

  }

  return 0;

}
