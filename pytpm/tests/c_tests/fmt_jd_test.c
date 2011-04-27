#include "tpm/times.h"
#include <stdio.h>

int main() {
  JD jd;

  jdSetDay(jd, 2451545.5);
  jdSetHours(jd, 0.0);
  jdSetMinutes(jd, 0.0);
  jdSetSeconds(jd, 0.0);

  printf("%s\n", fmt_jd(jd));

  jdSetDay(jd, 2456745.2456);
  jdSetHours(jd, 9.0);
  jdSetMinutes(jd, 12.3446);
  jdSetSeconds(jd, 49.99999);

  printf("%s\n", fmt_jd(jd));

  return 0;
}
