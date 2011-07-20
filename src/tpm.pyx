cimport tpm_times 
cimport tpm_vec
cimport tpm_tpm
cimport tpm_astro

include "tpm_times.pxi"
include "tpm_vec.pxi"
include "tpm_tpm.pxi"
include "tpm_astro.pxi"


# Some functions that use features in TPM.
def nalpha(alpha, degrees=True):
    """Normalize angle in the x-y plane, i.e., longitudinal angle.

    Normalize angles to the range [0, 360.0) degrees or [0, 2π)
    radians. This is useful for longitudinal angles, such as right
    ascension and longitude.

    Parameters
    ----------
    alpha : float
        Angle in the x-y plane, such as RA and Longitude.
    degrees : bool
        If True then `alpha` is in degrees (default), else it is in radians.

    Returns
    -------
    nalpha : float
        Angle normalized into the range [0, 360) or [0, 2π).

    See also
    --------
    r2r, h2h
    
    Notes
    -----
    For normalizing `alpha` and `delta` in `V6S` or `V3SP`
    objects, use the `nalpha` and `ndelta` attributes; they store
    properly normalized values, taking into account the sign of `r`.
    This function is for situations were we have a scalar angle and
    don't want to create a `V6S` or `V6SP` object just for
    normalizing the angle.
    
    """
    if degrees:
        x = tpm_times.d2r(alpha)
        x = tpm_times.r2r(x)
        return tpm_times.r2d(x)
    else:
        return tpm_times.r2r(alpha)

def ndelta(delta, degrees=True):
    """Normalize angle out of the x-y plane, i.e., latitudinal angle.

    This function takes an angle and normalizes it into the range [-90,
    90] if it is in degrees and into the range [-π/2, π/2] if it is in
    radians. This is useful for angles such as declination and
    latitude.

    Parameters
    ----------
    alpha : float
        Angle out of the x-y plane such as Dec.
    degrees: bool
        If True then `alpha` in in degrees (default), else it is in radians.

    Returns
    -------
    ndelta : float
        Angle normalized into the range [-90, 90] or [-π/2, π/2].

    See also
    --------
    fmt_delta
    
    Notes
    -----
    For normalizing `alpha` and `delta` in `V6S` or `V3SP`
    objects, use the `nalpha` and `ndelta` attributes; they store
    properly normalized values, taking into account the sign of `r`.
    This function is for situations were we have a scalar angle and
    don't want to create a `V6S` or `V6SP` object just for
    normalizing the angle.
    
    """
    # Create a V3 object and pass it to the v3delta function.
    cdef tpm_vec.V3 v3
    v3.v[0] = 1.0
    v3.v[1] = tpm_times.M_PI # Can be any value.
    v3.v[2] =  tpm_times.d2r(delta) if degrees else delta
    if degrees:
        return tpm_times.r2d(tpm_vec.v3delta(v3))
    else:
        return tpm_vec.v3delta(v3)
