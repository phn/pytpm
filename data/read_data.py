#Helper functions that return Numpy rec-array from the formatted data
#needed for performing tests.
import os
import csv
import numpy as np
import sys

# I want to run these without having to install PyTPM.
sys.path.append("..")
from pytpm import tpm, convert

y = os.path.dirname(__file__)
y = os.path.join(y, "../pytpm/tests/data")
testdatadir = os.path.abspath(y)


def get_hipdata():
    """Return data in tests/data/hip_full.txt.

    The data was created with hip_full.py file.
    """
    f = os.path.join(testdatadir, "hip_full.txt")
    dtype = [('ra_icrs', np.float64), ('dec_icrs', np.float64),
             ('px', np.float64), ('pma', np.float64), ('pmd', np.float64),
             ('raj2', np.float64), ('decj2', np.float64),
             ('rab1', np.float64), ('decb1', np.float64),
             ('glon', np.float64), ('glat', np.float64),
             ('elon2', np.float64), ('elat2', np.float64)
             ]
    d = np.loadtxt(f, dtype=dtype)

    d['ra_icrs'] = np.radians(d['ra_icrs'])
    d['dec_icrs'] = np.radians(d['dec_icrs'])
    d['raj2'] = np.radians(d['raj2'])
    d['decj2'] = np.radians(d['decj2'])
    d['rab1'] = np.radians(d['rab1'])
    d['decb1'] = np.radians(d['decb1'])
    d['glon'] = np.radians(d['glon'])
    d['glat'] = np.radians(d['glat'])
    d['elon2'] = np.radians(d['elon2'])
    d['elat2'] = np.radians(d['elat2'])

    # milli-arc-sec/jul yr to arc-sec per Jul. cent. And take out cos.
    d['pma'] = d['pma'] / np.cos(d['decj2']) / 1000.0 * 100.0
    d['pmd'] = d['pmd'] / 1000.0 * 100.0

    # milli-arsec to arc-sec
    d['px'] /= 1000.0

    return d


def cat2array(cat):
    dtype = [('alpha', np.float64), ('delta', np.float64),
             ('pma', np.float64), ('pmd', np.float64),
             ('px', np.float64), ('rv', np.float64)]
    d = np.array([(tpm.r2r(i['alpha']), i['delta'], i['pma'], i['pmd'],
                   i['px'], i['rv']) for i in cat],
                 dtype=dtype)

    return d


def get_ndwfs():
    """Return data in tests/data/ndwfs.txt as a dict.

    The data file was created with ndwfs.py.
    """
    f = os.path.join(testdatadir, "ndwfs.txt")
    dtype = [('racj2', np.float64), ('deccj2', np.float64),
             ('raj2', np.float64), ('decj2', np.float64),
             ('rab1', np.float64), ('decb1', np.float64),
             ('glon', np.float64), ('glat', np.float64),
             ('elon2', np.float64), ('elat2', np.float64)
             ]
    d = np.loadtxt(f, dtype=dtype)

    d['racj2'] = np.radians(d['racj2'])
    d['deccj2'] = np.radians(d['deccj2'])
    d['raj2'] = np.radians(d['raj2'])
    d['decj2'] = np.radians(d['decj2'])
    d['rab1'] = np.radians(d['rab1'])
    d['decb1'] = np.radians(d['decb1'])
    d['glon'] = np.radians(d['glon'])
    d['glat'] = np.radians(d['glat'])
    d['elon2'] = np.radians(d['elon2'])
    d['elat2'] = np.radians(d['elat2'])

    return d


class CommentedFile(object):
    def __init__(self, f, commentstring="#"):
        self.f = f
        self.commentstring = commentstring

    def next(self):
        line = self.f.next()
        while line.startswith(self.commentstring):
            line = self.f.next()
        return line

    def __iter__(self):
        return self


def get_sla(filename):
    """SLALIB ouput can have different columns."""
    f = open(os.path.join(testdatadir, filename), "r")
    tab = csv.reader(CommentedFile(f), quoting=csv.QUOTE_NONNUMERIC,
                     delimiter=" ", skipinitialspace=True)

    l = np.array(list(tab), dtype=np.float64)
    f.close()
    return l
