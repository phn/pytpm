/* file: $RCSfile: m6Qx.c,v $
** rcsid: $Id: m6Qx.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m6Qx.c,v $ - the Q1 matrix from Yallop et al., AJ 97, 274.
** *******************************************************************
*/

#include "vec.h"

M6
m6Qx(double x, double xdot)
{
    M6 m6;

    m6SetPP(m6, m3Rx(x));
    m6SetPV(m6, m3O());
    m6SetVP(m6, m3RxDot(x, xdot));
    m6SetVV(m6, m3Rx(x));

    return(m6);

}
