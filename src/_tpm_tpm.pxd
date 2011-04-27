# -*- coding: utf-8 -*-

# I have to repeat the following "tpm/vec.h" here, since the s_tstate
# structure uses some of these structures. Just saying "struct s_m3 nm"
# doesn't work, gives syntax error. And "s_v6 nm" results in the
# message: s_v6 is not declared.  The "tpm/tpm.h" file does not
# "#include tpm/vec.h". Perhaps that's why I have to include the
# definitions in that file here? The entire "tpm/vec.h" is declared in
# _tpm_vec.h. So from within Cython I will be using _tpm_vec.V3 and so
# on.
cdef extern from "tpm/vec.h":
    # vec.h #includes v3, v6, m3 and m6.
    # From v3.h.
    struct s_v3:
        int type
        double v[3]
 
    ctypedef s_v3 V3
 
    # From v6.h.
    struct s_v6:
        V3 v[2]
 
    ctypedef s_v6 V6
 
    int POS
    int VEL
 
    # From m3.h.
    struct s_m3:
        double m[3][3]
 
    ctypedef s_m3 M3
 
    # From m6.h
    struct s_m6:
        M3 m[2][2]
 
    ctypedef s_m6 M6

cdef extern from "tpm/tpm.h":
    # State names
    int TPM_S00
    int TPM_S01
    int TPM_S02
    int TPM_S03
    int TPM_S04
    int TPM_S05
    int TPM_S06
    int TPM_S07
    int TPM_S08
    int TPM_S09
    int TPM_S10
    int TPM_S11
    int TPM_S12
    int TPM_S13
    int TPM_S14
    int TPM_S15
    int TPM_S16
    int TPM_S17
    int TPM_S18
    int TPM_S19
    int TPM_S20
    int TPM_S21
    int N_TPM_STATES
    
    int TPM_T00 
    int TPM_T01
    int TPM_T02
    int TPM_T03
    int TPM_T04
    int TPM_T05
    int TPM_T06
    int TPM_T07
    int TPM_T08
    int TPM_T09
    int TPM_T10
    int TPM_T11
    int TPM_T12
    int TPM_T13
    int TPM_T14
    int TPM_T15
    int N_TPM_TRANS

    struct s_target:
        char *name # char name[BUFSIZ]
        int state
        double epoch
        double equinox
        double position[2]
        double offset[2]
        double motion[2]
        double parallax
        double speed

    ctypedef s_target TPM_TARGET

    int TARGET_FK4
    int TARGET_FK5 
    int TARGET_ECL
    int TARGET_GAL 
    int TARGET_APP_HADEC 
    int TARGET_OBS_HADEC 
    int TARGET_APP_AZEL
    int TARGET_OBS_AZEL
    int TARGET_OBS_WHAM
    int TARGET_HADEC
    int TARGET_TOP_AZEL

    struct s_boresight:
        double epoch
        double position[2]
        double offset[2]
        double motion[2]

    ctypedef s_boresight TPM_BORESIGHT

    struct s_tstate:
        double utc
        double delta_at
        double delta_ut
        double lon
        double lat
        double alt
        double xpole
        double ypole
        double T
        double P
        double H
        double wavelength
        
        double tai
        double tdt
        double tdb

        double obliquity
        double nut_lon
        double nut_obl
        s_m3 nm
        s_m6 pm

        double ut1
        double gmst
        double gast
        double last

        s_v6 eb
        s_v6 eh
        s_v6 obs_m
        s_v6 obs_t
        s_v6 obs_s
        
        double refa
        double refb
        
    ctypedef s_tstate TPM_TSTATE

    int TPM_INIT
    int TPM_FAST
    int TPM_MEDIUM
    int TPM_SLOW
    int TPM_REFRACTION
    int TPM_ALL

    struct s_pmcell:
        int ptrans
        int pstate

    ctypedef s_pmcell TPM_PMCELL
    


