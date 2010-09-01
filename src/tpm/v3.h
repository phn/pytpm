/* file: $RCSfile: v3.h,v $
** rcsid: $Id: v3.h 261 2007-10-19 19:07:02Z laidler $
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
**********************************************************************
** $RCSfile: v3.h,v $ -
**********************************************************************
*/

#ifndef V3_INCLUDE
#define V3_INCLUDE

typedef struct s_v3 {
	int type;	/* vector type, cartesian or spherical */
	double v[3];
} V3;

#define v3DecX(v3,x)		(v3.v[0] -= (x))
#define v3DecY(v3,x)		(v3.v[1] -= (x))
#define v3DecZ(v3,x)		(v3.v[2] -= (x))
#define v3DecR(v3,x)		(v3.v[0] -= (x))
#define v3DecAlpha(v3,x)	(v3.v[1] -= (x))
#define v3DecDelta(v3,x)	(v3.v[2] -= (x))

#define v3DivX(v3,x)		(v3.v[0] /= (x))
#define v3DivY(v3,x)		(v3.v[1] /= (x))
#define v3DivZ(v3,x)		(v3.v[2] /= (x))
#define v3DivR(v3,x)		(v3.v[0] /= (x))
#define v3DivAlpha(v3,x)	(v3.v[1] /= (x))
#define v3DivDelta(v3,x)	(v3.v[2] /= (x))

#define v3GetType(v3)		(v3.type)
#define v3GetX(v3)		(v3.v[0])
#define v3GetY(v3)		(v3.v[1])
#define v3GetZ(v3)		(v3.v[2])
#define v3GetR(v3)		(v3.v[0])
#define v3GetAlpha(v3)		(v3.v[1])
#define v3GetDelta(v3)		(v3.v[2])

#define v3IncX(v3,x)		(v3.v[0] += (x))
#define v3IncY(v3,x)		(v3.v[1] += (x))
#define v3IncZ(v3,x)		(v3.v[2] += (x))
#define v3IncR(v3,x)		(v3.v[0] += (x))
#define v3IncAlpha(v3,x)	(v3.v[1] += (x))
#define v3IncDelta(v3,x)	(v3.v[2] += (x))

#define v3MulX(v3,x)		(v3.v[0] *= (x))
#define v3MulY(v3,x)		(v3.v[1] *= (x))
#define v3MulZ(v3,x)		(v3.v[2] *= (x))
#define v3MulR(v3,x)		(v3.v[0] *= (x))
#define v3MulAlpha(v3,x)	(v3.v[1] *= (x))
#define v3MulDelta(v3,x)	(v3.v[2] *= (x))

#define v3SetType(v3,x)		(v3.type = (x))
#define v3SetX(v3,x)		(v3.v[0] = (x))
#define v3SetY(v3,x)		(v3.v[1] = (x))
#define v3SetZ(v3,x)		(v3.v[2] = (x))
#define v3SetR(v3,x)		(v3.v[0] = (x))
#define v3SetAlpha(v3,x)	(v3.v[1] = (x))
#define v3SetDelta(v3,x)	(v3.v[2] = (x))

/* some astro convenience macros */

#define v3DecRA(f,x)		(v3DecAlpha(f,x))
#define v3DecDec(f,x)		(v3DecDelta(f,x))

#define v3DivRA(f,x)		(v3DivAlpha(f,x))
#define v3DivDec(f,x)		(v3DivDelta(f,x))

#define v3GetRA(f)		(v3GetAlpha(f))
#define v3GetDec(f)		(v3GetDelta(f))

#define v3IncRA(f,x)		(v3IncAlpha(f,x))
#define v3IncDec(f,x)		(v3IncDelta(f,x))

#define v3MulRA(f,x)		(v3MulAlpha(f,x))
#define v3MulDec(f,x)		(v3MulDelta(f,x))

#define v3SetRA(f,x)		(v3SetAlpha(f,x))
#define v3SetDec(f,x)		(v3SetDelta(f,x))

/* EXTERN_START */
/* EXTERN_STOP */

#endif
