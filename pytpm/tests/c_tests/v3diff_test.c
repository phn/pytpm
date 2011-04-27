#include "tpm/vec.h"
#include <stdio.h>


int main() {
  /* Test v3diff for two spherical V3 */
  V3 v31, v32, v312;
  #define L 2
  double v[L][6] = {
    {1.0, 2.0, 3.0, 10.0, 0.2, -0.234},
    {-1.0, 2.0, 3.0, 1.0, -2.0, -0.234}
  };

  v31 = v3init(SPHERICAL);
  v32 = v3init(SPHERICAL);
  v312 = v3init(SPHERICAL);

  for(int i=0; i < L; i++){
    v3SetR(v31, v[i][0]);
    v3SetAlpha(v31, v[i][1]);
    v3SetDelta(v31, v[i][2]);
    v3SetR(v32, v[i][3]);
    v3SetAlpha(v32, v[i][4]);
    v3SetDelta(v32, v[i][5]);

    /* v3diff always returns Cartesian; so convert into spherical */
    v312 = v3c2s(v3diff(v32, v31));

    printf("%0.8f %0.8f %0.8f\n", v3GetR(v32), v3GetAlpha(v32), 
           v3GetDelta(v32));
    printf("%0.8f %0.8f %0.8f\n", v3GetR(v31), v3GetAlpha(v31), 
           v3GetDelta(v31));

    printf("%0.8f %0.8f %0.8f\n\n\n", v3GetR(v312), v3GetAlpha(v312), 
           v3GetDelta(v312));

  }

  return 0;
}
