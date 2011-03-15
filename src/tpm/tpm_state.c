/* file: $RCSfile: tpm_state.c,v $
** rcsid: $Id: tpm_state.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: tpm_state.c,v $
** map telescope pointing machine states onto state names
** *******************************************************************
*/

#include "astro.h"

static char *statenames[N_TPM_STATES] = {
	"null",			/* TPM_S00 */
	"Helio. mean FK4",	/* TPM_S01 */
	"Helio. mean FK5",	/* TPM_S02 */
	"IAU 1980 Ecliptic",	/* TPM_S03 */
	"IAU 1958 Galactic",	/* TPM_S04 */
	"Helio. mean FK4",	/* TPM_S05 */
	"Helio. mean FK5",	/* TPM_S06 */
	"Geoc. mean FK5",	/* TPM_S07 */
	"S07 + Light Defl.",	/* TPM_S08 */
	"S08 + Aberration",	/* TPM_S09 */
	"S09 + Precession",	/* TPM_S10 */
	"Geoc. app. FK5",	/* TPM_S11 */
	"Topo. mean FK5",	/* TPM_S12 */
	"S12 + Light Defl.",	/* TPM_S13 */
	"S13 + Aberration",	/* TPM_S14 */
	"S14 + Precession",	/* TPM_S15 */
	"Topo. app. FK5",	/* TPM_S16 */
	"Topo. app. HA/Dec",	/* TPM_S17 */
	"Topo. app. Az/El",	/* TPM_S18 */
	"Topo. obs. Az/El",	/* TPM_S19 */
	"Topo. obs. HA/Dec",	/* TPM_S20 */
	"Topo. obs. WHAM"	/* TPM_S21 */
};

char *
tpm_state(int state)
{
    char *name;
    static char buf[BUFSIZ];

    if ((state < 0) || (state >= N_TPM_STATES)) {
	(void)sprintf(buf, "%s (S%02d)", "unknown", state);
	name = &buf[0];
    } else {
	name = statenames[state];
    }

    return(name);
}
