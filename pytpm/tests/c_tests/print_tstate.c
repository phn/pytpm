#include <stdio.h>
#include "tpm/astro.h"

int print_tstate(TPM_TSTATE* tstate){
  /* Print the parameters in TPM_TSTATE structure. */

  printf("\n************ Independent parameters ************\n\n");
  printf("%-15s %.12f\n", "UTC", tstate->utc);
  printf("%-15s %d\n", "Delta AT", tstate->delta_at);
  printf("%-15s %.12f\n", "Detla UT", tstate->delta_ut);
  printf("%-15s %.12f\n", "Longitude", tstate->lon);
  printf("%-15s %.12f\n", "Latitude", tstate->lat);
  printf("%-15s %.12f\n", "Altitude", tstate->alt);
  printf("%-15s %.12f\n", "Xpole", tstate->xpole);
  printf("%-15s %.12f\n", "Ypole", tstate->ypole);
  printf("%-15s %.12f\n", "Temperature", tstate->T);
  printf("%-15s %.12f\n", "Pressure", tstate->P);
  printf("%-15s %.12f\n", "Humidity", tstate->H);
  printf("%-15s %.12f\n", "Wavelength", tstate->wavelength);

  printf("\n************ Dependent dynamical times ************\n\n");
  printf("%-15s %.12f\n", "TAI", tstate->tai);
  printf("%-15s %.12f\n", "TDT", tstate->tdt);
  printf("%-15s %.12f\n", "TDB", tstate->tdb);
  printf("\n************ Dependent geometrical quantities ************\n\n");
  printf("%-15s %.12f\n", "Obliquity", tstate->obliquity);
  printf("%-15s %.12f\n", "Nut Lon", tstate->nut_lon);
  printf("%-15s %.12f\n", "Nut Obl", tstate->nut_obl);
  printf("%-15s\n%s\n", "NM", m3fmt(tstate->nm));
  printf("%2s\n", "PM");
  for(int i=0; i < 2; i++){
    for(int j=0; j < 2; j++){
      printf("PM[%d][%d]\n%s\n", i,j, m3fmt(tstate->pm.m[i][j]));
    }
  }

  printf("\n************ Dependent rotational times ************\n\n");
  printf("%-15s %.12f\n", "Universal Time", tstate->ut1);
  printf("%-15s %.12f\n", "GMST", tstate->gmst); 
  printf("%-15s %.12f\n", "GAST", tstate->gast); 
  printf("%-15s %.12f\n", "LAST", tstate->last); 
  printf("\n************ Observer ephemerides ************\n\n");
  printf("%2s\n", "EB");
  printf("EB[POS]\n%s\n", v3fmt(tstate->eb.v[0]));
  printf("EB[VEL]\n%s\n", v3fmt(tstate->eb.v[1]));
  printf("%2s\n", "EH");
  printf("EH[POS]\n%s\n", v3fmt(tstate->eh.v[0]));
  printf("EH[VEL]\n%s\n", v3fmt(tstate->eh.v[1]));
  printf("%5s\n", "OBS_M");
  printf("OBS_M[POS]\n%s\n", v3fmt(tstate->obs_m.v[0]));
  printf("OBS_M[VEL]\n%s\n", v3fmt(tstate->obs_m.v[1]));
  printf("%5s\n", "OBS_T");
  printf("OBS_T[POS]\n%s\n", v3fmt(tstate->obs_t.v[0]));
  printf("OBS_T[VEL]\n%s\n", v3fmt(tstate->obs_t.v[1]));
  printf("%5s\n", "OBS_S");
  printf("OBS_S[POS]\n%s\n", v3fmt(tstate->obs_s.v[0]));
  printf("OBS_S[VEL]\n%s\n", v3fmt(tstate->obs_s.v[1]));
  printf("\n************ Dependent physical quantities ************\n\n");
  printf("%-15s %.12f\n", "Ref. A", tstate->refa);
  printf("%-15s %.12f\n", "Ref. B", tstate->refb);

  printf("\n");
  return 0;
}



















