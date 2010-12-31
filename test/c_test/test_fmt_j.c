#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
    printf("%s\n", fmt_j(2451545.0));
    printf("%s\n", fmt_j(1111111.1234));
    return 0;
}
