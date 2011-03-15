/* file: $RCSfile: fmt_delta.c,v $
** rcsid: $Id: fmt_delta.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: fmt_delta.c,v $ - format a scalar angle as angle from -90 to 90 degrees
** *******************************************************************
*/

#include "times.h"

char *
fmt_delta(double delta)
{
    DMS dms;

    if (delta <= -M_PI) {
	delta += ceil(delta / (-2*M_PI)) * 2*M_PI;
    }

    if (delta > M_PI) {
	delta -= floor(delta / (2*M_PI)) * 2*M_PI;
    }

    if (delta > M_PI/2) {
	delta = M_PI - delta;
    }

    if (delta < -M_PI/2) {
	delta = -M_PI - delta;
    }

#ifdef DEBUG
    (void)fprintf(stdout, "fmt_delta: delta = %g\n", delta);
#endif

    dms = r2dms(delta);

#ifdef DEBUG
    (void)fprintf(stdout, "fmt_delta: dms.dd = %g\n", dmsGetDegrees(dms));
    (void)fprintf(stdout, "fmt_delta: dms.mm = %g\n", dmsGetMinutes(dms));
    (void)fprintf(stdout, "fmt_delta: dms.ss = %g\n", dmsGetSeconds(dms));
#endif

    return(fmt_dms(dms));
}
