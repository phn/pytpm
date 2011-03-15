/* file: $RCSfile: v6.h,v $
** rcsid: $Id: v6.h 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6.h,v $ -
**********************************************************************
*/

#ifndef V6_INCLUDE
#define V6_INCLUDE

typedef struct s_v6 {
	V3 v[2];
} V6;

/* index into the 6-vector */
#define POS	(0)
#define VEL	(1)

#define v6GetPos(v6)	(v6.v[POS])
#define v6GetVel(v6)	(v6.v[VEL])

#define v6SetPos(v6,v3)	(v6.v[POS] = (v3))
#define v6SetVel(v6,v3)	(v6.v[VEL] = (v3))

#define v6DecX(v6,x)		(v6.v[POS].v[0] -= (x))
#define v6DecY(v6,x)		(v6.v[POS].v[1] -= (x))
#define v6DecZ(v6,x)		(v6.v[POS].v[2] -= (x))
#define v6DecXDot(v6,x)		(v6.v[VEL].v[0] -= (x))
#define v6DecYDot(v6,x)		(v6.v[VEL].v[1] -= (x))
#define v6DecZDot(v6,x)		(v6.v[VEL].v[2] -= (x))
#define v6DecR(v6,x)		(v6.v[POS].v[0] -= (x))
#define v6DecAlpha(v6,x)	(v6.v[POS].v[1] -= (x))
#define v6DecDelta(v6,x)	(v6.v[POS].v[2] -= (x))
#define v6DecRDot(v6,x)		(v6.v[VEL].v[0] -= (x))
#define v6DecAlphaDot(v6,x)	(v6.v[VEL].v[1] -= (x))
#define v6DecDeltaDot(v6,x)	(v6.v[VEL].v[2] -= (x))

#define v6DivX(v6,x)		(v6.v[POS].v[0] /= (x))
#define v6DivY(v6,x)		(v6.v[POS].v[1] /= (x))
#define v6DivZ(v6,x)		(v6.v[POS].v[2] /= (x))
#define v6DivXDot(v6,x)		(v6.v[VEL].v[0] /= (x))
#define v6DivYDot(v6,x)		(v6.v[VEL].v[1] /= (x))
#define v6DivZDot(v6,x)		(v6.v[VEL].v[2] /= (x))
#define v6DivR(v6,x)		(v6.v[POS].v[0] /= (x))
#define v6DivAlpha(v6,x)	(v6.v[POS].v[1] /= (x))
#define v6DivDelta(v6,x)	(v6.v[POS].v[2] /= (x))
#define v6DivRDot(v6,x)		(v6.v[VEL].v[0] /= (x))
#define v6DivAlphaDot(v6,x)	(v6.v[VEL].v[1] /= (x))
#define v6DivDeltaDot(v6,x)	(v6.v[VEL].v[2] /= (x))

#define v6GetType(v6)		(v6.v[POS].type)
#define v6GetX(v6)		(v6.v[POS].v[0])
#define v6GetY(v6)		(v6.v[POS].v[1])
#define v6GetZ(v6)		(v6.v[POS].v[2])
#define v6GetXDot(v6)		(v6.v[VEL].v[0])
#define v6GetYDot(v6)		(v6.v[VEL].v[1])
#define v6GetZDot(v6)		(v6.v[VEL].v[2])
#define v6GetR(v6)		(v6.v[POS].v[0])
#define v6GetAlpha(v6)		(v6.v[POS].v[1])
#define v6GetDelta(v6)		(v6.v[POS].v[2])
#define v6GetRDot(v6)		(v6.v[VEL].v[0])
#define v6GetAlphaDot(v6)	(v6.v[VEL].v[1])
#define v6GetDeltaDot(v6)	(v6.v[VEL].v[2])

#define v6IncX(v6,x)		(v6.v[POS].v[0] += (x))
#define v6IncY(v6,x)		(v6.v[POS].v[1] += (x))
#define v6IncZ(v6,x)		(v6.v[POS].v[2] += (x))
#define v6IncXDot(v6,x)		(v6.v[VEL].v[0] += (x))
#define v6IncYDot(v6,x)		(v6.v[VEL].v[1] += (x))
#define v6IncZDot(v6,x)		(v6.v[VEL].v[2] += (x))
#define v6IncR(v6,x)		(v6.v[POS].v[0] += (x))
#define v6IncAlpha(v6,x)	(v6.v[POS].v[1] += (x))
#define v6IncDelta(v6,x)	(v6.v[POS].v[2] += (x))
#define v6IncRDot(v6,x)		(v6.v[VEL].v[0] += (x))
#define v6IncAlphaDot(v6,x)	(v6.v[VEL].v[1] += (x))
#define v6IncDeltaDot(v6,x)	(v6.v[VEL].v[2] += (x))

#define v6MulX(v6,x)		(v6.v[POS].v[0] *= (x))
#define v6MulY(v6,x)		(v6.v[POS].v[1] *= (x))
#define v6MulZ(v6,x)		(v6.v[POS].v[2] *= (x))
#define v6MulXDot(v6,x)		(v6.v[VEL].v[0] *= (x))
#define v6MulYDot(v6,x)		(v6.v[VEL].v[1] *= (x))
#define v6MulZDot(v6,x)		(v6.v[VEL].v[2] *= (x))
#define v6MulR(v6,x)		(v6.v[POS].v[0] *= (x))
#define v6MulAlpha(v6,x)	(v6.v[POS].v[1] *= (x))
#define v6MulDelta(v6,x)	(v6.v[POS].v[2] *= (x))
#define v6MulRDot(v6,x)		(v6.v[VEL].v[0] *= (x))
#define v6MulAlphaDot(v6,x)	(v6.v[VEL].v[1] *= (x))
#define v6MulDeltaDot(v6,x)	(v6.v[VEL].v[2] *= (x))

#define v6SetType(v6,t)		(v6.v[POS].type = v6.v[VEL].type = (t))
#define v6SetX(v6,x)		(v6.v[POS].v[0] = (x))
#define v6SetY(v6,x)		(v6.v[POS].v[1] = (x))
#define v6SetZ(v6,x)		(v6.v[POS].v[2] = (x))
#define v6SetXDot(v6,x)		(v6.v[VEL].v[0] = (x))
#define v6SetYDot(v6,x)		(v6.v[VEL].v[1] = (x))
#define v6SetZDot(v6,x)		(v6.v[VEL].v[2] = (x))
#define v6SetR(v6,x)		(v6.v[POS].v[0] = (x))
#define v6SetAlpha(v6,x)	(v6.v[POS].v[1] = (x))
#define v6SetDelta(v6,x)	(v6.v[POS].v[2] = (x))
#define v6SetRDot(v6,x)		(v6.v[VEL].v[0] = (x))
#define v6SetAlphaDot(v6,x)	(v6.v[VEL].v[1] = (x))
#define v6SetDeltaDot(v6,x)	(v6.v[VEL].v[2] = (x))

/* some astro convenience macros */

#define v6DecRA(f,x)		(v6DecAlpha(f,x))
#define v6DecPMRA(f,x)		(v6DecAlphaDot(f,x))
#define v6DecDec(f,x)		(v6DecDelta(f,x))
#define v6DecPMDec(f,x)		(v6DecDeltaDot(f,x))

#define v6DivRA(f,x)		(v6DivAlpha(f,x))
#define v6DivPMRA(f,x)		(v6DivAlphaDot(f,x))
#define v6DivDec(f,x)		(v6DivDelta(f,x))
#define v6DivPMDec(f,x)		(v6DivDeltaDot(f,x))

#define v6GetRA(f)		(v6GetAlpha(f))
#define v6GetPMRA(f)		(v6GetAlphaDot(f))
#define v6GetDec(f)		(v6GetDelta(f))
#define v6GetPMDec(f)		(v6GetDeltaDot(f))

#define v6IncRA(f,x)		(v6IncAlpha(f,x))
#define v6IncPMRA(f,x)		(v6IncAlphaDot(f,x))
#define v6IncDec(f,x)		(v6IncDelta(f,x))
#define v6IncPMDec(f,x)		(v6IncDeltaDot(f,x))

#define v6MulRA(f,x)		(v6MulAlpha(f,x))
#define v6MulPMRA(f,x)		(v6MulAlphaDot(f,x))
#define v6MulDec(f,x)		(v6MulDelta(f,x))
#define v6MulPMDec(f,x)		(v6MulDeltaDot(f,x))

#define v6SetRA(f,x)		(v6SetAlpha(f,x))
#define v6SetPMRA(f,x)		(v6SetAlphaDot(f,x))
#define v6SetDec(f,x)		(v6SetDelta(f,x))
#define v6SetPMDec(f,x)		(v6SetDeltaDot(f,x))

/* EXTERN_START */
/* EXTERN_STOP */

#endif
