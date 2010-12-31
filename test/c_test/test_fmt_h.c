#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
    printf("%s\n", fmt_h(12.0));
    printf("%s\n", fmt_h(36.12345));
    return 0;
}
