/* file: $RCSfile: j2gcal.c,v $
** rcsid: $Id: j2gcal.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: j2gcal.c,v $ - map a julian day number onto the gregorian proleptic calendar.
** the algorithm is from
** The Explanatory Supplement to the Astronomical Almanac (1992),
** section 12.92, equation 12.92-2, page 604.
** *******************************************************************
*/

#include "times.h"

void
j2gcal(int *y, int *m, int *d, double j)
{
    int i;
    int l;
    int n;
    int x;	/* replaces 'j' in reference formula */

    /* remember to round the JD to the next higher civil day */
    l = (int)(j+0.5) + 68569;
    n = (4 * l) / 146097;
    l -= ((146097 * n) + 3) / 4;
    i = (4000 * (l + 1)) / 1461001;
    l -= (1461 * i) / 4 - 31;
    x = (80 * l) / 2447;
    *d = l - (2447 * x) / 80;
    l = x / 11;
    *m = x + 2 - (12 * l);
    *y = 100 * (n - 49) + i + l;

    return;
}
