/* file: $RCSfile: m6I.c,v $
** rcsid: $Id: m6I.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m6I.c,v $ - the identity 6-matrix
** *******************************************************************
*/

#include "vec.h"

M6
m6I(double x)
{
    M6 m;

    m.m[0][0] = m3I(x);
    m.m[0][1] = m3O();
    m.m[1][0] = m3O();
    m.m[1][1] = m3I(x);

    return(m);

}
