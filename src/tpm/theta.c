/* file: $RCSfile: theta.c,v $
** rcsid: $Id: theta.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: theta.c,v $
** FK4 and FK5 precession angles and derivatives.
** the pflag argument indicates which precession angles to use
** (see astro.h for definitions).
** *******************************************************************
*/

#include "astro.h"

#undef DEBUG

double
theta(double j1, double j2, int pflag)
{
    double T;
    double t;
    double theta;

    switch (pflag) {
    case PRECESS_NEWCOMB:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	theta = (-0.042);
	theta *= t;
	theta += (-0.426);
	theta *= t;
	theta += (2004.682 + ((T-0.5) * (-0.853)));
	theta *= t;
	break;
    case PRECESS_ANDOYER:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	theta = (-0.04180);
	theta *= t;
	theta += (-0.4265 + (T * (-0.00037)));
	theta *= t;
	theta += (2005.112 + (T * (-0.8529 + (T * (-0.00037)))));
	theta *= t;
	break;
    case PRECESS_KINOSHITA:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	theta = (-0.041802);
	theta *= t;
	theta += (-0.42647 + (T * (-0.000365)));
	theta *= t;
	theta += (2005.1125 + (T * (-0.85294 + (T * (-0.000365)))));
	theta *= t;
	break;
    case PRECESS_LIESKE:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	theta = (-0.0418);
	theta *= t;
	theta += (-0.4266 + ((T-0.5) * (-0.00032)));
	theta *= t;
	theta += (2004.684 + ((T-0.5) * (-0.8532 + ((T-0.5) * (-0.000317)))));
	theta *= t;
	break;
    case PRECESS_FK5:
    default:
	T = (j1 - J2000) / CJ;
	t = (j2 - j1) / CJ;
	theta = (-0.041833);
	theta *= t;
	theta += (-0.42665 + (T * (-0.000217)));
	theta *= t;
	theta += (2004.3109 + (T * (-0.85330 + (T * (-0.000217)))));
	theta *= t;
	break;
    }

#ifdef DEBUG
    (void)fprintf(stdout, "theta(%d): %.15e\n", pflag, theta);
#endif

    /* convert to radians */
    theta = as2r(theta);

    return(theta);
}

double
thetadot(double j1, double j2, int pflag)
{
    double T;
    double f = CB;	/* conversion factor from centuries to days */
    double t;
    double thetadot;

    switch (pflag) {
    case PRECESS_NEWCOMB:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	thetadot = 3 * (-0.042);
	thetadot *= t;
	thetadot += 2 * (-0.426);
	thetadot *= t;
	thetadot += (2004.682 + ((T-0.5) * (-0.853)));
	break;
    case PRECESS_ANDOYER:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	thetadot = 3 * (-0.04180);
	thetadot *= t;
	thetadot += 2 * (-0.4265 + (T * (-0.00037)));
	thetadot *= t;
	thetadot += (2005.112 + (T * (-0.8529 + (T * (-0.00037)))));
	break;
    case PRECESS_KINOSHITA:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	thetadot = 3 * (-0.041802);
	thetadot *= t;
	thetadot += 2 * (-0.42647 + (T * (-0.000365)));
	thetadot *= t;
	thetadot += (2005.1125 + (T * (-0.85294 + (T * (-0.000365)))));
	break;
    case PRECESS_LIESKE:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	thetadot = 3 * (-0.0418);
	thetadot *= t;
	thetadot += 2 * (-0.4266 + ((T-0.5) * (-0.00032)));
	thetadot *= t;
	thetadot += (2004.684 + ((T-0.5) * (-0.8532 + ((T-0.5) * (-0.000317)))));
	break;
    case PRECESS_FK5:
    default:
	T = (j1 - J2000) / CJ;
	t = (j2 - j1) / CJ;
	f = CJ;
	thetadot = 3 * (-0.041833);
	thetadot *= t;
	thetadot += 2 * (-0.42665 + (T * (-0.000217)));
	thetadot *= t;
	thetadot += (2004.3109 + (T * (-0.85330 + (T * (-0.000217)))));
	break;
    }

#ifdef DEBUG
    (void)fprintf(stdout, "thetadot(%d): %.15e\n", pflag, thetadot);
#endif

    /* convert to radians per day */
    thetadot = as2r(thetadot)/f;

    return(thetadot);
}
