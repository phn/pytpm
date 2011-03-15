/* file: $RCSfile: m3scale.c,v $
** rcsid: $Id: m3scale.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3scale.c,v $ - scale a 3-matrix
** *******************************************************************
*/

#include "vec.h"

M3
m3scale(M3 m, double s)
{
    m3MulXX(m, s);
    m3MulXY(m, s);
    m3MulXZ(m, s);

    m3MulYX(m, s);
    m3MulYY(m, s);
    m3MulYZ(m, s);

    m3MulZX(m, s);
    m3MulZY(m, s);
    m3MulZZ(m, s);

    return(m);
}
