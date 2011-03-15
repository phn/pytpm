/* file: $RCSfile: m6O.c,v $
** rcsid: $Id: m6O.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m6O.c,v $ - the null 6-matrix
** *******************************************************************
*/

#include "vec.h"

M6
m6O(void)
{
    M6 m;

    m.m[0][0] = m3O();
    m.m[0][1] = m3O();
    m.m[1][0] = m3O();
    m.m[1][1] = m3O();

    return(m);

}
