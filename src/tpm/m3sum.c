/* file: $RCSfile: m3sum.c,v $
** rcsid: $Id: m3sum.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3sum.c,v $ - sum of two 3-matrices
** *******************************************************************
*/

#include "vec.h"

M3
m3sum(M3 m1, M3 m2)
{
    m3IncXX(m1, m3GetXX(m2));
    m3IncXY(m1, m3GetXY(m2));
    m3IncXZ(m1, m3GetXZ(m2));

    m3IncYX(m1, m3GetYX(m2));
    m3IncYY(m1, m3GetYY(m2));
    m3IncYZ(m1, m3GetYZ(m2));

    m3IncZX(m1, m3GetZX(m2));
    m3IncZY(m1, m3GetZY(m2));
    m3IncZZ(m1, m3GetZZ(m2));

    return(m1);
}
