============================================
 Coordinate conversions using TPM and PyTPM
============================================

Please read the TPM manual to learn more about TPM. Here I will only
give a overview of the way TPM performs coordinate conversions.

.. contents::

In TPM all the information needed to perform coordinate transformations
are stored in a ``TPM_TSTATE`` structure. This **state data structure**
stores time information, observers location and other data. Not all
data stored in this data structure are needed for all conversions.

Each coordinate system defined in TPM is called a **state**. There are 21
different states in TPM, each identified by an integer from 1 to 21.

The actual coordinates used are stored as vectors with 6 components (a
6-vector or a **state vector**): three position and three velocity
components. Internally, all vectors are in Cartesian coordinates. But
for input and output spherical vectors are also used.

The set of steps needed to perform a particular conversion are stored
in a **look up table**. Each rows of this table stands for a starting
state and a column stands for a final start. Each cell in the table
holds two pieces of information. First, the **next step** that must be
performed to get from the starting state indicated by the row to that
indicated by the column. Second the **resulting state** after this step
is performed. If the resulting state matches the final state then we
are done. Otherwise, the resulting state will become the new starting
state. We can then look up the cell in the row for this new state and
the column for the original final state. This is repeated until the
current state and the final state are the same.

TPM has a function, ``tpm``, that can perform this look up and perform
the indicated steps. It takes an array of 6-vectors, a starting state,
a final state, an epoch, an equinox and a state data structure. The
starting and end states are integers. This function will take these
information and the information stored in the look up table, and
perform the coordinate transformations.

The 6-vectors corresponding to the input and output coordinates are
stored in the array of 6-vectors.  If we want to perform a conversion
from state ``s1`` to state ``s2`` then the input 6-vector must be in
the index position ``s1``, and the final result will be stored in the
index position ``s2``.

For example, the FK5 epoch and equinox J2000 state is indicated by the
integer constant ``TPM_S06``, which is equal to 6, and the Galactic
coordinate system is indicated by the integer constant ``TPM_S04``,
which is equal to 4. So to perform the conversion from the former to
the latter, we would store the 6-vector for the FK5 coordinate at index
``TPM_S06``. After calling the function ``tpm``, we will extract the
6-vector for the Galactic coordinates from index ``TPM_S04``.

The general steps involved are: create a ``TPM_TSTATE`` structure, set
the various independent parameters and calculate the dependent
parameters. Create a 6-vector for the input coordinates and insert it
at the appropriate position in a array of 6-vectors. Then call the
``tpm`` function with the required information. After successful
completion extract the 6-vector for the output coordinates from the
appropriate position in the array of 6-vectors.

Also, the result from each intermediate step indicated by the look up
table is also stored in appropriate locations in the array of
6-vectors.

All these steps can be performed in PyTPM.

The following code takes the FK5 equinox and epoch J2000.0 coordinates
of M100 through all coordinate systems defined in TPM. C code using the
TPM library and Python code, for the equivalent conversion, using the
PyTPM library are both show. The code is also available in
:download:`examples/conversion_example.c` and
:download:`examples/conversion_example.py`, respectively.

C code
======

.. code-block:: c

  #include "tpm/astro.h"
  #include <stdio.h>
  #include <math.h>
   
  /* Take a coordinate through all states. */
  /* Coordinates for M100 from SIMBAD. */
   
  int main(){
    double ra = (12+22/60.0+54.899/3600.0) * (2*M_PI/24.0);
    double de = (15+49/60.0+20.57/3600.0) * (2*M_PI/360.0);
    double ra1, ra1_d, de1, de1_d;
    double ep = J2000;
    double eq = J2000;
    V6 v6;
    V6 pvec[N_TPM_STATES];
    TPM_TSTATE tstate;
    int s1 = TPM_S06; /* Heliocentric mean J2000 FK5 ~~ ICRS */
    int s2 = TPM_S00; /* Assign required states. */
   
    for(int i=TPM_S00; i < N_TPM_STATES; i ++){
      tpm_data(&tstate, TPM_INIT);
      tstate.utc = J2000;
      tstate.lon = d2r(-111.598333);
      tstate.lat = d2r(31.956389);
      tstate.alt = 2093.093;
      tstate.delta_ut = delta_UT(tstate.utc);
      tpm_data(&tstate, TPM_ALL);
       
      v6 = v6init(SPHERICAL);
      v6SetR(v6, 1e9);
      v6SetAlpha(v6, ra);
      v6SetDelta(v6, de);
       
      pvec[s1] = v6s2c(v6);
      s2 = i;
      tpm(pvec, s1, s2, ep, eq, &tstate);
      v6 = v6c2s(pvec[s2]);
       
      ra1 = v6GetAlpha(v6);
      de1 = v6GetDelta(v6);
      ra1_d = r2d(ra1);
      if (ra1_d < 0.0) ra1_d += 360.0;
      de1_d = r2d(de1);
      if (de1_d < 0.0) de1_d += 360.0;
   
      printf("%02d-%02d %-17s %s %s %8.4f %8.4f\n", s1, s2, 
        tpm_state(s2), fmt_alpha(ra1), fmt_delta(de1), ra1_d, de1_d);
    }
    return 0;
  }


.. _pytpm-full-conversion:

PyTPM code
==========

.. code-block:: python

  # Take coordinates of M100 through all states.
  from pytpm import tpm
   
  ra = tpm.h2r(12+22/60.0+54.899/3600.0)
  de = tpm.d2r(15+49/60.0+20.57/3600.0)
  ep = tpm.J2000
  eq = tpm.J2000
  s1 = tpm.TPM_S06
  s2 = tpm.TPM_S00
  tstate = tpm.TSTATE()
  pvec = tpm.PVEC()
   
  for i in range(tpm.N_TPM_STATES):
      tpm.tpm_data(tstate, tpm.TPM_INIT)
      tstate.utc = tpm.J2000
      tstate.lon = tpm.d2r(-111.598333)
      tstate.lat = tpm.d2r(31.956389)
      tstate.alt = 2093.093
      tstate.delta_ut = tpm.delta_UT(tstate.utc)
      tpm.tpm_data(tstate, tpm.TPM_ALL)
   
      v6 = tpm.V6S()
      v6.r = 1e9
      v6.alpha = ra
      v6.delta = de
      
   
      pvec[s1] = v6.s2c()
      s2 = i
      tpm.tpm(pvec, s1, s2, ep, eq, tstate)
      v6 = pvec[s2].c2s()
   
      ra1 = v6.alpha
      de1 = v6.delta
      ra1_d = tpm.r2d(ra1)
      if ra1_d < 0.0 : ra1_d += 360.0
      de1_d = tpm.r2d(de1)
      if de1_d < 0.0 : de1_d += 360.0
   
      s = "{0:02d}-{1:02d} {2:<17s} {3:s} {4:s} {5:8.4f} {6:8.4f}"
      print s.format(s1, s2, tpm.tpm_state(s2),
                     tpm.fmt_alpha(ra1), tpm.fmt_delta(de1), ra1_d,
                     de1_d)

      
We create a state structure, **tstate**, and initialize it by calling
``tpm_data()`` with ``TPM_INIT``. Then we assign values to independent
parameters of the state data structure. We then calculate all dependent
state properties by calling ``tpm_data()`` and passing ``TPM_ALL``. We
then create an array of ``V6`` vectors, ``pvec``, create a ``V6``
vector for our object, and assign it to the desired location in the
array, based on the starting state. We then call ``tpm()`` with the
state structure and the array of ``V6`` vectors, along with the
starting and ending state numbers. Finally we retrieve the appropriate
``V6`` vector from the array, which will give us the final coordinates.

         
The result from running the above code is given below::

 06-00 null               12H 22M 54.898S +15D 49' 20.570" 185.7287  15.8224
 06-01 Helio. mean FK4    12H 22M 54.824S +15D 49' 20.447" 185.7284  15.8223
 06-02 Helio. mean FK5    12H 22M 54.898S +15D 49' 20.570" 185.7287  15.8224
 06-03 IAU 1980 Ecliptic  11H 55M 07.815S +16D 45' 34.920" 178.7826  16.7597
 06-04 IAU 1958 Galactic  18H 04M 32.673S +76D 53' 55.928" 271.1361  76.8989
 06-05 Helio. mean FK4    12H 20M 22.935S +16D 05' 58.024" 185.0956  16.0995
 06-06 Helio. mean FK5    12H 22M 54.898S +15D 49' 20.570" 185.7287  15.8224
 06-07 Geoc. mean FK5     12H 22M 54.899S +15D 49' 20.569" 185.7287  15.8224
 06-08 S07 + Light Defl.  12H 22M 54.898S +15D 49' 20.571" 185.7287  15.8224
 06-09 S08 + Aberration   12H 22M 54.995S +15D 49' 13.474" 185.7291  15.8204
 06-10 S09 + Precession   12H 22M 54.995S +15D 49' 13.474" 185.7291  15.8204
 06-11 Geoc. app. FK5     12H 22M 54.045S +15D 49' 19.561" 185.7252  15.8221
 06-12 Topo. mean FK5     12H 22M 54.899S +15D 49' 20.569" 185.7287  15.8224
 06-13 S12 + Light Defl.  12H 22M 54.898S +15D 49' 20.571" 185.7287  15.8224
 06-14 S13 + Aberration   12H 22M 55.013S +15D 49' 13.452" 185.7292  15.8204
 06-15 S14 + Precession   12H 22M 55.013S +15D 49' 13.452" 185.7292  15.8204
 06-16 Topo. app. FK5     12H 22M 54.063S +15D 49' 19.539" 185.7253  15.8221
 06-17 Topo. app. HA/Dec  22H 52M 35.524S +15D 49' 19.539" 343.1480  15.8221
 06-18 Topo. app. Az/El   08H 50M 11.837S +67D 45' 09.683" 132.5493  67.7527
 06-19 Topo. obs. Az/El   08H 50M 11.837S +67D 45' 34.371" 132.5493  67.7595
 06-20 Topo. obs. HA/Dec  22H 52M 36.636S +15D 49' 38.307" 343.1527  15.8273
 06-21 Topo. obs. WHAM    22H 52M 56.457S -14D 49' 46.993" 343.2352 345.1703


For more details on TPM library see the TPM manual.

..  LocalWords:  PyTPM TPM LocalWords
