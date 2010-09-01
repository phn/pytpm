/* file: $RCSfile: fk524.c,v $
** rcsid: $Id: fk524.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: fk524.c,v $
** transform from FK4 to FK5 reference frames.
** see yallop et al. (AJ,97,274).
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
#define ETERMS_ITERATE

#define E50	(0.525)
#define Edot	(1.275)
static V3 A = {CARTESIAN, {-1.62557e-6, -0.31919e-6, -0.13843e-6}};
static V3 Adot = {CARTESIAN, {1.245e-3, -1.580e-3, -0.659e-3}};

static M6 M = {
    {
    {
    {
    {
    {  9.999256794999889e-01,  1.118148284190867e-02,  4.859003870329621e-03},
    { -1.118148278993808e-02,  9.999374848980191e-01, -2.717714199112759e-05},
    { -4.859003989958792e-03, -2.715574626236038e-05,  9.999881946019697e-01}
    }
    },

    {
    {
    { -1.826121924585810e+04, -2.042075683517238e+02, -8.872901339192146e+01},
    {  2.042075684365956e+02, -1.826143479951601e+04,  4.960738018777507e-01},
    {  8.872901319665669e+01,  4.961087284511042e-01, -1.826236098729231e+04}
    }
    }
    },

    {
    {
    {
    { -7.309640594504733e-14,  3.165912442232767e-11, -5.782233482677956e-11},
    { -3.166582955112588e-11, -3.540613426475124e-13,  1.626588003924293e-12},
    {  5.783776847498632e-11, -1.133748570491210e-12,  2.809649189197363e-13}
    }
    },

    {
    {
    {  9.999256790194837e-01,  1.118169095558628e-02,  4.858623770785860e-03},
    { -1.118169094769237e-02,  9.999374825705697e-01, -2.716644949038319e-05},
    { -4.858623788960764e-03, -2.716319904536669e-05,  9.999881964489141e-01}
    }
    }
    }
    }
};

V6
fk524(V6 v)
{
    v = m6v6(M, v);

    /* restore e-terms */
#ifdef ETERMS
    {
	double m;		/* modulus of position vector */
	V3 s0;
	V3 s1, s1dot;
	V3 r0, r0dot;
	V3 r1, r1dot;

	/* cache the modulus */
	m = v6mod(v);

	/* convert the state vector back to a unit vector */
	v6GetPos(v) = v3scale(v6GetPos(v), 1/m);
	v6GetVel(v) = v3scale(v6GetVel(v), CB/(m*as2r(1)));

	/* now proceed with the standard treatment */
	r1 = v6GetPos(v);
	r1dot = v6GetVel(v);

	s1 = v3unit(r1);

	s0 = s1;
	r0 = v3sum(s1, v3diff(A, v3scale(s0, v3dot(s0, A))));
#ifdef ETERMS_ITERATE
	s0 = v3unit(r0);
	r0 = v3sum(s1, v3diff(A, v3scale(s0, v3dot(s0, A))));
#endif
	v6SetPos(v, r0);

#ifdef ETERMS_VEL
	s1dot = v3scale(r1dot, 1/v3mod(r1));
	r0dot = v3sum(s1dot, v3diff(Adot, v3scale(s0, v3dot(s0, Adot))));
	v6SetVel(v, r0dot);
#endif

	/* convert the unit vector back into a state vector */
	v6GetPos(v) = v3scale(v6GetPos(v), m);
	v6GetVel(v) = v3scale(v6GetVel(v), (m*as2r(1))/CB);
    }
#endif

    return(v);
}
