/* file: $RCSfile: precess_m.c,v $
** rcsid: $Id: precess_m.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: precess_m.c,v $
** compute the precession matrix for a given time span
** the pflag argument indicates which precession angles to use
** (see astro.h for definitions).
** the sflag argument indicates whether the precession is between
** inertial frames (e.g. FK5 -> FK5) or not
** (see astro.h for definitions).
** this routine returns the full 6x6 precession matrix appropriate
** for precessing proper motions along with positions.
** see yallop (AJ,97,274) for details.
** *******************************************************************
*/

#include "astro.h"

M6
precess_m(double j1, double j2, int pflag, int sflag)
{
    M6 m6;	/* the precession matrix */
    M6 qtheta;
    M6 qzee;
    M6 qzeta;

    qzeta = m6Qz(-zeta(j1, j2, pflag), -zetadot(j1, j2, pflag));
    qtheta = m6Qy(theta(j1, j2, pflag), thetadot(j1, j2, pflag));
    qzee = m6Qz(-zee(j1, j2, pflag), -zeedot(j1, j2, pflag));

    m6 = m6m6(qzee, m6m6(qtheta, qzeta));

    if (sflag != PRECESS_ROTATING) {
	/* zero out the non-inertial "P-dot" term */
	m6GetVP(m6) = m3O();
    }

    return(m6);
}
