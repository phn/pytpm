#include "v3Functions.h"

/* Decrement components of a V3 vector by the given amount. */
void v3DecXf(V3 *const v3, double x){
  v3->v[0] -= x;
}

void v3DecYf(V3 *const v3, double y){
  v3->v[1] -= y;
}

void v3DecZf(V3 *const v3, double z){
  v3->v[2] -= z;
}

double v3GetXf(const V3 v3){
  return v3.v[0];
}

void v3SetXf(V3 *const v3, double x){
  v3->v[0] = x;
}
