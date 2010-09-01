/* file: $RCSfile: m3diff.c,v $
** rcsid: $Id: m3diff.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3diff.c,v $ - the difference of two 3-matrices
** *******************************************************************
*/

#include "vec.h"

M3
m3diff(M3 m1, M3 m2)
{
    m3DecXX(m1, m3GetXX(m2));
    m3DecXY(m1, m3GetXY(m2));
    m3DecXZ(m1, m3GetXZ(m2));

    m3DecYX(m1, m3GetYX(m2));
    m3DecYY(m1, m3GetYY(m2));
    m3DecYZ(m1, m3GetYZ(m2));

    m3DecZX(m1, m3GetZX(m2));
    m3DecZY(m1, m3GetZY(m2));
    m3DecZZ(m1, m3GetZZ(m2));

    return(m1);
}
