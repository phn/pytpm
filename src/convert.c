#include "tpm/astro.h"

/* xo and y0 are in radians. */
void convert(double x0, double y0, int s1, int s2, 
             double epoch, double equinox, double timetag,
             double delta_ut,
             double lon, double lat, double alt,
             double x_pole, double y_pole, 
             double T, double P, double H, 
             double W,
             double *x1, double *y1){
    TPM_TSTATE tstate;
    V6 v6;
    V6 pvec[N_TPM_STATES];

    /* Initialize state vector */
    tpm_data(&tstate, TPM_INIT);

    /* Set values of some dependent variables */
    tstate.lon = d2r(lon);
    tstate.lat = d2r(lat);
    tstate.alt = alt;
    tstate.T = T;
    tstate.P = P;
    tstate.H = H;
    tstate.wavelength = W;
    tstate.utc = timetag;
    tstate.delta_ut = delta_ut;
    tstate.delta_at = delta_AT(timetag);
    tstate.xpole = x_pole;
    tstate.ypole = y_pole;
        
    tpm_data(&tstate, TPM_ALL);

    /* Set up position-velocity vector for the object */
    v6 = v6init(SPHERICAL);
    v6SetR(v6, 1e9);
    v6SetAlpha(v6, x0);
    v6SetDelta(v6, y0);
    pvec[s1] = v6s2c(v6);

    /* Call tpm tp perform conversion from state s1 to state s2 */
    tpm(pvec,s1,s2,epoch,equinox,&tstate);

    /* Extract ra/longitude and dec/latitude */
    v6 = v6c2s(pvec[s2]);
    *x1 = v6GetAlpha(v6);
    *y1 = v6GetDelta(v6);

    return;
}
/*
int main(int argc, char *argv){
    double x1=0;
    double y1=0;
    double timetag = 0;
    timetag = utc_now();
    convert(0,0,6,19,J2000,J2000,timetag,-111.598333,
                31.956389, 2093.093, 288.0, 1013.0, 0.5,0.55000,
                &x1, &y1);
    printf("%f %s %s\n", timetag, fmt_alpha(x1), fmt_delta(y1));

    return 0;
}*/
