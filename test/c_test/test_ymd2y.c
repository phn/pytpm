#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
    YMD ymd;
    ymd.y = 2000;
    ymd.m = 10;
    ymd.dd = 12.0;
    ymd.hms.hh = 12.0;
    ymd.hms.mm = 12.0;
    ymd.hms.ss = 12.345;
    printf("%f\n", ymd2y(ymd));
    return 0;
}
