/* file: $RCSfile: h2h.c,v $
** rcsid: $Id: h2h.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: h2h.c,v $ scalar hours
** *******************************************************************
*/

#include <math.h>
#include "times.h"

double
h2h(double h)
{
    if (h < 0.0) {
	h += ceil(h / -24.0) * 24.0;
    }
    if (h >= 24.0) {
	h -= floor(h / 24.0) * 24.0;
    }

    return(h);
}
