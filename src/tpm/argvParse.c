/* file: $RCSfile: argvParse.c,v $
** rcsid: $Id: argvParse.c 261 2007-10-19 19:07:02Z laidler $
** Copyright Jeffrey W Percival
** *******************************************************************
** Space Astronomy Laboratory
** University of Wisconsin
** 1150 University Avenue
** Madison, WI 53706 USA
** *******************************************************************
** Do not use this software without attribution.
** Do not remove or alter any of the lines above.
** *******************************************************************
*/

/*
** *******************************************************************
** $RCSfile: argvParse.c,v $ - parse time structures out of argv lists

the "cooked" argument determines how negative signs are handled for inputs
like "-45 30 30".  in raw mode, each field keeps its own sign.  in
cooked mode, the sign of the 1st item is applied to the 2nd and 3rd as
is expected with traditional usage.  So in cooked mode, the example
above would be -45 -30 -30, while in raw mode it would be -45 30 30.

Note that in cooked mode, -45 -30 -30 will be returned as -45 30 30.

** *******************************************************************
*/

#include <stdlib.h>
#include "times.h"

int
argv2dms(DMS *dms, char *argv[], int argnum, int cooked)
{
    DMS x;
    int sign = 1;

    if (*argv[argnum+1] == '-') {
	sign = -1;
    }
    x.dd = atof(argv[++argnum]);
    x.mm = atof(argv[++argnum]);
    x.ss = atof(argv[++argnum]);

    if (cooked) {
	x.mm *= sign;
	x.ss *= sign;
    }

    *dms = x;

    return(argnum);
}

int
argv2hms(HMS *hms, char *argv[], int argnum, int cooked)
{
    int sign = 1;
    HMS x;

    if (*argv[argnum+1] == '-') {
	sign = -1;
    }
    x.hh = atof(argv[++argnum]);
    x.mm = atof(argv[++argnum]);
    x.ss = atof(argv[++argnum]);

    if (cooked) {
	x.mm *= sign;
	x.ss *= sign;
    }

    *hms = x;

    return(argnum);
}

int
argv2ymd(YMD *ymd, char *argv[], int argnum, int cooked)
{
    YMD x;

    x.y = atoi(argv[++argnum]);
    x.m = atoi(argv[++argnum]);
    x.dd = atof(argv[++argnum]);
    argnum = argv2hms(&x.hms, argv, argnum, cooked);

    *ymd = x;

    return(argnum);
}
