/* file: $RCSfile: m3RzDot.c,v $
** rcsid: $Id: m3RzDot.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3RzDot.c,v $ - the R3-dot matrix from Yallop et al., AJ 97, 274.
** *******************************************************************
*/

#include "vec.h"

M3
m3RzDot(double z, double zdot)
{
    M3 m3;

    m3 = m3O();
    m3SetXX(m3, zdot * -sin(z));
    m3SetXY(m3, zdot * cos(z));
    m3SetYX(m3, zdot * -cos(z));
    m3SetYY(m3, zdot * -sin(z));

    return(m3);

}
