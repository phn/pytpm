#include "tpm/astro.h"
#include <stdio.h>
#include <math.h>

int main(){
  V6 v6;
  DMS dms;
  HMS hms;
  double ra=0.0, de=0.0, pmra=0.0, pmde=0.0, px=0.0, rv=0.0, C=0.0;
  /* Barnard's star from Hipparcos catalog. 
     ICRS Epoch J1991.25 */
  ra = d2r(269.45402305);
  de = d2r(4.66828815);
  px = 549.01 / 1000.0; /* Arc seconds */
  rv = 0.0;
  pmra = (-797.84 / 1000.0 ) / cos(de); /* pmra * cos(de) into pmra */
  pmra *= 100.0; /* Arcseconds per century. */
  pmde = (10326.93 / 1000.0);
  pmde *= 100.0; /* Arcseconds per century. */
  C = CJ;
  printf("RA %f DE %f PMRA %f PMDE %f PX %f RV %f\n",
         ra, de, pmra, pmde, px, rv);

  v6 = v6init(CARTESIAN);
  v6 = cat2v6(ra, de, pmra, pmde, px, rv, C);
  v6 = proper_motion(v6, J2000, JYEAR2JD(1991.25));
  printf("RAJ2000: %s DEJ2000:%s\n", fmt_alpha(v6GetAlpha(v6c2s(v6))),
  fmt_d(r2d(v6GetDelta(v6c2s(v6)))));

  hms = hms2hms(r2hms(v6GetAlpha(v6c2s(v6))));
  dms = dms2dms(r2dms(v6GetDelta(v6c2s(v6))));
  printf("RAJ2000: hh %.1f mm %.1f ss %.4f\n", hms.hh, hms.mm, hms.ss);
  printf("DEJ2000: dd %.1f mm %.1f ss %.4f\n", dms.dd, dms.mm, dms.ss);
  
  return 0;
}
  
