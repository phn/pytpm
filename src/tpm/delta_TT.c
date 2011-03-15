/* file: $RCSfile: delta_TT.c,v $
** rcsid: $Id: delta_TT.c,v 1.5 2003/09/03 20:19:12 jwp Exp $
** Copyright Jeffrey W Percival
** *******************************************************************
** Space Astronomy Laboratory
** University of Wisconsin
** 1150 University Avenue
** Madison, WI 53706 USA
** *******************************************************************
** Do not use this software without permission.
** Do not use this software without attribution.
** Do not remove or alter any of the lines above.
** *******************************************************************
*/
static char *rcsid = "$Id: delta_TT.c,v 1.5 2003/09/03 20:19:12 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: delta_TT.c,v $
** return the difference (TDT - UTC) in seconds.
** *******************************************************************
*/

#include "astro.h"

double
delta_TT(double utc)
{
    double dt;

    dt = delta_AT(utc) + 32.184;

    return(dt);
}
