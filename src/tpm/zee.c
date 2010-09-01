/* file: $RCSfile: zee.c,v $
** rcsid: $Id: zee.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: zee.c,v $
** FK4 and FK5 precession angles and derivatives
** the pflag argument indicates which precession angles to use
** (see astro.h for definitions).
** *******************************************************************
*/

#include "astro.h"

#undef DEBUG

double
zee(double j1, double j2, int pflag)
{
    double T;
    double t;
    double zee;

    switch (pflag) {
    case PRECESS_NEWCOMB:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zee = (0.018);
	zee *= t;
	zee += (1.093);
	zee *= t;
	zee += (2304.250 + ((T-0.5) * (1.396)));
	zee *= t;
	break;
    case PRECESS_ANDOYER:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zee = (0.018325);
	zee *= t;
	zee += (1.09480 + (T * (0.000390)));
	zee *= t;
	zee += (2303.5545 + (T * (1.39720 + (T * (0.000060)))));
	zee *= t;
	break;
    case PRECESS_KINOSHITA:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zee = (0.018324);
	zee *= t;
	zee += (1.09478 + (T * (0.000387)));
	zee *= t;
	zee += (2303.5548 + (T * (1.39720 + (T * (0.000059)))));
	zee *= t;
	break;
    case PRECESS_LIESKE:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zee = (0.0183);
	zee *= t;
	zee += (1.0949 + ((T-0.5) * (0.00046)));
	zee *= t;
	zee += (2304.253 + ((T-0.5) * (1.3972 + ((T-0.5) * (0.000125)))));
	zee *= t;
	break;
    case PRECESS_FK5:
    default:
	T = (j1 - J2000) / CJ;
	t = (j2 - j1) / CJ;
	zee = (0.018203);
	zee *= t;
	zee += (1.09468 + (T * (0.000066)));
	zee *= t;
	zee += (2306.2181 + (T * (1.39656 + (T * (-0.000139)))));
	zee *= t;
	break;
    }

#ifdef DEBUG
    (void)fprintf(stdout, "zee(%d): %.15e\n", pflag, zee);
#endif

    /* convert to radians */
    zee = as2r(zee);

    return(zee);
}

double
zeedot(double j1, double j2, int pflag)
{
    double T;
    double f = CB;	/* conversion factor from centuries to days */
    double t;
    double zeedot;

    switch (pflag) {
    case PRECESS_NEWCOMB:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zeedot = 3 * (0.018);
	zeedot *= t;
	zeedot += 2 * (1.093);
	zeedot *= t;
	zeedot += (2304.250 + ((T-0.5) * (1.396)));
	break;
    case PRECESS_ANDOYER:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zeedot = 3 * (0.018325);
	zeedot *= t;
	zeedot += 2 * (1.09480 + (T * (0.000390)));
	zeedot *= t;
	zeedot += (2303.5545 + (T * (1.39720 + (T * (0.000060)))));
	break;
    case PRECESS_KINOSHITA:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zeedot = 3 * (0.018324);
	zeedot *= t;
	zeedot += 2 * (1.09478 + (T * (0.000387)));
	zeedot *= t;
	zeedot += (2303.5548 + (T * (1.39720 + (T * (0.000059)))));
	break;
    case PRECESS_LIESKE:
	T = (j1 - BYEAR2JD(1850)) / CB;
	t = (j2 - j1) / CB;
	zeedot = 3 * (0.0183);
	zeedot *= t;
	zeedot += 2 * (1.0949 + ((T-0.5) * (0.00046)));
	zeedot *= t;
	zeedot += (2304.253 + ((T-0.5) * (1.3972 + ((T-0.5) * (0.000125)))));
	break;
    case PRECESS_FK5:
    default:
	T = (j1 - J2000) / CJ;
	t = (j2 - j1) / CJ;
	f = CJ;
	zeedot = 3 * (0.018203);
	zeedot *= t;
	zeedot += 2 * (1.09468 + (T * (0.000066)));
	zeedot *= t;
	zeedot += (2306.2181 + (T * (1.39656 + (T * (-0.000139)))));
	break;
    }

#ifdef DEBUG
    (void)fprintf(stdout, "zeedot(%d): %.15e\n", pflag, zeedot);
#endif

    /* convert to radians per day */
    zeedot = as2r(zeedot)/f;

    return(zeedot);
}
