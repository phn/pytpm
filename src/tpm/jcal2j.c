/* file: $RCSfile: jcal2j.c,v $
** rcsid: $Id: jcal2j.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: jcal2j.c,v $ - map a julian proleptic calendar date onto a julian day number
** the algorithm is from
** The Explanatory Supplement to the Astronomical Almanac (1992),
** section 12.95, equation 12.95-x, page 606.
** *******************************************************************
*/

#include "times.h"

double
jcal2j(int y, int m, int d)
{
    int j;

    j = 367 * y;
    j -= (7 * (y + 5001 + (m - 9) / 7)) / 4;
    j += (275 * m) / 9;
    j += d;
    j += 1729777;

    return((double)j);
}
