/* file: $RCSfile: y2doy.c,v $
** rcsid: $Id: y2doy.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: y2doy.c,v $ - return days per year given the gregorian proleptic calendar year
** 0 => 1 BC
** *******************************************************************
*/

#include "times.h"

int
y2doy(int y)
{
    int doy;

    if ((y % 400) == 0) {
	doy = 366;
    } else if ((y % 100) == 0) {
	doy = 365;
    } else if ((y % 4) == 0) {
	doy = 366;
    } else {
	doy = 365;
    }

    return(doy);
}
