import sys
sys.path.append("../")
from pytom import tpm
from pytom import utils as tpm_utils
import os
print 
print "Converting coordinates 0 RA 0 DEC (FK5 J2000)"
print "to Azimuth and Elevation (present epoch)"
print "for Kitt Peak National Observatory location"
print "using default settings."
print
print "From tpm binary: "
x = os.system('tpm')
if x != 0:
    print "TPM executable not found."
a,b = tpm_utils.convert()
print "From pytpm: "
print "%.6f"%tpm.utc_now(),tpm.fmt_alpha(a), tpm.fmt_delta(b)

