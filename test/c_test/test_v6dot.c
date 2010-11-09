#include "tpm/vec.h"
#include <stdio.h>

int main(void){

  V3 v3_1, v3_2;
  V6 v6_1, v6_2;
  double x;
  /* Create a V6 vector, using 2 V3 vectors.*/
	v3_1 = v3init(CARTESIAN);
  v3_2 = v3init(CARTESIAN);
  v6_1 = v6init(CARTESIAN);

  v3SetType(v3_1, CARTESIAN);
	v3SetX(v3_1, 1123.4556);
	v3SetY(v3_1, 4556.1123);
	v3SetZ(v3_1, 9876.1267);
	
  v3SetType(v3_2, CARTESIAN);
	v3SetX(v3_2, 2.3456);
	v3SetY(v3_2, 6.7891);
	v3SetZ(v3_2, 7.8912);
	
	v6SetPos(v6_1, v3_1);
	v6SetVel(v6_1, v3_2);
	
	v6SetType(v6_1, CARTESIAN);

  v3_1 = v3init(CARTESIAN);
  v3_2 = v3init(CARTESIAN);
  v6_2 = v6init(CARTESIAN);

  v3SetType(v3_1, CARTESIAN);
	v3SetX(v3_1, 65.234556);
	v3SetY(v3_1, 32.561123);
	v3SetZ(v3_1, 76.761267);
	
  v3SetType(v3_2, CARTESIAN);
	v3SetX(v3_2, 0.6543);
	v3SetY(v3_2, 0.1987);
	v3SetZ(v3_2, 0.2189);
	
	v6SetPos(v6_2, v3_1);
	v6SetVel(v6_2, v3_2);
	
	v6SetType(v6_2, CARTESIAN);
  
  x = v6dot(v6_1, v6_2);
  
  printf("%f\n", x);

}
