#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
    YMD ymd;
    ymd = j2ymd(2451545.0);
    printf("%s\n", fmt_ymd_raw(ymd));
    ymd = j2ymd(1111111.12345);
    printf("%s\n", fmt_ymd_raw(ymd));
    return 0;
}
