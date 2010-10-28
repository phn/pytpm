#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
    printf("%f\n", d2d(360.0));
    printf("%f\n", d2d(361.0));
    printf("%f\n", d2d(-361.0));
    return 0;
}
