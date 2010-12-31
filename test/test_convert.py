"""Tests for the convert function.

Convert function uses TPM to convert coordinates from one system to 
another.

TODO: 

    #. Compare TPM and pytpm

    This is the most important test
    select a few coordinates from SIMBAD/NED
    perform various conversions with binary TPM program
    perform the same using pytpm
    compare results

    #. A comparison with JPL HORIZONS

    Do some conversions using JPL HORIZONS
    Do the same using pytpm and tpm
    compare results

"""
import pytpm
from pytpm import tpm
from pytpm import utils as tpmu

# Coordinates from SIMBAD
ngc1 = {'icrs': {'x': '00:07:15.825', 'y': '+27:42:29.13', 
                'ep': 2000, 'eq': None},
        'fk5': {'x': '00:07:15.825', 'y': '+27:42:29.13', 
                'ep': 2000, 'eq': 2000},
        'fk4': {'x': '00:04:41.15', 'y': '+27:25:47.3', 
                'ep': 1950, 'eq': 1950},
        'gal': {'x': 111.1073, 'y': -34.1473, 
                'ep': 2000, 'eq': None}
        }
# NGC1 coordinates in degrees
ngc1_d_fk5  = {'x': (00+07/60.0+15.825/3600.0)*15,
               'y': (27+42/60.0+29.13/3600.0)}
ngc1_d_fk4 = {'x': (00+04/60.0+41.15/3600.0)*15,
              'y': (27+25/60.0+47.3/3600.0)}
ngc1_d_gal = {'x': 111.1073, 'y': -34.1473}

# Results of conversion of ngc1 coordinates using TPM binary,
# with default KPNO coordinates and utc=2451545.0
ngc1_fk5fk4_tpm = {'x': "00H 04M 41.142S",
                 'y': "+27D 25' 47.556\""}
ngc1_fk4fk5_tpm = {'x': "00H 07M 15.832S",
               'y': "+27D 42' 28.873\""}
ngc1_fk5gal_tpm = {'x': "07H 24M 25.737S",
               'y': "-34D 08' 50.166\""}

def test_convert_fk4fk5():
    """fk4 to fk5 with pytpm.utils.convert and compare with tpm binary.
    """
    ngc1_fk4fk5_x, ngc1_fk4fk5_y = tpmu.convert(s1=5, s2=6,
                       x=ngc1_d_fk4['x'], y=ngc1_d_fk4['y'],
                       timetag=2451545.0)

    # Convert degrees into HMS and DMS strings
    x_out_hms = tpm.dms2hms(tpm.d2dms(ngc1_fk4fk5_x))
    x_out_hms = tpmu.fmt_hms(x_out_hms)
    y_out_dms = tpm.fmt_d(ngc1_fk4fk5_y)

    assert x_out_hms.strip() == ngc1_fk4fk5_tpm['x']
    assert y_out_dms.strip() == ngc1_fk4fk5_tpm['y']

def test_convert_fk5fk4():
    """fk5 to fk4 with pytpm.utils.convert and compare with tpm binary.
    """
    ngc1_fk5fk4_x, ngc1_fk5fk4_y = tpmu.convert(s1=6, s2=5,
                       x=ngc1_d_fk5['x'], y=ngc1_d_fk5['y'],
                       timetag=2451545.0)

    # Convert degrees into HMS and DMS strings
    x_out_hms = tpm.dms2hms(tpm.d2dms(ngc1_fk5fk4_x))
    x_out_hms = tpmu.fmt_hms(x_out_hms)
    y_out_dms = tpm.fmt_d(ngc1_fk5fk4_y)

    assert x_out_hms.strip() == ngc1_fk5fk4_tpm['x']
    assert y_out_dms.strip() == ngc1_fk5fk4_tpm['y']
    
def test_convert_fk5gal():
    """fk5 to galactic with pytpm.utils.convert and compare with tpm
    binary.
    """
    ngc1_fk5gal_x, ngc1_fk5gal_y = tpmu.convert(s1=6, s2=4,
                       x=ngc1_d_fk5['x'], y=ngc1_d_fk5['y'],
                       timetag=2451545.0)

    # Convert degrees into HMS and DMS strings
    x_out_hms = tpm.dms2hms(tpm.d2dms(ngc1_fk5gal_x))
    x_out_hms = tpmu.fmt_hms(x_out_hms)
    y_out_dms = tpm.fmt_d(ngc1_fk5gal_y)

    assert x_out_hms.strip() == ngc1_fk5gal_tpm['x']
    assert y_out_dms.strip() == ngc1_fk5gal_tpm['y']
    

# Now convert SIMBAD values from one system to another and compare
# with the SIMBAD values themselves.
def test_convert_simfk4fk5():
    """Convert from FK4-FK5 and compare with SIMBAD FK5 values."""
    ngc1_fk4fk5_x, ngc1_fk4fk5_y = tpmu.convert(s1=5, s2=6,
                      x=ngc1_d_fk4['x'], y=ngc1_d_fk4['y'],
                      timetag=2451545.0)
    # Convert degrees into HMS and DMS strings
    x_out_hms = tpm.dms2hms(tpm.d2dms(ngc1_fk4fk5_x))
    x_out_hms = tpmu.fmt_hms(x_out_hms)
    y_out_dms = tpm.fmt_d(ngc1_fk4fk5_y)

    # x_out_hms = 00H 07M 15.832S  x_simbad = 00:07:15.825
    # y_out_dms = +27D 42' 28.873" y_simbad = +27:42:29.13
    # So only accurate to the nearest arc-second
    assert "{0:.3f}".format(ngc1_fk4fk5_x) == \
           "{0:.3f}".format(ngc1_d_fk5['x'])
    assert "{0:.3f}".format(ngc1_fk4fk5_y) == \
           "{0:.3f}".format(ngc1_d_fk5['y'])

def test_convert_simfk5fk4():
    """Convert from FK5-FK4 and compare with SIMBAD FK4 values."""
    ngc1_fk5fk4_x, ngc1_fk5fk4_y = tpmu.convert(s1=6, s2=5,
                      x=ngc1_d_fk5['x'], y=ngc1_d_fk5['y'],
                      timetag=2451545.0)
    # Convert degrees into HMS and DMS strings
    x_out_hms = tpm.dms2hms(tpm.d2dms(ngc1_fk5fk4_x))
    x_out_hms = tpmu.fmt_hms(x_out_hms)
    y_out_dms = tpm.fmt_d(ngc1_fk5fk4_y)

    # Only accurate to the nearest arc-second
    assert "{0:.3f}".format(ngc1_fk5fk4_x) == \
           "{0:.3f}".format(ngc1_d_fk4['x'])
    assert "{0:.3f}".format(ngc1_fk5fk4_y) == \
           "{0:.3f}".format(ngc1_d_fk4['y'])

def test_convert_simfk5gal():
    """Convert from FK5-GAL and compare with SIMBAD GAL values."""
    ngc1_fk5gal_x, ngc1_fk5gal_y = tpmu.convert(s1=6, s2=4,
                      x=ngc1_d_fk5['x'], y=ngc1_d_fk5['y'],
                      timetag=2451545.0)
    # Convert degrees into HMS and DMS strings
    x_out_hms = tpm.dms2hms(tpm.d2dms(ngc1_fk5gal_x))
    x_out_hms = tpmu.fmt_hms(x_out_hms)
    y_out_dms = tpm.fmt_d(ngc1_fk5gal_y)

    # Only accurate to the nearest arc-second
    assert "{0:.3f}".format(ngc1_fk5gal_x) == \
           "{0:.3f}".format(ngc1_d_gal['x'])
    assert "{0:.3f}".format(ngc1_fk5gal_y) == \
           "{0:.3f}".format(ngc1_d_gal['y'])


if __name__ == "__main__":
    test_convert_fk4fk5()
    test_convert_fk5fk4()
    test_convert_fk5gal()
