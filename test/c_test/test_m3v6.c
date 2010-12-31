#include "tpm/vec.h"
#include <stdio.h>

int main(void){
  V6 v6;
  V3 v3_1, v3_2;
  M3 m3_1;
  
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
  
  m3_1 = m3I(1.0);

  m3SetXX(m3_1,0.2345); 
	m3SetXY(m3_1,0.5432);  
	m3SetXZ(m3_1,0.1234);  
	m3SetYX(m3_1,0.5467);  
	m3SetYY(m3_1,0.4190);  
	m3SetYZ(m3_1,0.9874);  
	m3SetZX(m3_1,0.1225);  
	m3SetZY(m3_1,0.4331);  
	m3SetZZ(m3_1,0.2309);  

  v6 = m3v6(m3_1, v6);
  
  printf("X %f \tY %f \tZ %f\n XDOT %f \tYDOT %f \tZDOT %f\n",  \
         v6GetX(v6), v6GetY(v6), v6GetZ(v6), v6GetXDot(v6),
         v6GetYDot(v6), v6GetZDot(v6));
  
}
