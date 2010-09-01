/* file: $RCSfile: fmt_alpha.c,v $
** rcsid: $Id: fmt_alpha.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: fmt_alpha.c,v $ - format a scalar angle as time from 0 to 24 hours
** *******************************************************************
*/

#include "times.h"

char *
fmt_alpha(double alpha)
{
    HMS hms;

    if (alpha < 0.0) {
	alpha += ceil(alpha / (-2*M_PI)) * 2*M_PI;
    }

    if (alpha >= 2*M_PI) {
	alpha -= floor(alpha / (2*M_PI)) * 2*M_PI;
    }

    hms = r2hms(alpha);

    return(fmt_hms(hms));
}
