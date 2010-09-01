/* file: $RCSfile: m6.h,v $
** rcsid: $Id: m6.h 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m6.h,v $ -
**********************************************************************
*/

#ifndef M6_INCLUDE
#define M6_INCLUDE

typedef struct s_m6 {
	M3 m[2][2];
} M6;

#define m6GetPP(m6)	(m6.m[0][0])
#define m6GetPV(m6)	(m6.m[0][1])
#define m6GetVP(m6)	(m6.m[1][0])
#define m6GetVV(m6)	(m6.m[1][1])

#define m6SetPP(m6,m3)	(m6.m[0][0] = (m3))
#define m6SetPV(m6,m3)	(m6.m[0][1] = (m3))
#define m6SetVP(m6,m3)	(m6.m[1][0] = (m3))
#define m6SetVV(m6,m3)	(m6.m[1][1] = (m3))

/* EXTERN_START */
/* EXTERN_STOP */

#endif
