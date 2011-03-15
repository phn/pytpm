/* file: $RCSfile: j2jcal.c,v $
** rcsid: $Id: j2jcal.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: j2jcal.c,v $ - map a julian day number onto the julian proleptic calendar.
** the algorithm is from
** The Explanatory Supplement to the Astronomical Almanac (1992),
** section 12.95, equation 12.95-1, page 606.
** *******************************************************************
*/

#include "times.h"

void
j2jcal(int *y, int *m, int *d, double j)
{
    int i;
    int k;
    int l;
    int n;
    int x;	/* replaces 'j' in reference formula */

    /* remember to round the JD to the next higher civil day */
    x = (int)(j+0.5) + 1402;
    k = (x - 1) / 1461;
    l = x - (1461 * k);
    n = (l - 1) / 365 - (l / 1461);
    i = l - (365 * n) + 30;
    x = (80 * i) / 2447;
    *d = i - (2447 * x) / 80;
    i = x / 11;
    *m = x + 2 - (12 * i);
    *y = (4 * k) + n + i - 4716;

    return;
}
