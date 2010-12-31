"""Tests for functions in tpm/astro.h.

:Author: Prasanth Nair
:Contact: prasanthhn@gmail.com
"""
# M6 precess_m(double j1, double j2, int pflag, int sflag);
# V6 aberrate(V6 p, V6 e, int flag);
# V6 azel2hadec(V6 v6, double latitude);
# V6 ecl2equ(V6 v6, double obl);
# V6 ellab(double tdt, V6 star, int flag);
# V6 equ2ecl(V6 v6, double obl);
# V6 equ2gal(V6 v6);
# V6 eterms(double ep);
# V6 fk425(V6 v);
# V6 fk524(V6 v);
# V6 gal2equ(V6 v6);
# V6 geod2geoc(double lon, double lat, double alt);
# V6 hadec2azel(V6 v6, double latitude);
# V6 ldeflect(V6 s, V6 e, int flag);
# V6 precess(double j1, double j2, V6 v6, int pflag);
# V6 proper_motion(V6 v6, double t, double t0);
# char *tpm_state(int state);
# double delta_AT(double utc);
# double eccentricity(double tdt);
# double eccentricity_dot(double tdt);
# double obliquity(double tdt);
# double obliquity_dot(double tdt);
# double refract(double zx, double refa, double refb, int flag);
# double refraction(double zobs, double lat, double alt,
#   double T, double P, double rh, double lambda, double eps);
# double solar_perigee(double tdt);
# double solar_perigee_dot(double tdt);
# double tdt2tdb(double tdt);
# double theta(double j1, double j2, int pflag);
# double thetadot(double j1, double j2, int pflag);
# double ut12gmst(double ut1);
# double zee(double j1, double j2, int pflag);
# double zeedot(double j1, double j2, int pflag);
# int tpm(V6 *pvec, int s1, int s2, double ep, double eq, TPM_TSTATE *tstate);
# void atm(double r, double *n, double *dndr);
# void evp(double tdb, V6 *v6b, V6 *v6h);
# void nutations(double tdt, double *delta_phi, double *delta_eps);
# void refco(double lat, double alt, double T, double P,
#  double rh, double lambda, double eps, double *refa, double *refb);
# void tpm_data(TPM_TSTATE *p, int flags);

if __name__ == '__main__':
    pass
