/* file: $RCSfile: m3m3.c,v $
** rcsid: $Id: m3m3.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3m3.c,v $ - product of two 3-matrices
** *******************************************************************
*/

#include "vec.h"

M3
m3m3(M3 m1, M3 m2)
{
    int row, col;
    int i;
    M3 m;

    for (row = 0; row < 3; row++) {
	for (col = 0; col < 3; col++) {
	    m.m[row][col] = 0;
	    for (i = 0; i < 3; i++) {
		m.m[row][col] += m1.m[row][i] * m2.m[i][col];
	    }
	}
    }

    return(m);
}
