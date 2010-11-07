#include "tpm/vec.h"
#include <stdio.h>

int main(void){
  M3 m3_1;
  M6 m6;
  
	m3_1 = m3I(1.0);
	m6 = m6I(0);

	m3SetXX(m3_1, 0.2345); 
	m3SetXY(m3_1, 0.5432);	
	m3SetXZ(m3_1, 0.1234);	
	m3SetYX(m3_1, 0.5467);	
	m3SetYY(m3_1, 0.4190);	
	m3SetYZ(m3_1, 0.9874);	
	m3SetZX(m3_1, 0.1225);	
	m3SetZY(m3_1, 0.4331);	
	m3SetZZ(m3_1, 0.2309);	

	m6SetPP(m6, m3_1);

	m3SetXX(m3_1, 0.4523); 
	m3SetXY(m3_1, 0.3254);	
	m3SetXZ(m3_1, 0.3412);	
	m3SetYX(m3_1, 0.6754);	
	m3SetYY(m3_1, 0.9041);	
	m3SetYZ(m3_1, 0.7498);	
	m3SetZX(m3_1, 0.2512);	
	m3SetZY(m3_1, 0.3143);	
	m3SetZZ(m3_1, 0.0923);
	
	m6SetPV(m6, m3_1);

	m3SetXX(m3_1, 0.4253); 
	m3SetXY(m3_1, 0.3524);	
	m3SetXZ(m3_1, 0.3142);	
	m3SetYX(m3_1, 0.6574);	
	m3SetYY(m3_1, 0.9401);	
	m3SetYZ(m3_1, 0.7948);	
	m3SetZX(m3_1, 0.2152);	
	m3SetZY(m3_1, 0.4133);	
	m3SetZZ(m3_1, 0.2903);
	
	m6SetVP(m6, m3_1);

	m3SetXX(m3_1, 0.3524); 
	m3SetXY(m3_1, 0.4235);	
	m3SetXZ(m3_1, 0.2413);	
	m3SetYX(m3_1, 0.4756);	
	m3SetYY(m3_1, 0.1049);	
	m3SetYZ(m3_1, 0.8497);	
	m3SetZX(m3_1, 0.2512);	
	m3SetZY(m3_1, 0.3314);	
	m3SetZZ(m3_1, 0.3092);
	
	m6SetVV(m6, m3_1);

  printf("%s\n", m6fmt(m6));
  
  return 0;
}
