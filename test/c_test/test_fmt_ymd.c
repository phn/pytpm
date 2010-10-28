#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
    YMD ymd;
    ymd = j2ymd(2451545.0);
    ymd = ymd2ymd(ymd);
    printf("%s\n", fmt_ymd(ymd));
    ymd = j2ymd(1111111.12345);
    ymd = ymd2ymd(ymd);
    printf("%s\n", fmt_ymd(ymd));
    return 0;
}
