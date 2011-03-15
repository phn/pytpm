/* file: $RCSfile: m3Rx.c,v $
** rcsid: $Id: m3Rx.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3Rx.c,v $ - the R1 matrix from Yallop et al., AJ 97, 274.
** *******************************************************************
*/

#include "vec.h"

M3
m3Rx(double x)
{
    M3 m3;

    m3 = m3I(1.0);
    m3SetYY(m3, cos(x));
    m3SetYZ(m3, sin(x));
    m3SetZY(m3, -sin(x));
    m3SetZZ(m3, cos(x));

    return(m3);

}
