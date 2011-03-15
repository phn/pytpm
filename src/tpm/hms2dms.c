/* file: $RCSfile: hms2dms.c,v $
** rcsid: $Id: hms2dms.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: hms2dms.c,v $ - convert hms time into dms angle
** *******************************************************************
*/

#include "times.h"

DMS
hms2dms(HMS hms)
{
    DMS dms;

    dmsSetDegrees(dms, hmsGetHours(hms) * 15.0);
    dmsSetMinutes(dms, hmsGetMinutes(hms) * 15.0);
    dmsSetSeconds(dms, hmsGetSeconds(hms) * 15.0);

    return(dms);
}
