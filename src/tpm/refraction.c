/* file: $RCSfile: refraction.c,v $
** rcsid: $Id: refraction.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: refraction.c,v $
** full refraction calculation from Exp. Supp. p. 140
** this is similar to Pat Wallace's slalib routine sla_refro().
** *******************************************************************
*/

#include "astro.h"

#undef DEBUG

/* universal gas constant */
#define R	(8314.36)

/* molecular weight of dry air */
#define MD	(28.966)

/* molecular weight of water vapor */
#define MW	(18.016)

/* exponent of temperature dependence of water vapor pressure */
#define DELTA	(18.36)

/* mean radius of the earth in meters */
#define RE	(6378120)

/* altitude of the tropopause in meters */
#define HT	(11000)

/* upper edge of the stratosphere in meters */
#define HS	(80000)

/* canonical tropospheric lapse rate of temperature in K/m */
#define ALPHA	(0.0065)

/* the refraction integrand */
#define F(r,n,dndr)	(((r) * (dndr)) / ((n) + (r) * (dndr)))

/* snell's law */
#define SNELL(r0,n0,z0,r,n)	(asin(((r0)*(n0)*sin(z0))/((r)*(n))))

/* here we define static variables that are shared between functions */
static double C1 = 0;
static double C2 = 0;
static double C3 = 0;
static double C4 = 0;
static double C5 = 0;
static double C6 = 0;
static double C7 = 0;
static double C8 = 0;
static double C9 = 0;

static double T0;	/* T at the observer */
static double Tt;	/* T in the troposphere at the tropopause */
static double dndr0;	/* dndr at the observer */
static double dndrs;	/* dndr at the stratopause */
static double dndrt;	/* dndr in the troposphere at the tropopause */
static double dndrts;	/* dndr in the stratosphere at the tropopause */
static double n0;	/* n at the observer */
static double ns;	/* n at the stratopause */
static double nt;	/* n in the troposphere at the tropopause */
static double nts;	/* n in the stratosphere at the tropopause */
static double r0;	/* r at the observer */
static double rs;	/* r at the stratopause */
static double rt;	/* r in the troposphere at the tropopause */
static double rts;	/* r in the stratosphere at the tropopause */
static double z0;	/* z at the observer */
static double zs;	/* z at the stratopause */
static double zt;	/* z in the troposphere at the tropopause */
static double zts;	/* z in the stratosphere at the tropopause */

/* this routine implements the model atmosphere */
void
atm(double r, double *n, double *dndr)
{
    double T;	/* the temperature at r */

    /* enforce some limits on r */
    if (r < r0) {
	r = r0;
    } else if (r > (RE+HS)) {
	r = (RE+HS);
    }

    if (r <= (RE+HT)) {
	/* we're in the troposphere */

	T = T0 - C1 * (r - r0);

	*n = 1 + (C6 * pow(T/T0, C3-2) - C7 * pow(T/T0,C4-2)) * (T/T0);

	*dndr = -C8 * pow(T/T0, C3-2) + C9 * pow(T/T0, C4-2);
    } else {
	/* we're in the stratosphere */

	Tt = T0 - C1 * (rt - r0);

	*n = 1 + (nt - 1) * exp(-C2 * (r - rt)/Tt);

	*dndr = -(C2 / Tt) * (nt - 1) * exp(-C2 * (r - rt)/Tt);
    }

#ifdef DEBUG
    (void)fprintf(stdout, "atm: r %.15e\n", r);
    (void)fprintf(stdout, "atm: T %.15e\n", T);
    (void)fprintf(stdout, "atm: *n %.15e\n", *n);
    (void)fprintf(stdout, "atm: *dndr %.15e\n", *dndr);
#endif

    return;
}

/* this is the function of z to be passed to the quadrature routine.
** given a value of z, we must compute
** 1. r(z) using a newton-raphson iteration of snell's law
** 2. n(r) using the 2 component model atmosphere
** 3. dndr(r) using the 2 component model atmosphere
** 4. f(r,n,dndr), the desired result
*/
#ifdef DEBUG
static int n_func = 0;
#endif

double
func(double z)
{
    double dndr;
    double f;
    double n;
    int i;
    static double r = (RE+HT);

#ifdef DEBUG
    (void)fprintf(stdout, "func: z %.15e r %.15e\n", z, r);
#endif

    for (i = 0; i < 4; i++) {
	atm(r, &n, &dndr);
#ifdef DEBUG
	(void)fprintf(stdout, "func: i %d\n", i);
	(void)fprintf(stdout, "func: r %.15e\n", r);
	(void)fprintf(stdout, "func: n %.15e\n", n);
	(void)fprintf(stdout, "func: dndr %.15e\n", dndr);
#endif
	r -= (r*n - r0*n0*sin(z0)/sin(z)) / (n + r*dndr);
#ifdef DEBUG
	(void)fprintf(stdout, "func: i %d new r %.15e\n", i, r);
#endif
    }

    f = F(r, n, dndr);
#ifdef DEBUG
    (void)fprintf(stdout, "func: f %.15e\n", f);
    n_func++;
#endif

    return(f);
}

double
refraction(double zobs, double lat, double alt, double T, double P, double rh, double lambda, double eps)
{
    double A;
    double Pw0;
    double gbar;
    double ref;		/* total refraction */
    double refs;	/* startospheric refraction */
    double reft;	/* tropospheric refraction */
    int imax = 24;

#ifdef DEBUG
    (void)fprintf(stdout, "refraction: zobs %.15e\n", zobs);
#endif

    /* compute the model coefficients */
    T0 = T;
    gbar = 9.784 * (1 - 0.0026*cos(2*lat) - 0.00000028 * alt);
    A = 287.604 + ((1.6288 + 0.0136/(lambda*lambda)) / (lambda*lambda));
    A *= (273.15e-6 / 1013.25);
    C1 = ALPHA;
    C2 = gbar * MD / R;
    C3 = C2 / C1;
    C4 = DELTA;
    Pw0 = rh * pow((T0 / 247.1), C4);
    C5 = Pw0 * (1 - MW/MD) * C3 / (C4 - C3);
    C6 = A * (P + C5) / T0;
    C7 = (A * C5 + 11.2684e-6 * Pw0) / T0;
    C8 = C1 * (C3 - 1) * C6 / T0;
    C9 = C1 * (C4 - 1) * C7 / T0;
#ifdef DEBUG
    (void)fprintf(stdout, "x_refco: Pw0 %.15e\n", Pw0);
    (void)fprintf(stdout, "x_refco: gbar %.15e\n", gbar);
    (void)fprintf(stdout, "x_refco: A %.15e\n", A);
    (void)fprintf(stdout, "x_refco: C1 %.15e\n", C1);
    (void)fprintf(stdout, "x_refco: C2 %.15e\n", C2);
    (void)fprintf(stdout, "x_refco: C3 %.15e\n", C3);
    (void)fprintf(stdout, "x_refco: C4 %.15e\n", C4);
    (void)fprintf(stdout, "x_refco: C5 %.15e\n", C5);
    (void)fprintf(stdout, "x_refco: C6 %.15e\n", C6);
    (void)fprintf(stdout, "x_refco: C7 %.15e\n", C7);
    (void)fprintf(stdout, "x_refco: C8 %.15e\n", C8);
    (void)fprintf(stdout, "x_refco: C9 %.15e\n", C9);
#endif

    /* compute the limits of integration */
    r0 = RE + alt;
    atm(r0, &n0, &dndr0);
    z0 = zobs;
#ifdef DEBUG
    (void)fprintf(stdout, "refraction: r0 %.15e\n", r0);
    (void)fprintf(stdout, "refraction: n0 %.15e\n", n0);
    (void)fprintf(stdout, "refraction: dndr0 %.15e\n", dndr0);
    (void)fprintf(stdout, "refraction: z0 %.15e\n", z0);
#endif

    rt = (RE+HT) - 0.001;
    atm(rt, &nt, &dndrt);
    zt = SNELL(r0, n0, z0, rt, nt);
#ifdef DEBUG
    (void)fprintf(stdout, "refraction: rt %.15e\n", rt);
    (void)fprintf(stdout, "refraction: nt %.15e\n", nt);
    (void)fprintf(stdout, "refraction: dndrt %.15e\n", dndrt);
    (void)fprintf(stdout, "refraction: zt %.15e\n", zt);
#endif

    rts = (RE+HT) + 0.001;
    atm(rts, &nts, &dndrts);
    zts = SNELL(r0, n0, z0, rts, nts);
#ifdef DEBUG
    (void)fprintf(stdout, "refraction: rts %.15e\n", rts);
    (void)fprintf(stdout, "refraction: nts %.15e\n", nts);
    (void)fprintf(stdout, "refraction: dndrts %.15e\n", dndrts);
    (void)fprintf(stdout, "refraction: zts %.15e\n", zts);
#endif

    rs = (RE+HS);
    atm(rs, &ns, &dndrs);
    zs = SNELL(r0, n0, z0, rs, ns);
#ifdef DEBUG
    (void)fprintf(stdout, "refraction: rs %.15e\n", rs);
    (void)fprintf(stdout, "refraction: ns %.15e\n", ns);
    (void)fprintf(stdout, "refraction: dndrs %.15e\n", dndrs);
    (void)fprintf(stdout, "refraction: zs %.15e\n", zs);
#endif

    /* evaluate the integral through the troposphere */
#ifdef DEBUG
    n_func = 0;
#endif
    reft = qromb(func, z0, zt, eps, imax);
#ifdef DEBUG
    (void)fprintf(stdout, "refraction: n_func(t) %d\n", n_func);
#endif

    /* evaluate the integral through the stratosphere */
#ifdef DEBUG
    n_func = 0;
#endif
    refs = qromb(func, zts, zs, eps, imax);
#ifdef DEBUG
    (void)fprintf(stdout, "refraction: n_func(s) %d\n", n_func);
#endif

    ref = reft + refs;

#ifdef DEBUG
    (void)fprintf(stdout, "refraction: reft %.15e\n", reft);
    (void)fprintf(stdout, "refraction: refs %.15e\n", refs);
    (void)fprintf(stdout, "refraction: ref %.15e\n", ref);
#endif

    return(ref);
}
