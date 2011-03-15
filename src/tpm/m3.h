/* file: $RCSfile: m3.h,v $
** rcsid: $Id: m3.h 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3.h,v $ -
**********************************************************************
*/

#ifndef M3_INCLUDE
#define M3_INCLUDE

typedef struct s_m3 {
	double m[3][3];
} M3;

#define m3DecXX(m3,x)	(m3.m[0][0] -= (x))
#define m3DecXY(m3,x)	(m3.m[0][1] -= (x))
#define m3DecXZ(m3,x)	(m3.m[0][2] -= (x))
#define m3DecYX(m3,x)	(m3.m[1][0] -= (x))
#define m3DecYY(m3,x)	(m3.m[1][1] -= (x))
#define m3DecYZ(m3,x)	(m3.m[1][2] -= (x))
#define m3DecZX(m3,x)	(m3.m[2][0] -= (x))
#define m3DecZY(m3,x)	(m3.m[2][1] -= (x))
#define m3DecZZ(m3,x)	(m3.m[2][2] -= (x))

#define m3DivXX(m3,x)	(m3.m[0][0] /= (x))
#define m3DivXY(m3,x)	(m3.m[0][1] /= (x))
#define m3DivXZ(m3,x)	(m3.m[0][2] /= (x))
#define m3DivYX(m3,x)	(m3.m[1][0] /= (x))
#define m3DivYY(m3,x)	(m3.m[1][1] /= (x))
#define m3DivYZ(m3,x)	(m3.m[1][2] /= (x))
#define m3DivZX(m3,x)	(m3.m[2][0] /= (x))
#define m3DivZY(m3,x)	(m3.m[2][1] /= (x))
#define m3DivZZ(m3,x)	(m3.m[2][2] /= (x))

#define m3GetXX(m3)	(m3.m[0][0])
#define m3GetXY(m3)	(m3.m[0][1])
#define m3GetXZ(m3)	(m3.m[0][2])
#define m3GetYX(m3)	(m3.m[1][0])
#define m3GetYY(m3)	(m3.m[1][1])
#define m3GetYZ(m3)	(m3.m[1][2])
#define m3GetZX(m3)	(m3.m[2][0])
#define m3GetZY(m3)	(m3.m[2][1])
#define m3GetZZ(m3)	(m3.m[2][2])

#define m3IncXX(m3,x)	(m3.m[0][0] += (x))
#define m3IncXY(m3,x)	(m3.m[0][1] += (x))
#define m3IncXZ(m3,x)	(m3.m[0][2] += (x))
#define m3IncYX(m3,x)	(m3.m[1][0] += (x))
#define m3IncYY(m3,x)	(m3.m[1][1] += (x))
#define m3IncYZ(m3,x)	(m3.m[1][2] += (x))
#define m3IncZX(m3,x)	(m3.m[2][0] += (x))
#define m3IncZY(m3,x)	(m3.m[2][1] += (x))
#define m3IncZZ(m3,x)	(m3.m[2][2] += (x))

#define m3MulXX(m3,x)	(m3.m[0][0] *= (x))
#define m3MulXY(m3,x)	(m3.m[0][1] *= (x))
#define m3MulXZ(m3,x)	(m3.m[0][2] *= (x))
#define m3MulYX(m3,x)	(m3.m[1][0] *= (x))
#define m3MulYY(m3,x)	(m3.m[1][1] *= (x))
#define m3MulYZ(m3,x)	(m3.m[1][2] *= (x))
#define m3MulZX(m3,x)	(m3.m[2][0] *= (x))
#define m3MulZY(m3,x)	(m3.m[2][1] *= (x))
#define m3MulZZ(m3,x)	(m3.m[2][2] *= (x))

#define m3SetXX(m3,x)	(m3.m[0][0] = (x))
#define m3SetXY(m3,x)	(m3.m[0][1] = (x))
#define m3SetXZ(m3,x)	(m3.m[0][2] = (x))
#define m3SetYX(m3,x)	(m3.m[1][0] = (x))
#define m3SetYY(m3,x)	(m3.m[1][1] = (x))
#define m3SetYZ(m3,x)	(m3.m[1][2] = (x))
#define m3SetZX(m3,x)	(m3.m[2][0] = (x))
#define m3SetZY(m3,x)	(m3.m[2][1] = (x))
#define m3SetZZ(m3,x)	(m3.m[2][2] = (x))

/* EXTERN_START */
/* EXTERN_STOP */

#endif
