/* file: $RCSfile: m3I.c,v $
** rcsid: $Id: m3I.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3I.c,v $ - the identity 3-matrix (scaled by the given value)
** *******************************************************************
*/

#include "vec.h"

M3
m3I(double x)
{
    M3 m;

    m3SetXX(m, x);
    m3SetXY(m, 0);
    m3SetXZ(m, 0);

    m3SetYX(m, 0);
    m3SetYY(m, x);
    m3SetYZ(m, 0);

    m3SetZX(m, 0);
    m3SetZY(m, 0);
    m3SetZZ(m, x);

    return(m);

}
