/* file: $RCSfile: m3RyDot.c,v $
** rcsid: $Id: m3RyDot.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3RyDot.c,v $ - the R2-dot matrix from Yallop et al., AJ 97, 274.
** *******************************************************************
*/

#include "vec.h"

M3
m3RyDot(double y, double ydot)
{
    M3 m3;

    m3 = m3O();
    m3SetXX(m3, ydot * -sin(y));
    m3SetXZ(m3, ydot * -cos(y));
    m3SetZX(m3, ydot * cos(y));
    m3SetZZ(m3, ydot * -sin(y));

    return(m3);

}
