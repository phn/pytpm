#include "tpm/astro.h"
#include "print_tstate.h"
#include <stdio.h>
#include <stdlib.h>

/* Usage: ./tpm_data_test_exe INTEGER; see below. */

int main(int argc, char* argv[]){
  TPM_TSTATE tstate;
  int flag = 0;
  double utc = 2451545.6789234;
  tpm_data(&tstate, TPM_INIT);
  tstate.utc = utc;
  tstate.delta_at = delta_AT(utc);
  tstate.delta_ut = delta_UT(utc);
  tstate.lon = -111.598333;
  tstate.lat = 31.956389;
  tstate.alt = 2093.093;
  /* All other parameters are defaults. */

  for(int i = 1; i < argc; i++){
    flag = atoi(argv[i]);
    /* INIT = 1, FAST = 2, MEDIUM = 4, SLOW = 8, REFRACTION = 16 
       ALL = 30 (everything except INIT)*/
    if (flag & TPM_INIT){
      printf("TPM_INIT ");
    }
    if (flag & TPM_FAST){
      printf("TPM_FAST ");
    }
    if (flag & TPM_MEDIUM) {
      printf("TPM_MEDIUM ");
    }
    if (flag & TPM_REFRACTION){
      printf("TPM_REFRACTION ");
    }
    if (flag & TPM_SLOW){
      printf("TPM_SLOW ");
    }
    if (flag & TPM_ALL){
      printf("TPM_ALL ");
    }

    tpm_data(&tstate, flag);
      
    print_tstate(&tstate);
  }
  
  return 0;
}

