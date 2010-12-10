from pytpm import tpm

def print_matrix_string(m_string,rows,cols):
    """Split string into rows and columns."""
    l = m_string.split()
    temp = ["  "]
    for i in range(cols):
        s = "{0:02d}".format(i)
        s = s.center(21)
        temp.append(s)

    print " ".join(temp)
    for i in range(rows):
        s = "{0:02d}".format(i)
        print " ".join([s]+l[i*cols:(i*cols)+cols])

def print_state(tpm_tstate):
    """Print contents of TPM state vector."""
    print "\n*************** Independent properties **********************\n"
    print "UTC (Julian date)      : {0:15.8f}".format(tpm_tstate.utc)
    print "Delta AT (s)           : {0:15.8f}".format(tpm_tstate.delta_at)
    print "Delta UT (s)           : {0:15.8f}".format(tpm_tstate.delta_ut)            
    print "Latitude (rad)         : {0:15.8f}".format(tpm_tstate.lat)            
    print "Longitude (rad)        : {0:15.8f}".format(tpm_tstate.lon)                 
    print "Polar motion x (rad)   : {0:15.8f}".format(tpm_tstate.xpole)
    print "Polar motion y (rad)   : {0:15.8f}".format(tpm_tstate.ypole)
    print "Altitude (meters)      : {0:15.8f}".format(tpm_tstate.alt)
    print "Humidity (0-1)         : {0:15.8f}".format(tpm_tstate.H)             
    print "Pressure (milli-bars)  : {0:15.8f}".format(tpm_tstate.P)                    
    print "Temperature (Kelvin)   : {0:15.8f}".format(tpm_tstate.T)                    
    print "Wavelength (microns)   : {0:15.8f}".format(tpm_tstate.wavelength)
     
    print "\n*************** Dependent properties ************************\n"
    print "UT1 (s)                : {0:15.8f}".format(tpm_tstate.ut1)
    print "GAST (Julian date)     : {0:15.8f}".format(tpm_tstate.gast)                 
    print "GMST (Julian date)     : {0:15.8f}".format(tpm_tstate.gmst)                 
    print "LAST (Julian date)     : {0:15.8f}".format(tpm_tstate.last)                 
    print "TAI (Julian date)      : {0:15.8f}".format(tpm_tstate.tai)      
    print "TDB (Julian date)      : {0:15.8f}".format(tpm_tstate.tdb)        
    print "TDT (Julian date)      : {0:15.8f}".format(tpm_tstate.tdt)
    print "Obliquity (rad)        : {0:15.8f}".format(tpm_tstate.obliquity)
    print "Nutation in longitude  : {0:15.8f}".format(tpm_tstate.nut_lon)
    print "Nutation in obliquity  : {0:15.8f}".format(tpm_tstate.nut_obl)
    print "Refraction coeff. A    : {0:15.8f}".format(tpm_tstate.refa)
    print "Refraction coeff. B    : {0:15.8f}".format(tpm_tstate.refb)
    print "\nBarycentric Earth state vector\n"
    s = tpm.v6fmt(tpm_tstate.eb)
    print_matrix_string(s, 1, 6)
    print "\nHeliocentric Earth state vector\n"
    s = tpm.v6fmt(tpm_tstate.eh)
    print_matrix_string(s, 1, 6)
    print "\nGeometric Earth-fixed state vector, mean state\n"
    s = tpm.v6fmt(tpm_tstate.obs_m)
    print_matrix_string(s, 1, 6)
    print "\nGeometric Earth-fixed state vector, true state\n"
    s = tpm.v6fmt(tpm_tstate.obs_t)
    print_matrix_string(s, 1, 6)
    print "\nGeometric Space-fixed state vector, mean state\n"
    s = tpm.v6fmt(tpm_tstate.obs_s)
    print_matrix_string(s, 1, 6)
    print "\nPrecession matrix (J2000 to UTC)\n"
    s = tpm.m6fmt(tpm_tstate.pm)
    print_matrix_string(s, 6, 6)
    print "\nNutation matrix for UTC\n"
    s = tpm.m3fmt(tpm_tstate.nm)
    print_matrix_string(s, 3, 3)

