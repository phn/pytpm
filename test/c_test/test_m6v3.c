/* create m6 and v3; print them; print v3 from m6v3.c*/
#include "tpm/vec.h"
#include <stdio.h>

int main(void){
 V3 v3_1, v3_2;
 M6 m6;
  
 v3_1.v[0] = 1.2345;
 v3_1.v[1] = 2.3456;
 v3_1.v[2] = 3.4567;
 v3_1.type = CARTESIAN;
  
 m6 = m6Qy(1.98765432, 0.76543);
 v3_2 = m6v3(m6, v3_1);

 printf("%f %f %f\n",v3_2.v[0], v3_2.v[1], v3_2.v[2]);      

}
