#include "tpm/astro.h"
#include <stdio.h>
#include <math.h>

int main(){
  V6 v6;
  double ra=0.0, de=0.0, pmra=0.0, pmde=0.0, px=0.0, rv=0.0, C=0.0;
  double ra1=0.0, de1=0.0, pmra1=0.0, pmde1=0.0, px1=0.0, rv1=0.0;
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
  printf("X %.10f \tY %.10f \tZ %.10f \nXDOT %.10f \tYDOT %.10f \tZDOT %.10f\n",\
         v6GetX(v6), v6GetY(v6), v6GetZ(v6), v6GetXDot(v6),
         v6GetYDot(v6), v6GetZDot(v6));
  
  v62cat(&ra1, &de1, &pmra1, &pmde1, &px1, &rv1, v6, C);
  printf("RA %f DE %f PMRA %f PMDE %f PX %f RV %f\n",
         r2r(ra1), r2r(de1), pmra1, pmde1, px1, rv1);
  
  /*  v6 = proper_motion(v6, J2000, JYEAR2JD(1991.25));
  printf("RAJ2000: %s DEJ2000:%s\n", fmt_alpha(v6GetAlpha(v6c2s(v6))),
  fmt_d(r2d(v6GetDelta(v6c2s(v6)))));*/

  return 0;
}
