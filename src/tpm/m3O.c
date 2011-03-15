/* file: $RCSfile: m3O.c,v $
** rcsid: $Id: m3O.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3O.c,v $ - the null 3-matrix
** *******************************************************************
*/

#include "vec.h"

M3
m3O(void)
{
    M3 m;

    m3SetXX(m, 0);
    m3SetXY(m, 0);
    m3SetXZ(m, 0);

    m3SetYX(m, 0);
    m3SetYY(m, 0);
    m3SetYZ(m, 0);

    m3SetZX(m, 0);
    m3SetZY(m, 0);
    m3SetZZ(m, 0);

    return(m);

}
