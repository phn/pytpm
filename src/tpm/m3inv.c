/* file: $RCSfile: m3inv.c,v $
** rcsid: $Id: m3inv.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3inv.c,v $ - invert a 3-matrix
** we assume orthogonality, so the inverse is merely the transpose
** *******************************************************************
*/

#include "vec.h"

M3
m3inv(M3 m)
{
    M3 mi;

    m3SetXX(mi, m3GetXX(m));
    m3SetXY(mi, m3GetYX(m));
    m3SetXZ(mi, m3GetZX(m));

    m3SetYX(mi, m3GetXY(m));
    m3SetYY(mi, m3GetYY(m));
    m3SetYZ(mi, m3GetZY(m));

    m3SetZX(mi, m3GetXZ(m));
    m3SetZY(mi, m3GetYZ(m));
    m3SetZZ(mi, m3GetZZ(m));

    return(mi);
}
