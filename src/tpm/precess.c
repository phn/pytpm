/* file: $RCSfile: precess.c,v $
** rcsid: $Id: precess.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: precess.c,v $
** precess a state vector
** *******************************************************************
*/

#include "astro.h"

#undef DEBUG

V6
precess(double j1, double j2, V6 v6, int pflag)
{
    M6 pm;	/* the precession matrix */

    pm = precess_m(j1, j2, pflag, PRECESS_INERTIAL);

#ifdef DEBUG
    (void)fprintf(stdout, "precess: pm \n%s\n", m6fmt(pm));
#endif

    v6 = m6v6(pm, v6);

    return(v6);
}
