/* file: $RCSfile: evp.c,v $
** rcsid: $Id: evp.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: evp.c,v $
** compute the J2000 heliocentric and barycentric earth state vectors
** this is derived from evp.c by richard wolff at noao,
** who in turn derived his from pat wallace at starlink,
** who in turn derived his from stumpff
** (astron. astrophys. suppl. ser. 41, 1-8 (1980).
** our main modification is to dump the precessional calculations,
** and deal solely with the J2000 equinox.
**
** accuracy:
**
**	The maximum deviations from the JPL DE96 ephemeris are as follows:
**
**	barycentric velocity                  42  cm/s
**	barycentric position           0.000 046  au
**
** units:
**
**	the state vector is in units of AU and AU/day
**
** pedigree:
** 	p t wallace	starlink	march 1986
** 	r j wolff	noao		february 1988 (fortran to C)
**	j w percival	uw-sal		august,december 1993
** *******************************************************************
*/

#include "astro.h"

/* eccentricity */
#define E	(sorbel[0])

/* mean anomaly */
#define G	(forbel[0])

#define CCSEC3	(-7.757020e-08)

/* sidereal rate in longitude */
#define DCSLD	(1.990987e-07)

/* sidereal rate in mean anomaly */
#define CCSGD	(1.990969e-07)

/* some constants used in the calculation of the lunar contribution */
#define CCKM	(3.122140e-05)
#define CCMLD	(2.661699e-06)
#define CCFDI	(2.399485e-07)

/* 1 - mass(earth+moon) */
#define DC1MME	(0.99999696e0)

/* inclination(moon) */
#define CCIM	(8.978749e-2)

/* constants dcfel(k,i) of fast changing elements */
static double dcfel[8][3] = {
	{ 1.7400353e+00, 6.2833195099091e+02,  5.2796e-06} ,
	{ 6.2565836e+00, 6.2830194572674e+02, -2.6180e-06} ,
	{ 4.7199666e+00, 8.3997091449254e+03, -1.9780e-05} ,
	{ 1.9636505e-01, 8.4334662911720e+03, -5.6044e-05} ,
	{ 4.1547339e+00, 5.2993466764997e+01,  5.8845e-06} ,
	{ 4.6524223e+00, 2.1354275911213e+01,  5.6797e-06} ,
	{ 4.2620486e+00, 7.5025342197656e+00,  5.5317e-06} ,
	{ 1.4740694e+00, 3.8377331909193e+00,  5.6093e-06}
};

/* constants dceps and ccsel(k,i) of slowly changing elements */
static double dceps[3] = {
	4.093198e-01, -2.271110e-04, -2.860401e-08
};

static double ccsel[17][3] = {
	{ 1.675104e-02, -4.179579e-05, -1.260516e-07},
	{ 2.220221e-01,  2.809917e-02,  1.852532e-05},
	{ 1.589963e+00,  3.418075e-02,  1.430200e-05},
	{ 2.994089e+00,  2.590824e-02,  4.155840e-06},
	{ 8.155457e-01,  2.486352e-02,  6.836840e-06},
	{ 1.735614e+00,  1.763719e-02,  6.370440e-06},
	{ 1.968564e+00,  1.524020e-02, -2.517152e-06},
	{ 1.282417e+00,  8.703393e-03,  2.289292e-05},
	{ 2.280820e+00,  1.918010e-02,  4.484520e-06},
	{ 4.833473e-02,  1.641773e-04, -4.654200e-07},
	{ 5.589232e-02, -3.455092e-04, -7.388560e-07},
	{ 4.634443e-02, -2.658234e-05,  7.757000e-08},
	{ 8.997041e-03,  6.329728e-06, -1.939256e-09},
	{ 2.284178e-02, -9.941590e-05,  6.787400e-08},
	{ 4.350267e-02, -6.839749e-05, -2.714956e-07},
	{ 1.348204e-02,  1.091504e-05,  6.903760e-07},
	{ 3.106570e-02, -1.665665e-04, -1.590188e-07}
};

/* constants of the args of the short-period perturbations by the planets */
static double dcargs[15][2] = {
	{ 5.0974222e+00, -7.8604195454652e+02},
	{ 3.9584962e+00, -5.7533848094674e+02},
	{ 1.6338070e+00, -1.1506769618935e+03},
	{ 2.5487111e+00, -3.9302097727326e+02},
	{ 4.9255514e+00, -5.8849265665348e+02},
	{ 1.3363463e+00, -5.5076098609303e+02},
	{ 1.6072053e+00, -5.2237501616674e+02},
	{ 1.3629480e+00, -1.1790629318198e+03},
	{ 5.5657014e+00, -1.0977134971135e+03},
	{ 5.0708205e+00, -1.5774000881978e+02},
	{ 3.9318944e+00,  5.2963464780000e+01},
	{ 4.8989497e+00,  3.9809289073258e+01},
	{ 1.3097446e+00,  7.7540959633708e+01},
	{ 3.5147141e+00,  7.9618578146517e+01},
	{ 3.5413158e+00, -5.4868336758022e+02}
};

/* amplitudes ccamps(k,n) of the short-period perturbations */
static double ccamps[15][5] = {
	{ -2.279594e-5,  1.407414e-5,  8.273188e-6,  1.340565e-5, -2.490817e-7},
	{ -3.494537e-5,  2.860401e-7,  1.289448e-7,  1.627237e-5, -1.823138e-7},
	{  6.593466e-7,  1.322572e-5,  9.258695e-6, -4.674248e-7, -3.646275e-7},
	{  1.140767e-5, -2.049792e-5, -4.747930e-6, -2.638763e-6, -1.245408e-7},
	{  9.516893e-6, -2.748894e-6, -1.319381e-6, -4.549908e-6, -1.864821e-7},
	{  7.310990e-6, -1.924710e-6, -8.772849e-7, -3.334143e-6, -1.745256e-7},
	{ -2.603449e-6,  7.359472e-6,  3.168357e-6,  1.119056e-6, -1.655307e-7},
	{ -3.228859e-6,  1.308997e-7,  1.013137e-7,  2.403899e-6, -3.736225e-7},
	{  3.442177e-7,  2.671323e-6,  1.832858e-6, -2.394688e-7, -3.478444e-7},
	{  8.702406e-6, -8.421214e-6, -1.372341e-6, -1.455234e-6, -4.998479e-8},
	{ -1.488378e-6, -1.251789e-5,  5.226868e-7, -2.049301e-7,  0.0e0},
	{ -8.043059e-6, -2.991300e-6,  1.473654e-7, -3.154542e-7,  0.0e0},
	{  3.699128e-6, -3.316126e-6,  2.901257e-7,  3.407826e-7,  0.0e0},
	{  2.550120e-6, -1.241123e-6,  9.901116e-8,  2.210482e-7,  0.0e0},
	{ -6.351059e-7,  2.341650e-6,  1.061492e-6,  2.878231e-7,  0.0e0}
};

/* constants of the secular perturbations in longitude */
static double ccsec[4][3] = {
	{ 1.289600e-06, 5.550147e-01, 2.076942e+00},
	{ 3.102810e-05, 4.035027e+00, 3.525565e-01},
	{ 9.124190e-06, 9.990265e-01, 2.622706e+00},
	{ 9.793240e-07, 5.508259e+00, 1.559103e+01}
};

/* constants of the arguments of the perturbations of the motion of the moon */
static double dcargm[3][2] = {
	{ 5.1679830e+00,  8.3286911095275e+03},
	{ 5.4913150e+00, -7.2140632838100e+03},
	{ 5.9598530e+00,  1.5542754389685e+04}
};

/* amplitudes of the perturbations of the moon */
static double ccampm[3][4] = {
	{  1.097594e-01, 2.896773e-07, 5.450474e-02,  1.438491e-07},
	{ -2.223581e-02, 5.083103e-08, 1.002548e-02, -2.291823e-08},
	{  1.148966e-02, 5.658888e-08, 8.249439e-03,  4.063015e-08}
};

/* a*m*dl/dt (planets) */
static double ccpamv[4] = {
	8.326827e-11, 1.843484e-11, 1.988712e-12, 1.881276e-12
};

/* a*m (planets) */
static double ccpam[4] = {
	4.960906e-3, 2.727436e-3, 8.392311e-4, 1.556861e-3
};

void
evp(double tdb, V6 *v6b, V6 *v6h)
{
    double a;
    double d1pdro;
    double obl;		/* obliquity of the ecliptic */
    double deqcor;
    double dlocal;
    double dml = 0;
    double dpsi;
    double dr;
    double drd;
    double drld;
    double dt;
    double dxb;
    double dxbd;
    double dxh;
    double dxhd;
    double dyab;
    double dyah;
    double dyabd;
    double dyahd;
    double dyb;
    double dybd;
    double dyh;
    double dyhd;
    double dzab;
    double dzah;
    double dzabd;
    double dzahd;
    double dzb;
    double dzbd;
    double dzh;
    double dzhd;
    double f;
    double flat;
    double flatm;
    double forbel[7];
    double pertl;
    double pertld;
    double pertp;
    double pertpd;
    double pertr;
    double pertrd;
    double phi;
    double phid;
    double psid;
    double sigma;
    double ls;
    double lm;
    double lp[4];
    double sn[4];
    double sorbel[17];
    int k;
    V6 bv;	/* barycentric state vector */
    V6 hv;	/* heliocentric state vector */

    dt = (tdb - JYEAR2JD(1900)) / 36525;
#ifdef DEBUG
    (void)fprintf(stdout, "evp tdb %.15e\n", tdb);
    (void)fprintf(stdout, "evp dt %.15e\n", dt);
#endif

    /* values of all elements for the instant date */
    for (k = 0; k < 8; k++) {
    	dlocal = dcfel[k][0] + dt * (dcfel[k][1] + (dt * dcfel[k][2]));
    	if (k == 0) {
	    dml = dlocal;
    	} else {
	    forbel[k-1] = dlocal;
    	}
    }
    obl = dceps[0] + dt * (dceps[1] + (dt * dceps[2]));
    for (k = 0; k < 17; k++) {
    	sorbel[k] = ccsel[k][0] + dt * (ccsel[k][1] + (dt * ccsel[k][2]));
    }

    /* secular perturbations in longitude */
    for (k = 0; k < 4; k++) {
    	sn[k] = sin(ccsec[k][1] + dt * ccsec[k][2]);
#ifdef DEBUG
	(void)fprintf(stdout, "evp a %.15e\n",
		ccsec[k][1] + dt * ccsec[k][2]);
	(void)fprintf(stdout, "evp sn %d %.15e\n", k, sn[k]);
#endif
    }

    /* periodic perturbations of the emb (earth-moon barycentre) */
    pertl = ccsec[0][0] * sn[0]
	+ ccsec[1][0] * sn[1]
	+ (ccsec[2][0] + dt * CCSEC3) * sn[2]
	+ ccsec[3][0] * sn[3];
    pertld = 0.0;
    pertr = 0.0;
    pertrd = 0.0;
#ifdef DEBUG
    (void)fprintf(stdout, "evp pertl %.15e\n", pertl);
    (void)fprintf(stdout, "evp pertr %.15e\n", pertr);
    (void)fprintf(stdout, "evp pertld %.15e\n", pertld);
    (void)fprintf(stdout, "evp pertrd %.15e\n", pertrd);
#endif
    for (k = 0; k < 15; k++) {
    	a = dcargs[k][0] + dt * dcargs[k][1];
#ifdef DEBUG
	(void)fprintf(stdout, "evp k %d\n", k);
	(void)fprintf(stdout, "evp a %.15e\n", a);
#endif
    	pertl += ccamps[k][0] * cos(a) + ccamps[k][1] * sin(a);
    	pertr += ccamps[k][2] * cos(a) + ccamps[k][3] * sin(a);
    	if (k < 10) {
	    pertld += (ccamps[k][1]*cos(a) - ccamps[k][0]*sin(a))*ccamps[k][4];
	    pertrd += (ccamps[k][3]*cos(a) - ccamps[k][2]*sin(a))*ccamps[k][4];
	}
#ifdef DEBUG
	(void)fprintf(stdout, "evp k %d\n", k);
	(void)fprintf(stdout, "evp pertl %.15e\n", pertl);
	(void)fprintf(stdout, "evp pertr %.15e\n", pertr);
	(void)fprintf(stdout, "evp pertld %.15e\n", pertld);
	(void)fprintf(stdout, "evp pertrd %.15e\n", pertrd);
#endif
    }
#ifdef DEBUG
    (void)fprintf(stdout, "evp pertl %.15e\n", pertl);
    (void)fprintf(stdout, "evp pertr %.15e\n", pertr);
    (void)fprintf(stdout, "evp pertld %.15e\n", pertld);
    (void)fprintf(stdout, "evp pertrd %.15e\n", pertrd);
#endif

    /* elliptic part of the motion of the emb */
    phi = (2*E) * ((1 - E*E * 0.125) * sin(G) + E * 0.625 * sin(2*G)
    		+ (E*E) * 0.5416667 * sin(3*G));
    f = G + phi;
    dpsi = (1-E*E) / (1 + (E * cos(f)));
    phid = (2*E) * CCSGD * ((1 + E*E * 1.5) * cos(f) +
    				E * (1.25 - sin(f) * sin(f) * 0.5));
    psid = CCSGD * E * sin(f) / sqrt(1-E*E);

    /* perturbed heliocentric motion of the emb */
    d1pdro = 1 + pertr;
    drd = d1pdro * (psid + dpsi * pertrd);
    drld = d1pdro * dpsi * (DCSLD + phid + pertld);
    ls = dml + phi + pertl;
    dxhd = drd * cos(ls) - drld * sin(ls);
    dyhd = drd * sin(ls) + drld * cos(ls);
#ifdef DEBUG
    (void)fprintf(stdout, "evp dxhd %.15e\n", dxhd);
    (void)fprintf(stdout, "evp dyhd %.15e\n", dyhd);
#endif

    /* influence of eccentricity, evection and variation on the */
    /* geocentric motion of the moon */
    pertl = 0.0;
    pertld = 0.0;
    pertp = 0.0;
    pertpd = 0.0;
    for (k = 0; k < 3; k++) {
    	a = dcargm[k][0] + dt * dcargm[k][1];
    	pertl += ccampm[k][0] * sin(a);
    	pertld += ccampm[k][1] * cos(a);
    	pertp += ccampm[k][2] * cos(a);
    	pertpd -= ccampm[k][3] * sin(a);
    }

    /* heliocentric motion of the earth */
    lm = forbel[1] + pertl;
    sigma = CCKM / (1 + pertp);
    dxhd += sigma * ((CCMLD + pertld) * sin(lm) + (pertpd * cos(lm)));
    dyhd -= sigma * ((CCMLD + pertld) * cos(lm) - (pertpd * sin(lm)));
    dzhd  = -(sigma * CCFDI * cos(forbel[2]));
#ifdef DEBUG
    (void)fprintf(stdout, "evp dxhd %.15e\n", dxhd);
    (void)fprintf(stdout, "evp dyhd %.15e\n", dyhd);
    (void)fprintf(stdout, "evp dzhd %.15e\n", dzhd);
#endif

    /* barycentric motion of the earth */
    dxbd = dxhd * DC1MME;
    dybd = dyhd * DC1MME;
    dzbd = dzhd * DC1MME;
    for (k = 0; k < 4; k++) {
    	lp[k] = forbel[k+3] + 2 * sorbel[k+9] * sin(forbel[k+3] - sorbel[k+1]);
    	dxbd += ccpamv[k] * (sin(lp[k]) + sorbel[k+9] * sin(sorbel[k+1]));
    	dybd -= ccpamv[k] * (cos(lp[k]) + sorbel[k+9] * cos(sorbel[k+1]));
    	dzbd -= ccpamv[k] * sorbel[k+13] * cos(forbel[k+3] - sorbel[k+5]);
    }
#ifdef DEBUG
    (void)fprintf(stdout, "evp dxbd %.15e\n", dxbd);
    (void)fprintf(stdout, "evp dybd %.15e\n", dybd);
    (void)fprintf(stdout, "evp dzbd %.15e\n", dzbd);
#endif

    /* transition to mean equator of date */
    dyahd = cos(obl) * dyhd - sin(obl) * dzhd;
    dzahd = sin(obl) * dyhd + cos(obl) * dzhd;
    dyabd = cos(obl) * dybd - sin(obl) * dzbd;
    dzabd = sin(obl) * dybd + cos(obl) * dzbd;
#ifdef DEBUG
    (void)fprintf(stdout, "evp dyahd %.15e\n", dyahd);
    (void)fprintf(stdout, "evp dzahd %.15e\n", dzahd);
    (void)fprintf(stdout, "evp dyabd %.15e\n", dyabd);
    (void)fprintf(stdout, "evp dzabd %.15e\n", dzabd);
#endif

    /* heliocentric coordinates of the earth */
    dr = dpsi * d1pdro;
    flatm = CCIM * sin(forbel[2]);
    dxh = dr * cos(ls) - (sigma * cos(flatm) * cos(lm));
    dyh = dr * sin(ls) - (sigma * cos(flatm) * sin(lm));
    dzh = -(sigma * sin(flatm));
#ifdef DEBUG
    (void)fprintf(stdout, "evp dxh %.15e\n", dxh);
    (void)fprintf(stdout, "evp dyh %.15e\n", dyh);
    (void)fprintf(stdout, "evp dzh %.15e\n", dzh);
#endif

    /* barycentric coordinates of the earth */
    dxb = dxh * DC1MME;
    dyb = dyh * DC1MME;
    dzb = dzh * DC1MME;
    for (k = 0; k < 4; k++) {
    	flat = sorbel[k+13] * sin(forbel[k+3] - sorbel[k+5]);
    	a = ccpam[k] * (1 - sorbel[k+9] * cos(forbel[k+3] - sorbel[k+1]));
    	dxb -= a * cos(flat) * cos(lp[k]);
    	dyb -= a * cos(flat) * sin(lp[k]);
    	dzb -= a * sin(flat);
    }
#ifdef DEBUG
    (void)fprintf(stdout, "evp dxb %.15e\n", dxb);
    (void)fprintf(stdout, "evp dyb %.15e\n", dyb);
    (void)fprintf(stdout, "evp dzb %.15e\n", dzb);
#endif

    /* transition to mean equator of date */
    dyah = cos(obl) * dyh - sin(obl) * dzh;
    dzah = sin(obl) * dyh + cos(obl) * dzh;
    dyab = cos(obl) * dyb - sin(obl) * dzb;
    dzab = sin(obl) * dyb + cos(obl) * dzb;
#ifdef DEBUG
    (void)fprintf(stdout, "evp dyah %.15e\n", dyah);
    (void)fprintf(stdout, "evp dzah %.15e\n", dzah);
    (void)fprintf(stdout, "evp dyab %.15e\n", dyab);
    (void)fprintf(stdout, "evp dzab %.15e\n", dzab);
#endif

    /* copy result components into vectors, correcting for FK4 equinox */
    deqcor = as2r(0.525 + 1.275 * (tdb - B1950)/36525);
#ifdef DEBUG
    (void)fprintf(stdout, "evp deqcor %.15e\n", deqcor);
#endif

    hv = v6init(CARTESIAN);
    v6SetX(hv, dxh - deqcor * dyah);
    v6SetY(hv, dyah + deqcor * dxh);
    v6SetZ(hv, dzah);
    v6SetXDot(hv, dxhd - deqcor * dyahd);
    v6SetYDot(hv, dyahd + deqcor * dxhd);
    v6SetZDot(hv, dzahd);

    bv = v6init(CARTESIAN);
    v6SetX(bv, dxb - deqcor * dyab);
    v6SetY(bv, dyab + deqcor * dxb);
    v6SetZ(bv, dzab);
    v6SetXDot(bv, dxbd - deqcor * dyabd);
    v6SetYDot(bv, dyabd + deqcor * dxbd);
    v6SetZDot(bv, dzabd);

#ifdef DEBUG
    (void)fprintf(stdout, "evp hv pos %.15e %.15e %.15e\n",
	v6GetX(hv), v6GetY(hv), v6GetZ(hv));
    (void)fprintf(stdout, "evp hv vel %.15e %.15e %.15e\n",
	v6GetXDot(hv), v6GetYDot(hv), v6GetZDot(hv));
    (void)fprintf(stdout, "evp bv pos %.15e %.15e %.15e\n",
	v6GetX(bv), v6GetY(bv), v6GetZ(bv));
    (void)fprintf(stdout, "evp bv vel %.15e %.15e %.15e\n",
	v6GetXDot(bv), v6GetYDot(bv), v6GetZDot(bv));
#endif

    /* scale from (AU,AU/s) to (AU,AU/day) */
    v6MulXDot(hv, 86400.0);
    v6MulYDot(hv, 86400.0);
    v6MulZDot(hv, 86400.0);
    v6MulXDot(bv, 86400.0);
    v6MulYDot(bv, 86400.0);
    v6MulZDot(bv, 86400.0);

    /* precess to the mean equator and equinox of J2000 */
    hv = precess(tdb, J2000, hv, PRECESS_FK5);
    bv = precess(tdb, J2000, bv, PRECESS_FK5);

    *v6b = bv;
    *v6h = hv;

    return;
}
