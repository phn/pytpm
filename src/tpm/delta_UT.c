/* file: $RCSfile: delta_UT.c,v $
** rcsid: $Id: delta_UT.c,v 1.5 2003/09/03 20:19:12 jwp Exp $
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
static char *rcsid = "$Id: delta_UT.c,v 1.5 2003/09/03 20:19:12 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: delta_UT.c,v $
** return the difference (UT1 - UTC) in seconds.
** *******************************************************************
*/

#include "astro.h"

double
delta_UT(double utc)
{
    double dt;

    /*
    ** note that the argument of delta_T should really be UT1 not UTC,
    ** but delta_T varies slowly through the year, so the error in not
    ** using UT1 should be small.
    */
    dt = delta_ET(utc) - delta_T(utc);

    return(dt);
}
