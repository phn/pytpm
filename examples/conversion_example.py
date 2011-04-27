# Take coordinates of M100 through all states.
from pytpm import tpm

ra = tpm.h2r(12+22/60.0+54.899/3600.0)
de = tpm.d2r(15+49/60.0+20.57/3600.0)
ep = tpm.J2000
eq = tpm.J2000
s1 = tpm.TPM_S06
s2 = tpm.TPM_S00
tstate = tpm.TSTATE()
pvec = tpm.PVEC()

for i in range(tpm.N_TPM_STATES):
    tpm.tpm_data(tstate, tpm.TPM_INIT)
    tstate.utc = tpm.J2000
    tstate.lon = tpm.d2r(-111.598333)
    tstate.lat = tpm.d2r(31.956389)
    tstate.alt = 2093.093
    tstate.delta_ut = tpm.delta_UT(tstate.utc)
    tpm.tpm_data(tstate, tpm.TPM_ALL)

    v6 = tpm.V6S()
    v6.r = 1e9
    v6.alpha = ra
    v6.delta = de
    

    pvec[s1] = v6.s2c()
    s2 = i
    tpm.tpm(pvec, s1, s2, ep, eq, tstate)
    v6 = pvec[s2].c2s()

    ra1 = v6.alpha
    de1 = v6.delta
    ra1_d = tpm.r2d(ra1)
    if ra1_d < 0.0 : ra1_d += 360.0
    de1_d = tpm.r2d(de1)
    if de1_d < 0.0 : de1_d += 360.0

    s = "{0:02d}-{1:02d} {2:<17s} {3:s} {4:s} {5:8.4f} {6:8.4f}"
    print s.format(s1, s2, tpm.tpm_state(s2),
                   tpm.fmt_alpha(ra1), tpm.fmt_delta(de1), ra1_d,
                   de1_d)
    
