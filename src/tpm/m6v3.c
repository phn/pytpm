/* file: $RCSfile: m6v3.c,v $
** rcsid: $Id: m6v3.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m6v3.c,v $ - product of a 6-matrix and a 3-vector.
** we define this operation to be a normal m6m6 with a null velocity component.
** *******************************************************************
*/

#include "vec.h"

V3
m6v3(M6 m, V3 v)
{
    v = m3v3(m6GetPP(m), v);

    return(v);
}
