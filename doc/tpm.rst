============================
 Telescope Pointing Machine
============================


.. _SLALIB: http://www.starlink.rl.ac.uk/star/docs/sun67.htx/sun67.html
.. _NOVAS: http://www.usno.navy.mil/USNO/astronomical-applications/
    software-products/novas

Telescope Pointing Machine, TPM, is "a table-driven software state
machine that produces and reduces coordinates for the purpose of
pointing a telescope, but which is generally  applicable to any
astronomical coordinate application"[#TPMDef].

TPM can handle coordinate conversions between 21 different "states",
including galactic, ecliptic, equatorial and topocentric systems. It
performs both position and velocity transformations simultaneously,
using vector/matrix methods.

The accuracies attained by TPM are comparable to that attained with
SLALIB_ and NOVAS_.


.. Papers:
..   Explanatory Supplement
..   Yallop 1989 AJ 97 274
..   Kaplan 1989 AJ 97 1197
..   Aoki 1983 A&A 128 263

TPM uses vector and matrix formulations throughout and no conversions
are done back and forth between Cartesion and spherical
coordinates. The quantity used is a "state vector" and not merely a
position vector.

A **state** is a reference frame. A **state vector** is "a 6-element
vector whose elements specify the target's position and velocity"
[#STATEVEC]. A **target** is an object for which we want to perform
coordinate conversions. The state vector is formed from three position
coordinates and three velocity components, in either Cartesian or in
spherical form. Positions and velocities are in units of AU and
AU/day, repectively. In both forms, the state vector stores real 3D
positions, and not unit vectors; they are "true-length target
vectors".

Coordinate conversions is a 6D phase-space problem, instead of a 3D
position problem; for example, we get both geocentric position and
velocity, when converting barycentric state vector into geocentric
state vector. Similarly, proper motions in equatorial coordinates get
converted into proper motions in azimuth and elevation.


Table driven state machine

 All the knowledge of the program is encoded into the state table. The
 rows in the table denote the current state and the columns denote the
 destination state. The value in a cell specifies the next step, in
 the chain of several steps, that should be taken to get from the
 current state to the destination state. 

 The program starts in a particular state, and read the information in
 the cell formed by the row and the destination column .

 The information in this cell, tells the program what is the next step
 it should perform to get to the destination. It performs this step
 and updates the current state to the resultant state; this
 corresponds to a different row.

 In the next iteration, the program repeats this process to get to
 next state in its progression from the initial state to the
 destination state. Finally the state represented by the row becomes
 equal to that represented by the column and the program stops.

 Even while constructing this table, we need to know only the next
 step that needs to be performed and the state that results from that
 step. Specifically, we don't have to layout the whole path that needs
 to be taken to get from the initial state to the final state.

 The state machine implementation embodies the correct sequence of
 events for all possible transformations.

 A new state can be added to the table by providing the
 computationally nearest existing state and the transformations for
 forward and backward transitions. The new state automatically gets
 connected to all existing states.

 This is a multiple-pass state machine, i.e., given a starting state
 and end state, the table cell does not give a list of all
 transformations to be performed; it just gives the next
 transformation and the process needs to be repeated until the
 destination is reached. In the former method it will not be easy to
 add a new state to the machine, since for each combintation of the
 new state and the existing states, detailed steps will be needed to
 be stored in the machine.


What is a state?

 A state is a reference frame, defined using 30 (31?) quantities. 12
 of these are independent, i.e., must be provided by the user and the
 remaining 18(19) are calculated from the independent quantities.

 The state is defined by providing a time (in various systems),
 position and velocity of the observer (w.r.t several coordinate
 systems), parameters for conversion between the different coordinate
 systems (precession, nutation etc.,) and two quantites that affect
 observations namely, refraction and wavelength.

 In TPM, all the dependent parameters in a state can be calculated by
 calling one function tpm_data().

 The independent quantites are:

 Time related

 + UTC as a Julian date
 + DeltaAT = TAI - UTC
 + DeltaUT = UT1 - UTC

 Position related
 
 + polar motion in radians
 + east longitude, north latitude; negative for west and south;
   in radians
 + altitude in meters
 + temperature in K, pressure in millibars, relative humidity (0-1)

 Quantity that affects observations

 + Wavelength of observation


 The dependent quantities are:

 Dynamic time related

 + TAI

 + TDT

 + TDB

 Rotational time related

 + UT1

 + GMST

 + GAST 

 + LAST

 Position and velocity 

 + earth's helocentric and barycentric state vectors

 + observers's mean and true geocentric state vectors

 Coordinate system related

 + precession matrix for J2000 to mean date rotation of FK5

 + nutation matrix for mean to true date rotation of FK5
 
 + obliquity

 + nutation in obliquity

 + nutation in longitude

 Quantities affecting observations

 + refraction coefficients


ALl the 30(31) quantities can grouped into three categories based on
the time over which they change: fast (less thatn a second), medium
(minutes to hours) and slow (days to years). They can be divided into
three different categories based on how computational intensive the
calculations are: low (a few additions and multiplications), medium
(several trigonometric terms) and high (thousands of trigonometric
terms, numerical integrations, iterative procedures).

Quantities that change slowly turn out to be those that have high
computational cost and those that change fast have low conputational
costs. Using tpm_data(), we can decide which of these calculations
must be performed. For example, if we want to calculate positions of
bodies over a time period of a few seconds, we needn't perform
calculations for quantities that vary on time scales of several days.

Epoch and equinox

Epoch

  a point in time.

  In astrometry, the input quantity labelled epoch, is a time that is
  used to apply proper motion corrections to an given set of
  coordinates, so as to obtain the coordinates of the object, in the
  same coordinate system, at the time given by the epoch.
  

Equinox 

  direction of line of nodes between ecliptic and equator at an
  epoch. This direction is a function of time and hence a time can be
  specified instead of an angle: the angle can be calculated using
  precession and nutation matrices, for the given time.

So we say

  Equinox and epoch of J2000: position of an object at the time J2000,
  in the coordinate system defined by the line of nodes of equatorial
  and ecliptic planes on J2000.

  Equinox and epoch of 1950: the same as above for B1950

  Equinox J2000 epoch J2010: position of an object at the time J2010,
  in the coordinate system defined by the line of nodes of equatorial
  and ecliptic planes on J2000.


In TPM the equnox values used are:
  
  + User specified say, J2010
  + J2000
  + B1950


Epoch is used in applying proper motion to coordinates. TPM does
not apply proper motion corrections. So, why does TPM need epoch?

  The Fk4-Fk5 conversion must be carried out for coordinates at the
  epoch 1984 Jan1, in both coordinate systems.

  For +T05, the coordinates at the user epoch are first converted into
  epoch B1950 by applying PM, then the algorithm that does Fk4-Fk5
  converts coordinates to B1950 epoch 1984, and then converts to FK5
  i.e., J2000 epoch 1984. Then this is converted into user epoch J2000
  equinox.

  For -T05, the user epoch equinox J2000 coordinates is converted into
  epoch J2000 equinox J2000, by applying PM. Then converted into epoch
  1984 equinox J2000, again applying PM. Then into epoch 1984 equinox
  B1950. This is then converted, using applying PM coorections, into
  user epoch equinox B1950.

Apparent places: Different apparent places result from the amount of
corrections that have been applied in each case. For example,
historically, due to computational difficulties, abberation is split
into annual or geocentric abberationa and diurnal or topocentric
aberration. Application of only the former results in a different
apparent place from that obtained by applying both. With modern day
computers there is no need to make such distinctions.


State transformations

Rotation matrices, from Yallop.

Standard R_x, R_y and R_z.

Matrix Q_x, Q_y and Q_z: [r_1, r_dot_1] = Q [r_0, r_dot_0]





state vector: a position
epoch: epoch of the state vector

equinox: equinox of the state vector; only used to transform from
equinox of user supplied state vector to FK4 B1950 and FK5 J2000
equinoxes

pvec: construct an array, of length N_TPM_STATES, of state vectors
provide starting state vector in pvec[s1].  the transformed state
vector will be pvec[s2], others will contain the appropriate
intermediate state vectors.

construct the TPM state: the reference frame, including informations
such as longitude, latitude etc.

Set TPM state: intialize it; then perform the desired calculations
i.e., fast, slow, medium, all, refraction.

call tpm() with state vectors (pvec), epoch and equinox of the
starting state vector, starting state, final state, TPM state. 

User must apply proper motion using tpm.proper_motion, BEFORE invoking
the state machine.

.. rubric:: Footnotes

.. [#TPMDef] Page 5 of the TPM manual.
.. [#STATEVEC] Page 7 of the TPM manual.
