/* file: $RCSfile: delta_AT.c,v $
** rcsid: $Id: delta_AT.c 767 2009-01-02 22:27:16Z laidler $
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
** $RCSfile: delta_AT.c,v $
** return the difference (TAI - UTC) in seconds.
** before 1972 Jan 1, a fixed value of 10 seconds is returned.
**       THIS FILE MUST BE UPDATED WHENEVER A LEAP SECOND IS ADDED.
** Compute the MJD of the first date to which the leap second applies
** and use that as the comparison in the code below.
**
** this is modelled after sla_DAT by P. T. Wallace
** *******************************************************************
*/

#include "astro.h"

double
delta_AT(double utc)
{
    double dt = 10.0;

    /* make it an MJD */
    utc -= MJD_0;

    if (utc >= 41499.0) dt = 11.0;	/* 1972 Jul 1 */

    if (utc >= 41683.0) dt = 12.0;	/* 1973 Jan 1 */

    if (utc >= 42048.0) dt = 13.0;	/* 1974 Jan 1 */

    if (utc >= 42413.0) dt = 14.0;	/* 1975 Jan 1 */

    if (utc >= 42778.0) dt = 15.0;	/* 1976 Jan 1 */

    if (utc >= 43144.0) dt = 16.0;	/* 1977 Jan 1 */

    if (utc >= 43509.0) dt = 17.0;	/* 1978 Jan 1 */

    if (utc >= 43874.0) dt = 18.0;	/* 1979 Jan 1 */

    if (utc >= 44239.0) dt = 19.0;	/* 1980 Jan 1 */

    if (utc >= 44786.0) dt = 20.0;	/* 1981 Jul 1 */

    if (utc >= 45151.0) dt = 21.0;	/* 1982 Jul 1 */

    if (utc >= 45516.0) dt = 22.0;	/* 1983 Jul 1 */

    if (utc >= 46247.0) dt = 23.0;	/* 1985 Jul 1 */

    if (utc >= 47161.0) dt = 24.0;	/* 1988 Jan 1 */

    if (utc >= 47892.0) dt = 25.0;	/* 1990 Jan 1 */

    if (utc >= 48257.0) dt = 26.0;	/* 1991 Jan 1 */

    if (utc >= 48804.0) dt = 27.0;	/* 1992 July 1 */

    if (utc >= 49169.0) dt = 28.0;	/* 1993 July 1 */

    if (utc >= 49534.0) dt = 29.0;	/* 1994 July 1 */

    if (utc >= 50083.0) dt = 30.0;	/* 1996 Jan 1 */

    if (utc >= 50630.0) dt = 31.0;	/* 1997 Jul 1 */

    if (utc >= 51179.0) dt = 32.0;	/* 1999 Jan 1 */

    if (utc >= 53736.0) dt = 33.0;	/* 2006 Jan 1 */

    if (utc >= 54832.0) dt = 34.0;	/* 2009 Jan 1 */

    if (utc >= 56109.0) dt = 35.0;	/* 2012 July 1 */    

    return(dt);
}
