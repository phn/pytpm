# -*- coding: utf-8 -*-
cdef extern from "tpm/vec.h":
    # vec.h #includes v3, v6, m3 and m6.
    # From v3.h.
    struct s_v3:
        int type
        double v[3]

    ctypedef s_v3 V3

    # From v6.h.
    struct s_v6:
        V3 v[2]

    ctypedef s_v6 V6

    int POS
    int VEL

    # From m3.h.
    struct s_m3:
        double m[3][3]

    ctypedef s_m3 M3

    # From m6.h
    struct s_m6:
        M3 m[2][2]

    ctypedef s_m6 M6
    
    # From vec.h.
    int CARTESIAN
    int SPHERICAL
    int POLAR

    M3 m3I(double x)
    M3 m3O()
    M3 m3Rx(double x)
    M3 m3RxDot(double x, double xdot)
    M3 m3Ry(double y)
    M3 m3RyDot(double y, double ydot)
    M3 m3Rz(double z)
    M3 m3RzDot(double z, double zdot)
    M3 m3diff(M3 m1, M3 m2)
    M3 m3inv(M3 m)
    M3 m3m3(M3 m1, M3 m2)
    M3 m3scale(M3 m, double s)
    M3 m3sum(M3 m1, M3 m2)
    M6 m6I(double x)
    M6 m6O()
    M6 m6Qx(double x, double xdot)
    M6 m6Qy(double y, double ydot)
    M6 m6Qz(double z, double zdot)
    M6 m6diff(M6 m1, M6 m2)
    M6 m6inv(M6 m)
    M6 m6m6(M6 m1, M6 m2)
    M6 m6scale(M6 m, double s)
    M6 m6sum(M6 m1, M6 m2)
    V3 m3v3(M3 m, V3 v1)
    V3 m6v3(M6 m, V3 v)
    V3 v3c2s(V3 vc)
    V3 v3cross(V3 v1, V3 v2)
    V3 v3diff(V3 v1, V3 v2)
    V3 v3init(int type)
    V3 v3s2c(V3 vs)
    V3 v3scale(V3 v, double s)
    V3 v3sum(V3 v1, V3 v2)
    V3 v3unit(V3 v)
    V3 v62v3(V6 v6, double dt)
    V6 m3v6(M3 m, V6 v1)
    V6 m6v6(M6 m, V6 v1)
    V6 v32v6(V3 v3)
    V6 v6c2s(V6 vc)
    V6 v6cross(V6 v1, V6 v2)
    V6 v6diff(V6 v1, V6 v2)
    V6 v6init(int type)
    V6 v6s2c(V6 vs)
    V6 v6scale(V6 v, double s)
    V6 v6sum(V6 v1, V6 v2)
    V6 v6unit(V6 v)
    char *m3fmt(M3 m)
    char *m6fmt(M6 m)
    char *v3fmt(V3 v)
    char *v6fmt(V6 v)
    double v3alpha(V3 v)
    double v3delta(V3 v)
    double v3dot(V3 v1, V3 v2)
    double v3mod(V3 v)
    double v6alpha(V6 v)
    double v6delta(V6 v)
    double v6dot(V6 v1, V6 v2)
    double v6mod(V6 v)
