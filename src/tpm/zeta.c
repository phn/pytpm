/* file: $RCSfile: zeta.c,v $
** rcsid: $Id: zeta.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: zeta.c,v $
** FK4 and FK5 precession angles and derivatives
** the pflag argument indicates which precession angles to use
** (see astro.h for definitions).
** *******************************************************************
*/

#include "astro.h"

#undef DEBUG

double
zeta(double j1, double j2, int pflag)
{
    double T;
    double t;
    double zeta;

    switch (pflag) {
    case PRECESS_NEWCOMB:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zeta = (0.018);
	zeta *= t;
	zeta += (0.302);
	zeta *= t;
	zeta += (2304.250 + ((T-0.5) * (1.396)));
	zeta *= t;
	break;
    case PRECESS_ANDOYER:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zeta = (0.017995);
	zeta *= t;
	zeta += (0.30240 + (T * (-0.000270)));
	zeta *= t;
	zeta += (2303.5545 + (T * (1.39720 + (T * (0.000060)))));
	zeta *= t;
	break;
    case PRECESS_KINOSHITA:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zeta = (0.017996);
	zeta *= t;
	zeta += (0.30242 + (T * (-0.000269)));
	zeta *= t;
	zeta += (2303.5548 + (T * (1.39720 + (T * (0.000059)))));
	zeta *= t;
	break;
    case PRECESS_LIESKE:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zeta = (0.0180);
	zeta *= t;
	zeta += (0.3023 + ((T-0.5) * (-0.000211)));
	zeta *= t;
	zeta += (2304.253 + ((T-0.5) * (1.3972 + ((T-0.5) * (0.000125)))));
	zeta *= t;
	break;
    case PRECESS_FK5:
    default:
	T = (j1 - J2000) / CJ;
	t = (j2 - j1) / CJ;
	zeta = (0.017998);
	zeta *= t;
	zeta += (0.30188 + (T * (-0.000344)));
	zeta *= t;
	zeta += (2306.2181 + (T * (1.39656 + (T * (-0.000139)))));
	zeta *= t;
	break;
    }

#ifdef DEBUG
    (void)fprintf(stdout, "zeta(%d): %.15e\n", pflag, zeta);
#endif

    /* convert to radians */
    zeta = as2r(zeta);

    return(zeta);
}

double
zetadot(double j1, double j2, int pflag)
{
    double T;
    double f = CB;	/* conversion factor from centuries to days */
    double t;
    double zetadot;

    switch (pflag) {
    case PRECESS_NEWCOMB:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zetadot = 3 * (0.018);
	zetadot *= t;
	zetadot += 2 * (0.302);
	zetadot *= t;
	zetadot += (2304.250 + ((T-0.5) * (1.396)));
	break;
    case PRECESS_ANDOYER:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zetadot = 3 * (0.017995);
	zetadot *= t;
	zetadot += 2 * (0.30240 + (T * (-0.000270)));
	zetadot *= t;
	zetadot += (2303.5545 + (T * (1.39720 + (T * (0.000060)))));
	break;
    case PRECESS_KINOSHITA:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zetadot = 3* (0.017996);
	zetadot *= t;
	zetadot += 2 * (0.30242 + (T * (-0.000269)));
	zetadot *= t;
	zetadot += (2303.5548 + (T * (1.39720 + (T * (0.000059)))));
	break;
    case PRECESS_LIESKE:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zetadot = 3 * (0.0180);
	zetadot *= t;
	zetadot += 2 * (0.3023 + ((T-0.5) * (-0.000211)));
	zetadot *= t;
	zetadot += (2304.253 + ((T-0.5) * (1.3972 + ((T-0.5) * (0.000125)))));
	break;
    case PRECESS_FK5:
    default:
	T = (j1 - J2000) / CJ;
	t = (j2 - j1) / CJ;
	f = CJ;
	zetadot = 3 * (0.017998);
	zetadot *= t;
	zetadot += 2 * (0.30188 + (T * (-0.000344)));
	zetadot *= t;
	zetadot += (2306.2181 + (T * (1.39656 + (T * (-0.000139)))));
	break;
    }

#ifdef DEBUG
    (void)fprintf(stdout, "zetadot(%d): %.15e\n", pflag, zetadot);
#endif

    /* convert to radians per day */
    zetadot = as2r(zetadot)/f;

    return(zetadot);
}
