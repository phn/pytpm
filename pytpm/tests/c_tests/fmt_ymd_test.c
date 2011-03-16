#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
  YMD ymd;

  ymdSetYear(ymd, 2010);
  ymdSetMonth(ymd, 10);
  ymdSetDay(ymd, 16.789);
  ymdSetHours(ymd,15.654);
  ymdSetMinutes(ymd, 1.345);
  ymdSetSeconds(ymd, 9.45);

  ymd = ymd2ymd(ymd);
  printf("%s\n", fmt_ymd(ymd));

  ymdSetYear(ymd, -1);
  ymdSetMonth(ymd, 10);
  ymdSetDay(ymd, 1.0);
  ymdSetHours(ymd,23.9999);
  ymdSetMinutes(ymd, 54.0);
  ymdSetSeconds(ymd, 9.45);

  ymd = ymd2ymd(ymd);
  printf("%s\n", fmt_ymd(ymd));
  
  
  return 0;
}
