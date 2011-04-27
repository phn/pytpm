#include "tpm/vec.h"
#include <stdio.h>

int main(){

  V3 v3_1, v3_2;
  V6 v6, v6s;
  /* Create a V6 vector, using 2 V3 vectors.*/
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

  v6s = v6c2s(v6);
  
  printf("X %f \tY %f \tZ %f \nXDOT %f \tYDOT %f \tZDOT %f\n",  \
         v6GetX(v6), v6GetY(v6), v6GetZ(v6), v6GetXDot(v6),
         v6GetYDot(v6), v6GetZDot(v6));
  printf("R %.8f \tAlpha %.8f \tDelta %.8f \nRDOT %.8f \tAlphaDOT %.8f \tDeltaDOT %.8f\n",  \
         v6GetR(v6s), v6GetAlpha(v6s), v6GetDelta(v6s), v6GetRDot(v6s),
         v6GetAlphaDot(v6s), v6GetDeltaDot(v6s));


  return 0;
}
