/* file: $RCSfile: j2dow.c,v $
** rcsid: $Id: j2dow.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: j2dow.c,v $ - map a julian day number onto the day of the week. (0 = sunday)
** the algorithm is from
** The Explanatory Supplement to the Astronomical Almanac (1992),
** section 12.91, equation 12.91-1, page 603.
** *******************************************************************
*/

#include "times.h"

int
j2dow(double j)
{
    int i;

    /* remember to round the JD to the next higher civil day */
    i = (int)(j+0.5) - 7 * (((int)(j+0.5) + 1) / 7) + 1;

    return(i);
}
