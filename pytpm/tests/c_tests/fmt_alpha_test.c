#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
    printf("%s\n",fmt_alpha(M_PI/3.0));
    printf("%s\n",fmt_alpha(M_PI*1.234));
    return 0;
}
