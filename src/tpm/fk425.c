/* file: $RCSfile: fk425.c,v $
** rcsid: $Id: fk425.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: fk425.c,v $
** transform from FK4 to FK5 reference frames.
** see yallop et al. (AJ,97,274) and the ES (1992).
** *******************************************************************

Note that yallop uses Andoyer's precession and the ES uses Kinoshita's.
this routine actually uses a variant on the standard 6x6, in that
here we use true-length vectors (AU and AU/day) instead of unit vectors
with proper motions in arcseconds/century.
This necessitates some changes compared to the normal treatment:
1. the space-motion part of the matrix must be scaled by 1/(206265*CB).
   this happens automatically because our precession angle routines
   return radians and radians/day.
2. the rotational term in the P matrix must be scaled by (206265*CB)
   this happens automatically because our precession angle routines
   return radians and radians/day.
3. the proper motions do not have to be scaled by CJ/CB, because we
   scale them to days as part of the vector setup.
4. in removing the eterms, we must save and restore the true lengths
   of r and r-dot.

** *******************************************************************
*/

#include "astro.h"

#define ETERMS
#define ETERMS_VEL

#define E50	(0.525)
#define Edot	(1.275)
static V3 A = {CARTESIAN, {-1.62557e-6, -0.31919e-6, -0.13843e-6}};
static V3 Adot = {CARTESIAN, {1.245e-3, -1.580e-3, -0.659e-3}};

static M6 M = {
    {
    {
    {
    {
    { 9.999256781650601e-01, -1.118206108957399e-02, -4.857947723285060e-03},
    { 1.118206101909165e-02,  9.999374784319468e-01, -2.717645143240717e-05},
    { 4.857947885514071e-03, -2.714743630320533e-05,  9.999881997331130e-01}
    }
    },

    {
    {
    { 1.826121923524781e+04, -2.042121648868126e+02, -8.872061776134910e+01},
    { 2.042121638286585e+02,  1.826143474812228e+04, -4.962732976077233e-01},
    { 8.872062019688346e+01, -4.958376946640886e-01,  1.826236102807574e+04}
    }
    }
    },

    {
    {
    {
    { -7.309640594504733e-14, -3.166582955102000e-11,  5.783776847498632e-11},
    {  3.165912442243355e-11, -3.540613426466852e-13, -1.133748570491623e-12},
    { -5.782233482677956e-11,  1.626588003924707e-12,  2.809649189197363e-13}
    }
    },

    {
    {
    { 9.999256776845553e-01, -1.118226924732827e-02, -4.857567522287033e-03},
    { 1.118226913276926e-02,  9.999374761044972e-01, -2.718390421541352e-05},
    { 4.857567785970310e-03, -2.713674380246095e-05,  9.999882015800575e-01}
    }
    }
    }
    }
};

V6
fk425(V6 v)
{
    /* ensure cartesian vectors */
    v = v6s2c(v);

#ifdef ETERMS
    {
	double m;		/* modulus of position vector */
	V3 u0, u0dot;
	V3 u1, u1dot;

	/* cache the modulus */
	m = v6mod(v);

	/* convert the state vector back to a unit vector */
	v6GetPos(v) = v3scale(v6GetPos(v), 1/m);
	v6GetVel(v) = v3scale(v6GetVel(v), CB/(m*as2r(1)));

	/* now proceed with the standard treatment */
	u0 = v6GetPos(v);
	u1 = v3diff(u0, v3diff(A, v3scale(u0, v3dot(u0, A))));
	v6SetPos(v, u1);

#ifdef ETERMS_VEL
	u0dot = v6GetVel(v);
	u1dot = v3diff(u0dot, v3diff(Adot, v3scale(u0, v3dot(u0, Adot))));
	v6SetVel(v, u1dot);
#endif

	/* convert the unit vector back into a state vector */
	v6GetPos(v) = v3scale(v6GetPos(v), m);
	v6GetVel(v) = v3scale(v6GetVel(v), (m*as2r(1))/CB);
    }
#endif

    v = m6v6(M, v);

    return(v);
}
