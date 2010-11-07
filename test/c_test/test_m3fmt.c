#include "tpm/vec.h"
#include <stdio.h>

int main(void){
  
  M3 m3;
  
  m3 = m3I(1.0);
   
  m3SetXX(m3, 0.2345); 
	m3SetXY(m3, 0.5432);	
	m3SetXZ(m3, 0.1234);	
	m3SetYX(m3, 0.5467);	
	m3SetYY(m3, 0.4190);	
	m3SetYZ(m3, 0.9874);	
	m3SetZX(m3, 0.1225);	
	m3SetZY(m3, 0.4331);	
	m3SetZZ(m3, 0.2309);	

  printf("%s\n", m3fmt(m3));

  return 0;
}
