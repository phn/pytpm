#include "tpm/vec.h"
#include <stdio.h>

int main(void){
  V3 v3_1, v3_2;
  V6 v6;
  M3 m3_1;
  M6 m6;
  /* Create a V6 vector, using 3 V3 vectors.*/
	v3_1 = v3init(CARTESIAN);
  v3_2 = v3init(CARTESIAN);
  v6 = v6init(CARTESIAN);

  v3SetType(v3_1, CARTESIAN);
	v3SetX(v3_1, 1123.4556);
	v3SetY(v3_1, 4556.1123);
	v3SetZ(v3_1, 9876.1267);
	
  v3SetType(v3_2, CARTESIAN);
	v3SetX(v3_2, 2.3456);
	v3SetY(v3_2, 6.7891);
	v3SetZ(v3_2, 7.8912);
	
	v6SetPos(v6, v3_1);
	v6SetVel(v6, v3_2);
	
	v6SetType(v6, CARTESIAN);

  /* Create a M6 matrix, by using 4 M3 matrices.*/
  m3_1 = m3I(1.0);
      

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

  v6 = m6v6(m6, v6);

  printf("X %f \tY %f \tZ %f\n XDOT %f \tYDOT %f \tZDOT %f\n",  \
         v6GetX(v6), v6GetY(v6), v6GetZ(v6), v6GetXDot(v6),
         v6GetYDot(v6), v6GetZDot(v6));
  
}
