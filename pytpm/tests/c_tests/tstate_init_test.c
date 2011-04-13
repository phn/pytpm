#include <stdio.h>
#include "tpm/astro.h"
#include "print_tstate.h"


int main(){
  TPM_TSTATE tstate;
  
  tpm_data(&tstate, TPM_INIT);
  print_tstate(&tstate);

  return 0;
}
