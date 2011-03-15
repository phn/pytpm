/* file: $RCSfile: v6alpha.c,v $
** rcsid: $Id: v6alpha.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6alpha.c,v $ - return the angle in the x-y plane (right ascension)
** *******************************************************************
*/

#include "vec.h"

double
v6alpha(V6 v)
{
    return(v3alpha(v6GetPos(v)));
}
