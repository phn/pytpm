/* file: $RCSfile: m6inv.c,v $
** rcsid: $Id: m6inv.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m6inv.c,v $ - invert a 6-matrix
** we assume it is composed of orthogonal 3-matrices
** *******************************************************************
*/

#include "vec.h"

M6
m6inv(M6 m)
{
    m.m[0][0] = m3inv(m.m[0][0]);
    m.m[0][1] = m3inv(m.m[0][1]);
    m.m[1][0] = m3inv(m.m[1][0]);
    m.m[1][1] = m3inv(m.m[1][1]);

    return(m);
}
