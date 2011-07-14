cimport tpm_times 
cimport tpm_vec
cimport tpm_tpm
cimport tpm_astro

include "tpm_times.pxi"
include "tpm_vec.pxi"
include "tpm_tpm.pxi"
include "tpm_astro.pxi"


# Some functions that use features in TPM.
def nalpha(double alpha, degrees=True):
    """Normalize angle in the x-y plane, i.e., longitudinal angle.
    
    :param alpha: Angle in x-y plane such as RA.
    :type alpha: float
    :param degrees: True = alpha in degrees (default), False = radians.
    :type degrees: boolean
    
    :return: Angle normalized into the range [0, 360) or [0, 2π).
    :rtype: float

    The tpm.d2d() function returns angle normalized to (-360, 360). So
    to get an angle normalized to (0, 360) we need to convert angle
    into radians, perform this normalization and then convert back into
    degrees. This function accepts angle in degrees and performs these
    steps. This function also takes angle in radians if ``degrees ==
    False`` but in this it is the same as calling ``tpm.r2r()``.
    
    For normalizing ``alpha`` and ``delta`` in ``V6S`` or ``V3SP``
    objects, use the ``nalpha`` and ``ndelta`` attributes; they store
    properly normalized values, taking into account the sign of ``r``.
    This function is for situations were we have a scalar angle and
    don't want to create a ``V6S`` or ``V6SP`` object just for
    normalizing the angle.
    """
    if degrees:
        x = tpm_times.d2r(alpha)
        x = tpm_times.r2r(x)
        return tpm_times.r2d(x)
    else:
        return tpm_times.r2r(alpha)

def ndelta(double delta, degrees=True):
    """Normalize angle out of the x-y plane, i.e., latitudinal angle.
    
    :param alpha: Angle out of the x-y plane such as DEC.
    :type alpha: float
    :param degrees: True = alpha in degrees (default), False = radians.
    :type degrees: boolean
    
    :return: Angle normalized into the range [-90, 90] or [-π/2, π/2].
    :rtype: float

    This function takes an angle and normalizes it into the range [-90,
    90] if it is in degrees and into the range [-π/2, π/2] if it is in
    radians.
    
    For normalizing ``alpha`` and ``delta`` in ``V6S`` or ``V3SP``
    objects, use the ``nalpha`` and ``ndelta`` attributes; they store
    properly normalized values, taking into account the sign of ``r``.
    This function is for situations were we have a scalar angle and
    don't want to create a ``V6S`` or ``V6SP`` object just for
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
