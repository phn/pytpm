/* file: $RCSfile: m6scale.c,v $
** rcsid: $Id: m6scale.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m6scale.c,v $ - scale a 6-matrix by a constant
** *******************************************************************
*/

#include "vec.h"

M6
m6scale(M6 m, double s)
{
    m.m[0][0] = m3scale(m.m[0][0], s);
    m.m[0][1] = m3scale(m.m[0][1], s);
    m.m[1][0] = m3scale(m.m[1][0], s);
    m.m[1][1] = m3scale(m.m[1][1], s);

    return(m);
}
