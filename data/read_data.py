#Helper functions that return Numpy rec-array from the formatted data
#needed for performing tests.
import os
import csv

y = os.path.dirname(__file__)
y = os.path.join(y, "../pytpm/tests/data")
testdatadir = os.path.abspath(y)
    
def get_hipdata():
    """Return data in tests/data/hip_format.txt as recarray.

    The data was created with hip_format.py file.
    """
    f = open(os.path.join(testdatadir,"hip_formatted.txt"),"r")
    #dt = [('ra_icrs', np.float64),('dec_icrs', np.float64),
    #      ('px',np.float64),
    #      ('pma', np.float64), ('pmd', np.float64),
    #      ('ra_j2000', np.float64), ('dec_j2000', np.float64),
    #      ('ra_b1950', np.float64), ('dec_b1950', np.float64),
    #      ('glon',np.float64), ('glat', np.float64),
    #      ('elon_2000', np.float64), ('elat_2000', np.float64)]
    #tab = np.loadtxt(f,dtype=dt)
    #return tab

def get_ndwfs():
    """Return data in tests/data/ndwfs.txt as a dict.

    The data file was created with ndwfs.py.
    """
    f = open(os.path.join(testdatadir,"ndwfs.txt"),"r")
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
        
    return d


