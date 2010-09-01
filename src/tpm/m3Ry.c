/* file: $RCSfile: m3Ry.c,v $
** rcsid: $Id: m3Ry.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3Ry.c,v $ - the R2 matrix from Yallop et al., AJ 97, 274.
** *******************************************************************
*/

#include "vec.h"

M3
m3Ry(double y)
{
    M3 m3;

    m3 = m3I(1.0);
    m3SetXX(m3, cos(y));
    m3SetXZ(m3, -sin(y));
    m3SetZX(m3, sin(y));
    m3SetZZ(m3, cos(y));

    return(m3);

}
