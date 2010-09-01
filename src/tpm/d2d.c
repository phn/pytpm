/* file: $RCSfile: d2d.c,v $
** rcsid: $Id: d2d.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: d2d.c,v $ - normalize scalar degrees
** *******************************************************************
*/

#include <math.h>
#include "times.h"

double
d2d(double d)
{

    if (d <= -360.0) {
	d += ceil(d / -360.0) * 360.0;
    }
    if (d >= 360.0) {
	d -= floor(d / 360.0) * 360.0;
    }

    return(d);
}
