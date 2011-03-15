/* file: $RCSfile: v6delta.c,v $
** rcsid: $Id: v6delta.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6delta.c,v $ - return the angle out of the x-y plane (declination)
** *******************************************************************
*/

#include "vec.h"

double
v6delta(V6 v)
{
    return(v3delta(v6GetPos(v)));
}
