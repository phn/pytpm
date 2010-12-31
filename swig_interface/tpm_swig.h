/* file: $RCSfile: tpm.h,v $
** rcsid: $Id: tpm.h 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: tpm.h,v $ - telescope pointing machine header file
** *******************************************************************
*/

#ifndef TPM_H
#define TPM_H

/* the state names */
#define TPM_S00	(0)
#define TPM_S01	(1)
#define TPM_S02	(2)
#define TPM_S03	(3)
#define TPM_S04	(4)
#define TPM_S05	(5)
#define TPM_S06	(6)
#define TPM_S07	(7)
#define TPM_S08	(8)
#define TPM_S09	(9)
#define TPM_S10	(10)
#define TPM_S11	(11)
#define TPM_S12	(12)
#define TPM_S13	(13)
#define TPM_S14	(14)
#define TPM_S15	(15)
#define TPM_S16	(16)
#define TPM_S17	(17)
#define TPM_S18	(18)
#define TPM_S19	(19)
#define TPM_S20	(20)
#define TPM_S21	(21)

#define N_TPM_STATES	(22)

/* the transition names */
#define TPM_T00	(0)
#define TPM_T01	(1)
#define TPM_T02	(2)
#define TPM_T03	(3)
#define TPM_T04	(4)
#define TPM_T05	(5)
#define TPM_T06	(6)
#define TPM_T07	(7)
#define TPM_T08	(8)
#define TPM_T09	(9)
#define TPM_T10	(10)
#define TPM_T11	(11)
#define TPM_T12	(12)
#define TPM_T13	(13)
#define TPM_T14	(14)
#define TPM_T15	(15)

#define N_TPM_TRANS	(16)

/* this describes a target */
typedef struct s_target {
	char name[BUFSIZ];
	int state;	/* pointing machine state (fk4, galactic, etc) */
	double epoch;		/* JD */
	double equinox;		/* JD */
	double position[2];	/* radians */
	double offset[2];	/* radians */
	double motion[2];	/* radians/day */
	double parallax;	/* in arcsec */
	double speed;		/* in AU/day */
} TPM_TARGET;

/* define some target states */
#define TARGET_FK4		(TPM_S01)
#define TARGET_FK5		(TPM_S02)
#define TARGET_ECL		(TPM_S03)
#define TARGET_GAL		(TPM_S04)
#define TARGET_APP_HADEC	(TPM_S17)
#define TARGET_OBS_HADEC	(TPM_S20)
#define TARGET_APP_AZEL		(TPM_S18)
#define TARGET_OBS_AZEL		(TPM_S19)
#define TARGET_OBS_WHAM		(TPM_S21)

/* used by WIYN, do not delete */
#define TARGET_HADEC	(TPM_S17)
#define TARGET_TOP_AZEL	(TPM_S18)

/* this describes the boresight */
typedef struct s_boresight {
	double epoch;		/* JD */
	double position[2];	/* radians */
	double offset[2];	/* radians */
	double motion[2];	/* radians/day */
} TPM_BORESIGHT;

/* telescope state */
typedef struct s_tstate {
	/*************************/
	/* independent variables */
	/*************************/
	double utc;		/* coordinated universal time, in JD */
	int delta_at;		/* utc + delta_at = tai */
	double delta_ut;	/* utc + delta_ut = ut1 */
	double lon;		/* east longitude in radians */
	double lat;		/* latitude in radians */
	double alt;		/* altitude above geoid in meters */
	double xpole;		/* polar motion in radians */
	double ypole;		/* polar motion in radians */
	double T;		/* ambient temperature in Kelvins */
	double P;		/* ambient pressure in millibars */
	double H;		/* ambient humidity (0-1) */
	double wavelength;	/* observing wavelength in microns */

	/*****************************/
	/* dependent dynamical times */
	/*****************************/
	double tai;		/* international atomic time */
	double tdt;		/* terrestrial dynamical time */
	double tdb;		/* barycentric dynamical time */

	/************************************/
	/* dependent geometrical quantities */
	/************************************/
	double obliquity;	/* the obliquity of the ecliptic */
	double nut_lon;		/* the nutation in longitude */
	double nut_obl;		/* the nutation in the obliquity */
	struct s_m3 nm;		/* the nutation matrix for now */
	struct s_m6 pm;		/* the precession matrix from J2000 to now */

	/******************************/
	/* dependent rotational times */
	/******************************/
	double ut1;		/* universal time */
	double gmst;		/* greenwich mean sidereal time */
	double gast;		/* greenwich apparent sidereal time */
	double last;		/* local apparent sidereal time */

	/************************/
	/* observer ephemerides */
	/************************/
	struct s_v6 eb;		/* barycentric earth state vector */
	struct s_v6 eh;		/* heliocentric earth state vector */
	struct s_v6 obs_m;	/* geocentric earth-fixed state vector */
	struct s_v6 obs_t;	/* geocentric earth-fixed state vector */
	struct s_v6 obs_s;	/* geocentric space-fixed state vector */

	/*********************************/
	/* dependent physical quantities */
	/*********************************/
	double refa;		/* refraction coefficient */
	double refb;		/* refraction coefficient */
} TPM_TSTATE;

/* define the pm_data flags */
#define TPM_INIT	(0x01)
#define TPM_FAST	(0x02)
#define TPM_MEDIUM	(0x04)
#define TPM_SLOW	(0x08)
#define TPM_REFRACTION	(0x10)
#define TPM_ALL		(TPM_FAST|TPM_MEDIUM|TPM_SLOW|TPM_REFRACTION)

/* a pointing machine cell */
typedef struct s_pmcell {
	int ptrans;	/* the next transition */
	int pstate;	/* the resulting state */
} TPM_PMCELL;

/* EXTERN_START */
/* EXTERN_STOP */

#endif
