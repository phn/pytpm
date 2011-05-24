#include <stdio.h>
#include "tpm/astro.h"

int main(){

  printf("Ep %.10f %.10f theta %.10f thetadot %.10f\n", J1984, 
         J2000, theta(J1984, J2000, PRECESS_FK5), 
         thetadot(J1984, J2000, PRECESS_FK5));

  printf("Ep %.10f %.10f zee %.10f zeedot %.10f\n", J1984, 
         J2000, zee(J1984, J2000, PRECESS_FK5), 
         zeedot(J1984, J2000, PRECESS_FK5));

  printf("Ep %.10f %.10f zeta %.10f zetadot %.10f\n", J1984, 
         J2000, zeta(J1984, J2000, PRECESS_FK5), 
         zetadot(J1984, J2000, PRECESS_FK5));


  return 0;
}
