/* file: $RCSfile: v6unit.c,v $
** rcsid: $Id: v6unit.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6unit.c,v $ - return a unit 6-vector
** *******************************************************************
*/

#include "vec.h"

V6
v6unit(V6 v)
{
    double m;

    m = v6mod(v);
    if (m != 0.0) {
	v = v6scale(v, 1/m);
    }

    return(v);
}
