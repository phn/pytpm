#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
    printf("%s\n",fmt_d(180.0));
    printf("%s\n",fmt_d(45.12345));
    return 0;
}
