# -*- coding: utf-8 -*-
# The following line must be present in the pytpm.pyx file.
# cimport _tpm_vec

POS = _tpm_vec.POS
VEL = _tpm_vec.VEL
CARTESIAN = _tpm_vec.CARTESIAN
SPHERICAL = _tpm_vec.SPHERICAL
POLAR = _tpm_vec.POLAR

cdef class V3(object):
    cdef _tpm_vec.V3 _v3
    cdef int _vtype
    
    def __cinit__(self):
        self._v3.type = CARTESIAN
        self._vtype = POS
        self._v3.v[0] = 0.0
        self._v3.v[1] = 0.0
        self._v3.v[2] = 0.0
        
    def __init__(self, **kwargs):
        self._v3.type = kwargs.get('ctype', CARTESIAN)
        self._vtype = kwargs.get('vtype', POS)
        if self._v3.type == CARTESIAN and self._vtype == POS:
            self._v3.v[0] = kwargs.get('x', 0.0)
            self._v3.v[1] = kwargs.get('y', 0.0)
            self._v3.v[2] = kwargs.get('z', 0.0)
        elif self._v3.type == CARTESIAN and self._vtype == VEL:
            self._v3.v[0] = kwargs.get('xdot', 0.0)
            self._v3.v[1] = kwargs.get('ydot', 0.0)
            self._v3.v[2] = kwargs.get('zdot', 0.0)
        elif self._v3.type == SPHERICAL and self._vtype == POS:
            self._v3.v[0] = kwargs.get('r', 0.0)
            self._v3.v[1] = kwargs.get('alpha', 0.0)
            self._v3.v[2] = kwargs.get('delta', 0.0)
        elif self._v3.type == SPHERICAL and self._vtype == VEL:
            self._v3.v[0] = kwargs.get('rdot', 0.0)
            self._v3.v[1] = kwargs.get('alphadot', 0.0)
            self._v3.v[2] = kwargs.get('deltadot', 0.0)

    cpdef _get_valid_keys(self):
        if self._v3.type == CARTESIAN and self._vtype == POS:
            return ('x', 'y', 'z', 'ctype', 'vtype')
        if self._v3.type == CARTESIAN and self._vtype == VEL:
            return ('xdot', 'ydot', 'zdot', 'ctype', 'vtype')
        if self._v3.type == SPHERICAL and self._vtype == POS:
            return ('r', 'alpha', 'delta', 'ctype', 'vtype')
        if self._v3.type == SPHERICAL and self._vtype == VEL:
            return ('rdot', 'alphadot', 'deltadot', 'ctype', 'vtype')
        
    def __getattr__(self, key):
        keys = self._get_valid_keys()
        if key not in keys:
            raise AttributeError, "No such property: {0}".format(key)
        if key == 'x' or key == 'xdot' or key == 'r' or key == 'rdot':
            return self._v3.v[0]
        if key == 'y' or key == 'ydot' or key== 'alpha' or \
                key == 'alphadot':
            return self._v3.v[1]
        if key == 'z' or key == 'zdot' or key == 'delta' or \
                key == 'deltadot':
            return self._v3.v[2]
        if key == 'ctype': return self._v3.type
        if key == 'vtype': return self._vtype
    
    def __setattr__(self, key, value):
        if key not in self._get_valid_keys():
            raise AttributeError, "No such property: {0}".format(key)
        if key == 'ctype' or key == 'vtype':
            raise TypeError, "Cannot change {0}".format(key)
        if key == 'x' or key == 'xdot' or key == 'r' or key == 'rdot':
            self._v3.v[0] = value
        if key == 'y' or key == 'ydot' or key== 'alpha' or \
                key == 'alphadot':
            self._v3.v[1] = value
        if key == 'z' or key == 'zdot' or key == 'delta' or \
                key == 'deltadot':
            self._v3.v[2] = value

    def __delattr__(self, key):
        raise TypeError, "Fields cannot be deleted."
        
