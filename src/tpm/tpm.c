/* file: $RCSfile: tpm.c,v $
** rcsid: $Id: tpm.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: tpm.c,v $
** telescope pointing machine
** *******************************************************************
*/

#include "astro.h"

#undef DEBUG

/* the telescope pointing machine state table */
static TPM_PMCELL pmtab[N_TPM_STATES][N_TPM_STATES] = {

	/* start state TPM_S00 */
	{
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S00},
	},

	/* start state TPM_S01 */
	{
		{TPM_T00, TPM_S00},
		{TPM_T00, TPM_S01},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
		{TPM_T01, TPM_S05},
	},

	/* start state TPM_S02 */
	{
		{TPM_T00, TPM_S00},
		{TPM_T02, TPM_S06},
		{TPM_T00, TPM_S02},
		{-TPM_T03, TPM_S03},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
		{TPM_T02, TPM_S06},
	},

	/* start state TPM_S03 */
	{
		{TPM_T00, TPM_S00},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T00, TPM_S03},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
		{TPM_T03, TPM_S02},
	},

	/* start state TPM_S04 */
	{
		{TPM_T00, TPM_S00},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T00, TPM_S04},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
		{TPM_T04, TPM_S05},
	},

	/* start state TPM_S05 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T01, TPM_S01},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{-TPM_T04, TPM_S04},
		{TPM_T00, TPM_S05},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
		{TPM_T05, TPM_S06},
	},

	/* start state TPM_S06 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T05, TPM_S05},
		{-TPM_T02, TPM_S02},
		{-TPM_T02, TPM_S02},
		{-TPM_T05, TPM_S05},
		{-TPM_T05, TPM_S05},
		{TPM_T00, TPM_S06},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
		{TPM_T06, TPM_S07},
	},

	/* start state TPM_S07 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T06, TPM_S06},
		{-TPM_T06, TPM_S06},
		{-TPM_T06, TPM_S06},
		{-TPM_T06, TPM_S06},
		{-TPM_T06, TPM_S06},
		{-TPM_T06, TPM_S06},
		{TPM_T00, TPM_S07},
		{TPM_T08, TPM_S08},
		{TPM_T08, TPM_S08},
		{TPM_T08, TPM_S08},
		{TPM_T08, TPM_S08},
		{TPM_T07, TPM_S12},
		{TPM_T07, TPM_S12},
		{TPM_T07, TPM_S12},
		{TPM_T07, TPM_S12},
		{TPM_T07, TPM_S12},
		{TPM_T07, TPM_S12},
		{TPM_T07, TPM_S12},
		{TPM_T07, TPM_S12},
		{TPM_T07, TPM_S12},
		{TPM_T07, TPM_S12},
	},

	/* start state TPM_S08 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{TPM_T00, TPM_S08},
		{TPM_T09, TPM_S09},
		{TPM_T09, TPM_S09},
		{TPM_T09, TPM_S09},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
		{-TPM_T08, TPM_S07},
	},

	/* start state TPM_S09 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{TPM_T00, TPM_S09},
		{TPM_T10, TPM_S10},
		{TPM_T10, TPM_S10},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
		{-TPM_T09, TPM_S08},
	},

	/* start state TPM_S10 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{TPM_T00, TPM_S10},
		{TPM_T11, TPM_S11},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
		{-TPM_T10, TPM_S09},
	},

	/* start state TPM_S11 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{TPM_T00, TPM_S11},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
		{-TPM_T11, TPM_S10},
	},

	/* start state TPM_S12 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T07, TPM_S07},
		{-TPM_T07, TPM_S07},
		{-TPM_T07, TPM_S07},
		{-TPM_T07, TPM_S07},
		{-TPM_T07, TPM_S07},
		{-TPM_T07, TPM_S07},
		{-TPM_T07, TPM_S07},
		{-TPM_T07, TPM_S07},
		{-TPM_T07, TPM_S07},
		{-TPM_T07, TPM_S07},
		{-TPM_T07, TPM_S07},
		{TPM_T00, TPM_S12},
		{TPM_T08, TPM_S13},
		{TPM_T08, TPM_S13},
		{TPM_T08, TPM_S13},
		{TPM_T08, TPM_S13},
		{TPM_T08, TPM_S13},
		{TPM_T08, TPM_S13},
		{TPM_T08, TPM_S13},
		{TPM_T08, TPM_S13},
		{TPM_T08, TPM_S13},
	},

	/* start state TPM_S13 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T08, TPM_S12},
		{-TPM_T08, TPM_S12},
		{-TPM_T08, TPM_S12},
		{-TPM_T08, TPM_S12},
		{-TPM_T08, TPM_S12},
		{-TPM_T08, TPM_S12},
		{-TPM_T08, TPM_S12},
		{-TPM_T08, TPM_S12},
		{-TPM_T08, TPM_S12},
		{-TPM_T08, TPM_S12},
		{-TPM_T08, TPM_S12},
		{-TPM_T08, TPM_S12},
		{TPM_T00, TPM_S13},
		{TPM_T09, TPM_S14},
		{TPM_T09, TPM_S14},
		{TPM_T09, TPM_S14},
		{TPM_T09, TPM_S14},
		{TPM_T09, TPM_S14},
		{TPM_T09, TPM_S14},
		{TPM_T09, TPM_S14},
		{TPM_T09, TPM_S14},
	},

	/* start state TPM_S14 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{-TPM_T09, TPM_S13},
		{TPM_T00, TPM_S14},
		{TPM_T10, TPM_S15},
		{TPM_T10, TPM_S15},
		{TPM_T10, TPM_S15},
		{TPM_T10, TPM_S15},
		{TPM_T10, TPM_S15},
		{TPM_T10, TPM_S15},
		{TPM_T10, TPM_S15},
	},

	/* start state TPM_S15 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{-TPM_T10, TPM_S14},
		{TPM_T00, TPM_S15},
		{TPM_T11, TPM_S16},
		{TPM_T11, TPM_S16},
		{TPM_T11, TPM_S16},
		{TPM_T11, TPM_S16},
		{TPM_T11, TPM_S16},
		{TPM_T11, TPM_S16},
	},

	/* start state TPM_S16 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{-TPM_T11, TPM_S15},
		{TPM_T00, TPM_S16},
		{TPM_T12, TPM_S17},
		{TPM_T12, TPM_S17},
		{TPM_T12, TPM_S17},
		{TPM_T12, TPM_S17},
		{TPM_T12, TPM_S17},
	},

	/* start state TPM_S17 */
	{
		{TPM_T12, TPM_S00},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{-TPM_T12, TPM_S16},
		{TPM_T00, TPM_S17},
		{TPM_T13, TPM_S18},
		{TPM_T13, TPM_S18},
		{TPM_T13, TPM_S18},
		{TPM_T13, TPM_S18},
	},

	/* start state TPM_S18 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{-TPM_T13, TPM_S17},
		{TPM_T00, TPM_S18},
		{TPM_T14, TPM_S19},
		{TPM_T14, TPM_S19},
		{TPM_T14, TPM_S19},
	},

	/* start state TPM_S19 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{-TPM_T14, TPM_S18},
		{TPM_T00, TPM_S19},
		{-TPM_T13, TPM_S20},
		{TPM_T15, TPM_S21},
	},

	/* start state TPM_S20 */
	{
		{TPM_T00, TPM_S00},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T13, TPM_S19},
		{TPM_T00, TPM_S20},
		{TPM_T13, TPM_S19},
	},

	/* start state TPM_S21 */
	{
		{TPM_T00, TPM_S00},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{-TPM_T15, TPM_S19},
		{TPM_T00, TPM_S21},
	}
};

int
tpm(V6 *pvec, int s1, int s2, double ep, double eq, TPM_TSTATE *tstate)
{
    int s;		/* the current state */
    V6 v6;	/* working vector */
    V6 vx;	/* scratch vector */

    /********************************/
    /* ensure cartesian coordinates */
    /********************************/
    pvec[s1] = v6s2c(pvec[s1]);

#ifdef DEBUG
    (void)fprintf(stdout, "pm: vc pvec[%d] = %s\n", s1, v6fmt(pvec[s1]));
    (void)fprintf(stdout, "pm: vs pvec[%d] = %s\n", s1, v6fmt(v6c2s(pvec[s1])));
#endif

    s = s1;
    while ((s != TPM_S00) && (s != s2)) {

#ifdef DEBUG
	(void)fprintf(stdout, "pm: state s%02d --> state s%02d (t%03d,s%02d)\n",
		s,
		s2,
		pmtab[s][s2].ptrans,
		pmtab[s][s2].pstate);
#endif

	/*************************************************************/
	/* now send this position vector through the next transition */
	/*************************************************************/

	switch (pmtab[s][s2].ptrans) {
	case TPM_T00:

	    /***********************/
	    /* the null transition */
	    /***********************/

	    pvec[pmtab[s][s2].pstate] = pvec[s];

	    break;

	case TPM_T01:

	    v6 = pvec[s];

	    /**************************/
	    /* remove current e-terms */
	    /**************************/
	    v6 = ellab(eq, v6, -1);

	    /****************************/
	    /* precess from eq to B1950 */
	    /****************************/
	    v6 = precess(eq, B1950, v6, PRECESS_FK4);

	    /************************/
	    /* add in B1950 e-terms */
	    /************************/
	    v6 = ellab(B1950, v6, 1);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T01:

	    v6 = pvec[s];

	    /************************/
	    /* remove B1950 e-terms */
	    /************************/
	    v6 = ellab(B1950, v6, -1);

	    /****************************/
	    /* precess from B1950 to eq */
	    /****************************/
	    v6 = precess(B1950, eq, v6, PRECESS_FK4);

	    /**************************/
	    /* add in current e-terms */
	    /**************************/
	    v6 = ellab(eq, v6, 1);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T02:

	    /****************************/
	    /* precess from eq to J2000 */
	    /****************************/

	    v6 = pvec[s];

	    v6 = precess(eq, J2000, v6, PRECESS_FK5);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T02:

	    /****************************/
	    /* precess from J2000 to eq */
	    /****************************/

	    v6 = pvec[s];

	    v6 = precess(J2000, eq, v6, PRECESS_FK5);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T03:

	    /**************************/
	    /* ecliptic to equatorial */
	    /**************************/

	    v6 = pvec[s];

	    v6 = ecl2equ(v6, tstate->obliquity);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T03:

	    /**************************/
	    /* equatorial to ecliptic */
	    /**************************/

	    v6 = pvec[s];

	    v6 = equ2ecl(v6, tstate->obliquity);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T04:

	    /**************************/
	    /* galactic to equatorial */
	    /**************************/

	    v6 = pvec[s];

	    v6 = gal2equ(v6);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T04:

	    /**************************/
	    /* equatorial to galactic */
	    /**************************/

	    v6 = pvec[s];

	    v6 = equ2gal(v6);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T05:

	    /**************/
	    /* FK4 to FK5 */
	    /**************/

	    v6 = pvec[s];

	    /* apply proper motion from the epoch to B1950 */
	    v6 = proper_motion(v6, B1950, ep);

	    /* transform from fk4 to fk5 */
	    v6 = fk425(v6);

	    /* remove proper motion from J2000 to the epoch */
	    v6 = proper_motion(v6, ep, J2000);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T05:

	    /**************/
	    /* FK5 to FK4 */
	    /**************/

	    v6 = pvec[s];

	    /* apply proper motion from the epoch to J2000 */
	    v6 = proper_motion(v6, J2000, ep);

	    /* transform from fk5 to fk4 */
	    v6 = fk524(v6);

	    /* remove proper motion from B1950 to the epoch */
	    v6 = proper_motion(v6, ep, B1950);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T06:

	    /*************************/
	    /* heliocentric parallax */
	    /*************************/

	    v6 = pvec[s];

	    v6 = v6diff(v6, tstate->eb);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T06:

	    /*************************/
	    /* heliocentric parallax */
	    /*************************/

	    v6 = pvec[s];

	    v6 = v6sum(v6, tstate->eb);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T07:

	    /***********************/
	    /* geocentric parallax */
	    /***********************/

	    v6 = pvec[s];

	    v6 = v6diff(v6, tstate->obs_s);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T07:

	    /***********************/
	    /* geocentric parallax */
	    /***********************/

	    v6 = pvec[s];

	    v6 = v6sum(v6, tstate->obs_s);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T08:

	    /********************/
	    /* light deflection */
	    /********************/

	    v6 = pvec[s];

	    v6 = ldeflect(v6, tstate->eh, 1);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T08:

	    /********************/
	    /* light deflection */
	    /********************/

	    v6 = pvec[s];

	    v6 = ldeflect(v6, tstate->eh, -1);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T09:

	    /**************/
	    /* aberration */
	    /**************/

	    v6 = pvec[s];

	    if (s == TPM_S13) {
		/* topocentric aberration */
		vx = v6sum(tstate->eb, tstate->obs_s);
	    } else {
		/* geocentric aberration */
		vx = tstate->eb;
	    }

	    v6 = aberrate(v6, vx, 1);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T09:

	    /**************/
	    /* aberration */
	    /**************/

	    v6 = pvec[s];

	    if (s == TPM_S14) {
		/* topocentric aberration */
		vx = v6sum(tstate->eb, tstate->obs_s);
	    } else {
		/* geocentric aberration */
		vx = tstate->eb;
	    }

	    v6 = aberrate(v6, vx, -1);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T10:

	    /******************************/
	    /* precess from J2000 to date */
	    /******************************/

	    v6 = pvec[s];

	    v6 = m6v6(tstate->pm, v6);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T10:

	    /******************************/
	    /* precess from date to J2000 */
	    /******************************/

	    v6 = pvec[s];

	    v6 = m6v6(m6inv(tstate->pm), v6);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T11:

	    /************/
	    /* nutation */
	    /************/

	    v6 = pvec[s];

	    v6 = m3v6(tstate->nm, v6);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T11:

	    /************/
	    /* nutation */
	    /************/

	    v6 = pvec[s];

	    v6 = m3v6(m3inv(tstate->nm), v6);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T12:

	    /********************/
	    /* earth's rotation */
	    /********************/

	    v6 = pvec[s];

	    v6 = m3v6(m3Rz(tstate->gast), v6);
	    v6 = m3v6(m3Rx(-tstate->ypole), v6);
	    v6 = m3v6(m3Ry(-tstate->xpole), v6);
	    v6 = m3v6(m3Rz(tstate->lon), v6);

	    /* change to left handed frame */
	    v6MulY(v6, -1.0);
	    v6MulYDot(v6, -1.0);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T12:

	    /********************/
	    /* earth's rotation */
	    /********************/

	    v6 = pvec[s];

	    /* change to right handed frame */
	    v6 = v6s2c(v6);
	    v6MulY(v6, -1.0);
	    v6MulYDot(v6, -1.0);

	    v6 = m3v6(m3Rz(-tstate->lon), v6);
	    v6 = m3v6(m3Ry(tstate->xpole), v6);
	    v6 = m3v6(m3Rx(tstate->ypole), v6);
	    v6 = m3v6(m3Rz(-tstate->gast), v6);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T13:

	    /*************************/
	    /* (HA, Dec) to (Az, El) */
	    /*************************/

	    v6 = pvec[s];

	    v6 = hadec2azel(v6, tstate->lat);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T13:

	    /*************************/
	    /* (Az, El) to (HA, Dec) */
	    /*************************/

	    v6 = pvec[s];

	    v6 = azel2hadec(v6, tstate->lat);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case TPM_T14:

	    /**************/
	    /* refraction */
	    /**************/

	    v6 = pvec[s];

	    {
		double z, dz;

		v6 = v6c2s(v6);

		z = M_PI/2 - v6GetDelta(v6);
		dz = refract(z, tstate->refa, tstate->refb, 1);
		z += dz;
		v6SetDelta(v6, (M_PI/2 - z));

		v6 = v6s2c(v6);
	    }

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T14:

	    /**************/
	    /* refraction */
	    /**************/

	    v6 = pvec[s];

	    {
		double z, dz;

		v6 = v6c2s(v6);

		z = M_PI/2 - v6GetDelta(v6);
		dz = refract(z, tstate->refa, tstate->refb, -1);
		z += dz;
		v6SetDelta(v6, (M_PI/2 - z));

		v6 = v6s2c(v6);
	    }

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;
	
	case TPM_T15:

	    /********/
	    /* wham */
	    /********/

	    v6 = pvec[s];

	    v6 = m3v6(m3Ry(M_PI/2), v6);
	    v6 = m3v6(m3Rz(M_PI), v6);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;

	case -TPM_T15:

	    /********/
	    /* wham */
	    /********/

	    v6 = pvec[s];

	    v6 = m3v6(m3Rz(-M_PI), v6);
	    v6 = m3v6(m3Ry(-M_PI/2), v6);

	    pvec[pmtab[s][s2].pstate] = v6;

	    break;
	
	default:
	    break;

	}

#ifdef DEBUG
	(void)fprintf(stdout, "pm: vs %s\n",
		v6fmt(v6c2s(pvec[pmtab[s][s2].pstate])));
#endif

	/*****************************/
	/* advance the state machine */
	/*****************************/
	s = pmtab[s][s2].pstate;

    }

    return(s2);
}
