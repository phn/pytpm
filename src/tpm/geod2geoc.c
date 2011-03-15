/* file: $RCSfile: geod2geoc.c,v $
** rcsid: $Id: geod2geoc.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: geod2geoc.c,v $
** geodetic to geocentric position
** see Exp. Supp. AA (1992), p 162.
** *******************************************************************
*/

#include "astro.h"

V6
geod2geoc(double lon, double lat, double alt)
{
    double C;
    double S;
    double x;
    double xdot;
    double y;
    double ydot;
    double z;
    double zdot;
    V6 g;	/* the equatorial rectangular state vector */

    C = 1 / sqrt(cos(lat)*cos(lat) + (1-IAU_F)*(1-IAU_F)*sin(lat)*sin(lat));

    S = (1-IAU_F) * (1-IAU_F) * C;

    x = ((IAU_RE * C) + alt) * cos(lat) * cos(lon);
    y = ((IAU_RE * C) + alt) * cos(lat) * sin(lon);
    z = ((IAU_RE * S) + alt) * sin(lat);

    /* the velocity vector is the cross product wk^g */
    xdot = -IAU_W * y;
    ydot = IAU_W * x;
    zdot = 0.0;

    g = v6init(CARTESIAN);
    v6SetX(g, x);
    v6SetY(g, y);
    v6SetZ(g, z);
    v6SetXDot(g, xdot);
    v6SetYDot(g, ydot);
    v6SetZDot(g, zdot);

    return(g);
}
