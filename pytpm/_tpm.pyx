cimport tpmc

# Export constants.

M_PI = tpmc.M_PI
MJD_0 = tpmc.MJD_0
B1950 = tpmc.B1950
J2000 = tpmc.J2000
J1984 = tpmc.J1984
CB = tpmc.CB
CJ = tpmc.CJ
SUNDAY  = tpmc.SUNDAY
MONDAY  = tpmc.MONDAY
TUESDAY = tpmc.TUESDAY
WEDNESDAY = tpmc.WEDNESDAY
THURSDAY =  tpmc.THURSDAY
FRIDAY  =   tpmc.FRIDAY
SATURDAY =  tpmc.SATURDAY

POS = tpmc.POS
VEL = tpmc.VEL
CARTESIAN = tpmc.CARTESIAN
SPHERICAL = tpmc.SPHERICAL
POLAR = tpmc.POLAR

TPM_S00 = tpmc.TPM_S00     
TPM_S01 = tpmc.TPM_S01   
TPM_S02 = tpmc.TPM_S02   
TPM_S03 = tpmc.TPM_S03   
TPM_S04 = tpmc.TPM_S04   
TPM_S05 = tpmc.TPM_S05   
TPM_S06 = tpmc.TPM_S06   
TPM_S07 = tpmc.TPM_S07   
TPM_S08 = tpmc.TPM_S08
TPM_S09 = tpmc.TPM_S09   
TPM_S10 = tpmc.TPM_S10   
TPM_S11 = tpmc.TPM_S11   
TPM_S12 = tpmc.TPM_S12   
TPM_S13 = tpmc.TPM_S13   
TPM_S14 = tpmc.TPM_S14   
TPM_S15 = tpmc.TPM_S15   
TPM_S16 = tpmc.TPM_S16   
TPM_S17 = tpmc.TPM_S17   
TPM_S18 = tpmc.TPM_S18   
TPM_S19 = tpmc.TPM_S19     
TPM_S20 = tpmc.TPM_S20     
TPM_S21 = tpmc.TPM_S21     
N_TPM_STATES = tpmc.N_TPM_STATES

TPM_T00 = tpmc.TPM_T00 
TPM_T01 = tpmc.TPM_T01    
TPM_T02 = tpmc.TPM_T02    
TPM_T03 = tpmc.TPM_T03    
TPM_T04 = tpmc.TPM_T04    
TPM_T05 = tpmc.TPM_T05    
TPM_T06 = tpmc.TPM_T06    
TPM_T07 = tpmc.TPM_T07    
TPM_T08 = tpmc.TPM_T08    
TPM_T09 = tpmc.TPM_T09    
TPM_T10 = tpmc.TPM_T10    
TPM_T11 = tpmc.TPM_T11    
TPM_T12 = tpmc.TPM_T12    
TPM_T13 = tpmc.TPM_T13    
TPM_T14 = tpmc.TPM_T14    
TPM_T15 = tpmc.TPM_T15    
N_TPM_TRANS = tpmc.N_TPM_TRANS

TARGET_FK4 = tpmc.TARGET_FK4 
TARGET_FK5 = tpmc.TARGET_FK5      
TARGET_ECL = tpmc.TARGET_ECL      
TARGET_GAL = tpmc.TARGET_GAL      
TARGET_APP_HADEC = tpmc.TARGET_APP_HADEC 
TARGET_OBS_HADEC = tpmc.TARGET_OBS_HADEC
TARGET_APP_AZEL  = tpmc.TARGET_APP_AZEL 
TARGET_OBS_AZEL  = tpmc.TARGET_OBS_AZEL 
TARGET_OBS_WHAM  = tpmc.TARGET_OBS_WHAM
TARGET_HADEC     = tpmc.TARGET_HADEC 
TARGET_TOP_AZEL  = tpmc.TARGET_TOP_AZEL 

TPM_INIT   = tpmc.TPM_INIT 
TPM_FAST   = tpmc.TPM_FAST   
TPM_MEDIUM = tpmc.TPM_MEDIUM   
TPM_SLOW   = tpmc.TPM_SLOW   
TPM_REFRACTION = tpmc.TPM_REFRACTION
TPM_ALL = tpmc.TPM_ALL

IAU_K = tpmc.IAU_K
IAU_DM = tpmc.IAU_DM
IAU_AU = tpmc.IAU_AU
IAU_C  = tpmc.IAU_C
IAU_RE = tpmc.IAU_RE
IAU_RM = tpmc.IAU_RM
IAU_F  = tpmc.IAU_F
IAU_KAPPA = tpmc.IAU_KAPPA
IAU_W   = tpmc.IAU_W
GAL_RA  = tpmc.GAL_RA
GAL_DEC = tpmc.GAL_DEC
GAL_LON = tpmc.GAL_LON
PRECESS_NEWCOMB    = tpmc.PRECESS_NEWCOMB
PRECESS_ANDOYER    = tpmc.PRECESS_ANDOYER
PRECESS_KINOSHITA  = tpmc.PRECESS_KINOSHITA
PRECESS_LIESKE     = tpmc.PRECESS_LIESKE
PRECESS_FK4        = tpmc.PRECESS_FK4
PRECESS_FK5        = tpmc.PRECESS_FK5
PRECESS_INERTIAL   = tpmc.PRECESS_INERTIAL
PRECESS_ROTATING   = tpmc.PRECESS_ROTATING


def byear2jd(double x):
    return tpmc.BYEAR2JD(x)

def fmt_alpha(double x):
    return tpmc.fmt_alpha(x)

def fmt_delta(double x):
    return tpmc.fmt_delta(x)


def tpm_gal():
    cdef tpmc.V6 v6 = tpmc.v6init(tpmc.SPHERICAL)
    cdef tpmc.V6 pvec[21]
    cdef tpmc.TPM_TSTATE tstate;

    v6.v[POS].v[0] = 1e9
    v6.v[POS].v[1] = tpmc.d2r(6.4738)
    v6.v[POS].v[2] = tpmc.d2r(50.5456)


    pvec[TPM_S04] = v6 
    tpmc.tpm(pvec, TPM_S04, TPM_S05, B1950, B1950, &tstate)

    v6 = tpmc.v6c2s(pvec[TPM_S05])
    return (v6.v[POS].v[1], v6.v[POS].v[2])


def tpm_pre():
    cdef tpmc.V6 v6 = tpmc.v6init(tpmc.SPHERICAL)
    cdef tpmc.V6 pvec[21]
    cdef tpmc.TPM_TSTATE tstate;

    tpmc.tpm_data(&tstate, TPM_INIT)
    tstate.utc = tpmc.utc_now()
    tpmc.tpm_data(&tstate, TPM_ALL)

    v6.v[POS].v[0] = 1e9
    v6.v[POS].v[1] = tpmc.d2r(10.0)
    v6.v[POS].v[2] = tpmc.d2r(10.0)   

    pvec[TPM_S14] = v6 

    tpmc.tpm(pvec, TPM_S14, TPM_S15, J2000, J2000, &tstate)

    v6 = tpmc.v6c2s(pvec[TPM_S15])
    
    return (v6.v[POS].v[1], v6.v[POS].v[2]) 