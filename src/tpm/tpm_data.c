/* file: $RCSfile: tpm_data.c,v $
** rcsid: $Id: tpm_data.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: tpm_data.c,v $
** compute dependent tstate data
** *******************************************************************
*/

#include "astro.h"

void
tpm_data(TPM_TSTATE *p, int flags)
{
    if (flags & TPM_INIT) {
	/***************/
	/* time things */
	/***************/
	p->utc = utc_now();
	p->delta_at = delta_AT(p->utc);	/* a best guess */
	p->delta_ut = 0;

	/***********************/
	/* observer's location */
	/***********************/
	p->lon = 0;
	p->lat = 0;
	p->alt = 0;

	/****************/
	/* polar motion */
	/****************/
	p->xpole = 0;
	p->ypole = 0;

	/**************************/
	/* atmospheric conditions */
	/**************************/
	p->T = 273.15;
	p->P = 1013.25;
	p->H = 0;

	/************************/
	/* observing wavelength */
	/************************/
	p->wavelength = 0.550;

	/**********************************/
	/* variables to be computed later */
	/**********************************/
	p->tai = 0;
	p->tdt = 0;
	p->tdb = 0;

	p->obliquity = 0;
	p->nut_lon = 0;
	p->nut_obl = 0;
	p->nm = m3I(1.0);
	p->pm = m6I(1.0);

	p->ut1 = 0;
	p->gmst = 0;
	p->gast = 0;
	p->last = 0;

	p->eb = v6init(CARTESIAN);
	p->eh = v6init(CARTESIAN);
	p->obs_m = v6init(CARTESIAN);
	p->obs_t = v6init(CARTESIAN);
	p->obs_s = v6init(CARTESIAN);

	p->refa = as2r(58.3);
	p->refb = as2r(-0.067);
    }

    if (flags & TPM_REFRACTION) {
	double refa;	/* refraction A */
	double refb;	/* refraction B */
	/***************************************/
	/* compute the refraction coefficients */
	/***************************************/
	refco(p->lat, p->alt, p->T, p->P, p->H, p->wavelength, 1e-8,
	    &refa, &refb);
	p->refa = refa;
	p->refb = refb;
    }

    if (flags & TPM_SLOW) {
	double nut_lon;	/* nutation in longitude */
	double nut_obl;	/* nutation in obliquity */
	M3 nm;	/* scratch nutation matrix */

	/*******************************/
	/* compute the dynamical times */
	/*******************************/
	p->tai = p->utc + (p->delta_at/86400.0);
	p->tdt = tai2tdt(p->tai);
	p->tdb = tdt2tdb(p->tdt);

	/******************************************************/
	/* compute the slowly changing geometrical quantities */
	/******************************************************/
	p->obliquity = obliquity(p->tdt);

	nutations(p->tdt, &nut_lon, &nut_obl);
	p->nut_lon = nut_lon;
	p->nut_obl = nut_obl;

	/* re-form the nutation matrix */
	nm = m3I(1.0);
	/* rotate the mean equator into the mean ecliptic */
	nm = m3m3(m3Rx(p->obliquity), nm);
	/* do the nutation in longitude */
	nm = m3m3(m3Rz(-(p->nut_lon)), nm);
	/* rotate the ecliptic back onto the equator */
	nm = m3m3(m3Rx(-(p->obliquity+p->nut_obl)), nm);
	/* load it in */
	p->nm = nm;

	/* re-form the precession matrix */
	p->pm = precess_m(J2000, p->tdt, PRECESS_FK5, PRECESS_INERTIAL);

	/***********************/
	/* get the J2000 earth */
	/***********************/
	evp(p->tdb, &(p->eb), &(p->eh));
    }

    if (flags & TPM_FAST) {
	/*******************************/
	/* compute the dynamical times */
	/*******************************/
	p->tai = p->utc + (p->delta_at/86400.0);
	p->tdt = tai2tdt(p->tai);
	p->tdb = tdt2tdb(p->tdt);

	/********************************/
	/* compute the rotational times */
	/********************************/
	p->ut1 = p->utc + (p->delta_ut/86400);

	p->gmst = ut12gmst(p->ut1);
	p->gmst = r2r(p->gmst);

	p->gast = p->gmst + p->nut_lon * cos(p->obliquity);
	p->gast = r2r(p->gast);

	p->last = p->gast + p->lon;
	p->last = r2r(p->last);
    }

    if (flags & TPM_MEDIUM) {
	/************************************/
	/* compute the observer ephemerides */
	/************************************/

	/* get the earth-fixed state vector,
	** referred to the CIO (mean pole)
	*/
	p->obs_m = geod2geoc(p->lon, p->lat, p->alt);
	/* scale from (m,m/s) to (AU,AU/day) */
	v6DivX(p->obs_m, IAU_AU);
	v6DivY(p->obs_m, IAU_AU);
	v6DivZ(p->obs_m, IAU_AU);
	v6DivXDot(p->obs_m, (IAU_AU/86400));
	v6DivYDot(p->obs_m, (IAU_AU/86400));
	v6DivZDot(p->obs_m, (IAU_AU/86400));

	/* get the earth-fixed state vector,
	** referred to the true pole of date
	** (correct for polar motion)
	*/
	p->obs_t = p->obs_m;
	p->obs_t = m3v6(m3Ry(p->xpole), p->obs_t);
	p->obs_t = m3v6(m3Rx(p->ypole), p->obs_t);

	/* get the space-fixed state vector,
	** referred to the mean equator and equinox of J2000
	*/
	p->obs_s = p->obs_m;
	p->obs_s = m3v6(m3Rz(-p->gast), p->obs_s);
	p->obs_s = m3v6(m3inv(p->nm), p->obs_s);
	p->obs_s = m6v6(m6inv(p->pm), p->obs_s);
    }

    return;
}
