/* file: $RCSfile: m6sum.c,v $
** rcsid: $Id: m6sum.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m6sum.c,v $ - sum of two 6-matrices
** *******************************************************************
*/

#include "vec.h"

M6
m6sum(M6 m1, M6 m2)
{
    m1.m[0][0] = m3sum(m1.m[0][0], m2.m[0][0]);
    m1.m[0][1] = m3sum(m1.m[0][1], m2.m[0][1]);
    m1.m[1][0] = m3sum(m1.m[1][0], m2.m[1][0]);
    m1.m[1][1] = m3sum(m1.m[1][1], m2.m[1][1]);

    return(m1);
}
