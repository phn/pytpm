/* file: $RCSfile: tpm.c,v $
** rcsid: $Id: tpm_main.c 261 2007-10-19 19:07:02Z laidler $
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
** ******************************************************************
** $RCSfile: tpm.c,v $
** front end for the mighty TPM
** ******************************************************************
*/

#include <stdlib.h>
#include <string.h>
#include "astro.h"

int
main(int argc, char *argv[])
{
    DMS dms;	/* scratch */
    HMS hms;	/* scratch */
    TPM_TSTATE tstate;
    V6 pvec[N_TPM_STATES];
    V6 v6;
    YMD ymd;	/* scratch */
    char *argptr;
    double dt = 60;	/* time step in minutes */
    double epoch = J2000;
    double equinox = J2000;
    double utc1, utc2;	/* time range in JD */
    double x0 = 0;	/* longitudinal angle */
    double x1, y1;	/* the answer */
    double y0 = 0;	/* latitudinal angle */
    int argnum;
    int debug = 0;
    int i;
    int s1 = TPM_S06;	/* heliocentric mean J2000 FK5 */
    int s2 = TPM_S19;	/* topocentric observed az/el */
    int verbose = 0;
    size_t arglen;

    utc2 = utc1 = utc_now();
    ymd = j2ymd(utc1);

    /******************************/
    /* initialize the tstate data */
    /******************************/
    tpm_data(&tstate, TPM_INIT);
    /* WIYN observatory */
    tstate.lon = d2r(-111.598333);
    tstate.lat = d2r(31.956389);
    tstate.alt = 2093.093;
    /* change DUT, polar motion if needed */

    for (argnum = 1; argnum < argc; argnum++) {
	argptr = argv[argnum];
	if (*argptr == '-') argptr++;
	arglen = strlen(argptr);

	if (strcmp(argptr, "help") == 0) {
	    (void)fprintf(stdout, "Usage: %s\n", argv[0]);
	    (void)fprintf(stdout, "\t-verbose\n");
	    (void)fprintf(stdout, "\t-lon [%s]\n", fmt_h(r2h(tstate.lon)));
	    (void)fprintf(stdout, "\t-lat [%s]\n", fmt_delta(tstate.lat));
	    (void)fprintf(stdout, "\t-alt (altitude in m above MSL) [%g]\n",
		tstate.alt);
	    (void)fprintf(stdout, "\n");
	    (void)fprintf(stdout, "\t-equinox yyyy [%g]\n", JD2JYEAR(equinox));
	    (void)fprintf(stdout, "\t-epoch yyyy [%g]\n", JD2JYEAR(epoch));
	    (void)fprintf(stdout, "\n");
	    (void)fprintf(stdout, "\t-from [%s]\n", fmt_ymd_raw(j2ymd(utc1)));
	    (void)fprintf(stdout, "\t-to [%s]\n", fmt_ymd_raw(j2ymd(utc2)));
	    (void)fprintf(stdout, "\t-dt [%g] (time step in minutes)\n", dt);
	    (void)fprintf(stdout, "\t-utc [%s] (at this time only)\n",
		fmt_ymd_raw(j2ymd(utc1)));
	    (void)fprintf(stdout, "\n");
	    (void)fprintf(stdout, "\t-x [%s] (target longitudinal angle)\n",
		fmt_d(x0));
	    (void)fprintf(stdout, "\t-y [%s] (target latitudinal angle)\n",
		fmt_d(y0));
	    (void)fprintf(stdout, "\t-s1 [%d] (starting state, see below)\n",
		s1);
	    (void)fprintf(stdout, "\t-s2 [%d] (ending state, see below)\n",
		s2);
	    (void)fprintf(stdout, "\n");
	    (void)fprintf(stdout, "wavelength: %f microns\n", tstate.wavelength);
	    (void)fprintf(stdout, "\tstates:\n");
	    for (i = 0; i < N_TPM_STATES; i++) {
		(void)fprintf(stdout, "state %2d: %s\n", i, tpm_state(i));
	    }

	    return(0);

	} else if (strncmp(argptr, "verbose", arglen) == 0) {
	    verbose++;
	} else if (strncmp(argptr, "debug", arglen) == 0) {
	    debug++;

	} else if (strcmp(argptr, "lon") == 0) {
	    argnum = argv2hms(&hms, argv, argnum, 1);
	    tstate.lon = hms2r(hms);
	} else if (strcmp(argptr, "lat") == 0) {
	    argnum = argv2dms(&dms, argv, argnum, 1);
	    tstate.lat = dms2r(dms);
	} else if (strcmp(argptr, "alt") == 0) {
	    tstate.alt = atof(argv[++argnum]);

	} else if (strcmp(argptr, "equinox") == 0) {
	    equinox = atof(argv[++argnum]);
	    equinox = JYEAR2JD(equinox);
	} else if (strcmp(argptr, "epoch") == 0) {
	    epoch = atof(argv[++argnum]);
	    epoch = JYEAR2JD(epoch);

	} else if (strcmp(argptr, "from") == 0) {
	    argnum = argv2ymd(&ymd, argv, argnum, 1);
	    utc1 = ymd2j(ymd);
	} else if (strcmp(argptr, "to") == 0) {
	    argnum = argv2ymd(&ymd, argv, argnum, 1);
	    utc2 = ymd2j(ymd);
	} else if (strcmp(argptr, "dt") == 0) {
	    dt = atof(argv[++argnum]);
	} else if (strcmp(argptr, "utc") == 0) {
	    argnum = argv2ymd(&ymd, argv, argnum, 1);
	    utc1 = utc2 = ymd2j(ymd);
	    dt = 1;

	} else if (strcmp(argptr, "x") == 0) {
	    argnum = argv2hms(&hms, argv, argnum, 1);
	    x0 = hms2r(hms);
	} else if (strcmp(argptr, "y") == 0) {
	    argnum = argv2dms(&dms, argv, argnum, 1);
	    y0 = dms2r(dms);
	} else if (strcmp(argptr, "s1") == 0) {
	    s1 = atoi(argv[++argnum]);
	} else if (strcmp(argptr, "s2") == 0) {
	    s2 = atoi(argv[++argnum]);

	} else if (strncmp(argptr, "wavelength", arglen) == 0) {
	    tstate.wavelength = atof(argv[++argnum]);

	} else {
	    (void)fprintf(stderr, "%s: bad arg(%s)\n", argv[0], argptr);
	    return(1);
	}
    }

    if (verbose) {
	(void)fprintf(stdout, "lon %s\n", fmt_hms(r2hms(tstate.lon)));
	(void)fprintf(stdout, "lat %s\n", fmt_dms(r2dms(tstate.lat)));
	(void)fprintf(stdout, "alt %gm\n", tstate.alt);
	(void)fprintf(stdout, "\n");
	(void)fprintf(stdout, "equinox %g\n", JD2JYEAR(equinox));
	(void)fprintf(stdout, "epoch %g\n", JD2JYEAR(epoch));
	(void)fprintf(stdout, "\n");
	(void)fprintf(stdout, "from %s\n", fmt_ymd(j2ymd(utc1)));
	(void)fprintf(stdout, "to %s\n", fmt_ymd(j2ymd(utc2)));
	(void)fprintf(stdout, "dt %gm\n", dt);
	(void)fprintf(stdout, "\n");
	(void)fprintf(stdout, "x %s\n", fmt_alpha(x0));
	(void)fprintf(stdout, "y %s\n", fmt_delta(y0));
	(void)fprintf(stdout, "s1 %d (%s)\n", s1, tpm_state(s1));
	(void)fprintf(stdout, "s2 %d (%s)\n", s2, tpm_state(s2));
	(void)fprintf(stdout, "\n");
	(void)fprintf(stdout, "wavelength %f microns\n", tstate.wavelength);
    }

    /* these are here to force them into the tpm distribution */
    (void)j2y(0.0);
    (void)j2ymd(0.0);
    (void)r2dms(0.0);
    (void)r2hms(0.0);
    (void)dms2r(dms);
    (void)hms2r(hms);
    (void)dms2dms(dms);
    (void)hms2hms(hms);
    (void)ymd2ymd(ymd);
    if (verbose && debug) {
	(void)fprintf(stdout, "dms: %s\n", fmt_dms(dms));
	(void)fprintf(stdout, "hms: %s\n", fmt_hms(hms));
	(void)fprintf(stdout, "ymd: %s\n", fmt_ymd(ymd));
    }

    for (tstate.utc = utc1;  tstate.utc <= utc2; tstate.utc += dt/1440) {

	/*************************/
	/* set up the state data */
	/*************************/
	tpm_data(&tstate, TPM_ALL);

	if (verbose & debug) {
	    (void)fprintf(stdout, "nut_obl: %f\"\n", r2as(tstate.nut_obl));
	    (void)fprintf(stdout, "nut_lon: %f\"\n", r2as(tstate.nut_lon));
	    (void)fprintf(stdout, "delta_at: %d\n", tstate.delta_at);
	    (void)fprintf(stdout, "delta_ut: %f\n", tstate.delta_ut);
	    (void)fprintf(stdout, "lon: %f\n", tstate.lon);
	    (void)fprintf(stdout, "lat: %f\n", tstate.lat);
	    (void)fprintf(stdout, "utc: %f\n", tstate.utc);
	    (void)fprintf(stdout, "tai: %f\n", tstate.tai);
	    (void)fprintf(stdout, "tdt: %f\n", tstate.tdt);
	    (void)fprintf(stdout, "tdb: %f\n", tstate.tdb);
	    (void)fprintf(stdout, "ut1: %f\n", tstate.ut1);
	    (void)fprintf(stdout, "gmst: %f\n", tstate.gmst);
	    (void)fprintf(stdout, "gast: %f\n", tstate.gast);
	    (void)fprintf(stdout, "last: %f\n", tstate.last);
	    (void)fprintf(stdout, "gmst: %s\n", fmt_h(r2h(tstate.gmst)));
	    (void)fprintf(stdout, "gast: %s\n", fmt_h(r2h(tstate.gast)));
	    (void)fprintf(stdout, "last: %s\n", fmt_h(r2h(tstate.last)));
	}

	/******************************/
	/* set up the target position */
	/******************************/
	v6 = v6init(SPHERICAL);
	v6SetR(v6, 1e9);
	v6SetAlpha(v6, x0);
	v6SetDelta(v6, y0);

	/******************/
	/* invoke the TPM */
	/******************/
	pvec[s1] = v6s2c(v6);
	(void)tpm(pvec, s1, s2, epoch, equinox, &tstate);
	v6 = v6c2s(pvec[s2]);

	/**********************/
	/* extract the answer */
	/**********************/
	x1 = v6GetAlpha(v6);
	y1 = v6GetDelta(v6);

	(void)fprintf(stdout, "%f %s %s\n", tstate.utc, fmt_alpha(x1), fmt_delta(y1));
    }

    return(0);
}
