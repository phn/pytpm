#include "tpm/times.h"
#include <stdio.h>

int main(int argc, const char *argv[])
{
    printf("%s\n",fmt_delta(M_PI));
    printf("%s\n",fmt_delta(M_PI/2.0));
    printf("%s\n",fmt_delta(M_PI*1.2345));
    return 0;
}
