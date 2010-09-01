/* file: $RCSfile: m3Rz.c,v $
** rcsid: $Id: m3Rz.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3Rz.c,v $ - the R3 matrix from Yallop et al., AJ 97, 274.
** *******************************************************************
*/

#include "vec.h"

M3
m3Rz(double z)
{
    M3 m3;

    m3 = m3I(1.0);
    m3SetXX(m3, cos(z));
    m3SetXY(m3, sin(z));
    m3SetYX(m3, -sin(z));
    m3SetYY(m3, cos(z));

    return(m3);

}
