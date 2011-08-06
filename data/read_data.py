#Helper functions that return Numpy rec-array from the formatted data
#needed for performing tests.
import os
import csv

y = os.path.dirname(__file__)
y = os.path.join(y, "../pytpm/tests/data")
testdatadir = os.path.abspath(y)


def get_hipdata():
    """Return data in tests/data/hip_full.txt.

    The data was created with hip_full.py file.
    """
    f = open(os.path.join(testdatadir, "hip_full.txt"), "r")
    s = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC,
                   delimiter=" ", skipinitialspace=True)
    d = dict(ra_icrs=[], dec_icrs=[], px=[], pma=[], pmd=[],
             raj2=[], decj2=[], rab1=[], decb1=[], glon=[],
             glat=[], elon2=[], elat2=[])

    for i in s:
        d["ra_icrs"].append(i[0])
        d["dec_icrs"].append(i[1])
        d["px"].append(i[2])
        d["pma"].append(i[3])
        d["pmd"].append(i[4])
        d["raj2"].append(i[5])
        d["decj2"].append(i[6])
        d["rab1"].append(i[7])
        d["decb1"].append(i[8])
        d["glon"].append(i[9])
        d["glat"].append(i[10])
        d["elon2"].append(i[11])
        d["elat2"].append(i[12])

    f.close()
    return d


def get_ndwfs():
    """Return data in tests/data/ndwfs.txt as a dict.

    The data file was created with ndwfs.py.
    """
    f = open(os.path.join(testdatadir, "ndwfs.txt"), "r")
    s = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC,
                   delimiter=" ", skipinitialspace=True)
    d = dict(racj2=[], deccj2=[], raj2=[], decj2=[], rab1=[], decb1=[],
             glon=[], glat=[], elon2=[], elat2=[])

    for i in s:
        d["racj2"].append(i[0])
        d["deccj2"].append(i[1])
        d["raj2"].append(i[2])
        d["decj2"].append(i[3])
        d["rab1"].append(i[4])
        d["decb1"].append(i[5])
        d["glon"].append(i[6])
        d["glat"].append(i[7])
        d["elon2"].append(i[8])
        d["elat2"].append(i[9])

    f.close()
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
        f = open(os.path.join(testdatadir, filename), "r")
        tab = csv.reader(CommentedFile(f), quoting=csv.QUOTE_NONNUMERIC,
                         delimiter=" ", skipinitialspace=True)

        l = list(tab)
        f.close()
        return l
