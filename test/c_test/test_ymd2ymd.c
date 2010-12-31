#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
    YMD ymd;
    ymd.y = 2000;
    ymd.m = 1;
    ymd.dd = 286.0;
    ymd.hms.hh = 12.123456;
    ymd.hms.mm = 0.0;
    ymd.hms.ss = 0.0;
    ymd = ymd2ymd(ymd);
    printf("%d %d %f %f %f %f\n",ymd.y, ymd.m, ymd.dd, ymd.hms.hh,
            ymd.hms.mm, ymd.hms.ss);
    return 0;
}
