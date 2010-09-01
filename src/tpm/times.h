/* file: $RCSfile: times.h,v $
** rcsid: $Id: times.h 261 2007-10-19 19:07:02Z laidler $
** Copyright Jeffrey W Percival
** *******************************************************************
** Space Astronomy Laboratory
** University of Wisconsin
** 1150 University Avenue
** Madison, WI 53706 USA
** *******************************************************************
** Do not use this software without attribution.
** Do not remove or alter any of the lines above.
** *******************************************************************
*/

/*
**********************************************************************
** $RCSfile: times.h,v $ - declarations for the times routines
**
** "rdb" time is defined to be a scalar of the form yymmdd.ff
**********************************************************************
*/

#ifndef TIMES_H
#define TIMES_H

#include <math.h>
#ifndef M_PI
#define M_PI (3.14159265358979323846)
#endif

/* the JD of the modified JD system */
#define MJD_0	(2400000.5)

/* the JD of B1950.0 */
#define B1950	(2433282.42345905)

/* the JD of J2000.0 */
#define J2000	(2451545.0)

/* the JD of 1984.0, the magic FK4/FK5 conversion time */
#define J1984   (2445700.5)

/* the tropical century at 1900.0 */
#define CB	(36524.21987817305)

/* the julian century */
#define CJ	(36525.0)

#define BYEAR2JD(x)	(B1950 + ((x)-1950.0)*(CB/100.0))
#define JD2BYEAR(x)	(1950.0 + ((x)-B1950)*(100.0/CB))
#define JYEAR2JD(x)	(J2000 + ((x)-2000.0)*(CJ/100.0))
#define JD2JYEAR(x)	(2000.0 + ((x)-J2000)*(100.0/CJ))

#define SUNDAY		(0)
#define MONDAY		(1)
#define TUESDAY		(2)
#define WEDNESDAY	(3)
#define THURSDAY	(4)
#define FRIDAY		(5)
#define SATURDAY	(6)

/* degree, minute, second */
typedef struct s_dms {
	double dd;
	double mm;
	double ss;
} DMS;

/* hour, minute, second */
typedef struct s_hms {
	double hh;
	double mm;
	double ss;
} HMS;

/* year, month, day*/
typedef struct s_ymd {
	int y;
	int m;
	double dd;
	HMS hms;
} YMD;

/* julian day */
typedef struct s_jd {
	double dd;	/* day part */
	HMS hms;	/* fractional part */
} JD;

/* define some macros to access the structures */

#define dmsDecDegrees(s, x)	(s.dd -= (x))
#define dmsDecMinutes(s, x)	(s.mm -= (x))
#define dmsDecSeconds(s, x)	(s.ss -= (x))
#define dmsDivDegrees(s, x)	(s.dd /= (x))
#define dmsDivMinutes(s, x)	(s.mm /= (x))
#define dmsDivSeconds(s, x)	(s.ss /= (x))
#define dmsGetDegrees(s)	(s.dd)
#define dmsGetMinutes(s)	(s.mm)
#define dmsGetSeconds(s)	(s.ss)
#define dmsIncDegrees(s, x)	(s.dd += (x))
#define dmsIncMinutes(s, x)	(s.mm += (x))
#define dmsIncSeconds(s, x)	(s.ss += (x))
#define dmsMulDegrees(s, x)	(s.dd *= (x))
#define dmsMulMinutes(s, x)	(s.mm *= (x))
#define dmsMulSeconds(s, x)	(s.ss *= (x))
#define dmsSetDegrees(s, x)	(s.dd = (x))
#define dmsSetMinutes(s, x)	(s.mm = (x))
#define dmsSetSeconds(s, x)	(s.ss = (x))

#define hmsDecHours(s, x)	(s.hh -= (x))
#define hmsDecMinutes(s, x)	(s.mm -= (x))
#define hmsDecSeconds(s, x)	(s.ss -= (x))
#define hmsDivHours(s, x)	(s.hh /= (x))
#define hmsDivMinutes(s, x)	(s.mm /= (x))
#define hmsDivSeconds(s, x)	(s.ss /= (x))
#define hmsGetHours(s)		(s.hh)
#define hmsGetMinutes(s)	(s.mm)
#define hmsGetSeconds(s)	(s.ss)
#define hmsIncHours(s, x)	(s.hh += (x))
#define hmsIncMinutes(s, x)	(s.mm += (x))
#define hmsIncSeconds(s, x)	(s.ss += (x))
#define hmsMulHours(s, x)	(s.hh *= (x))
#define hmsMulMinutes(s, x)	(s.mm *= (x))
#define hmsMulSeconds(s, x)	(s.ss *= (x))
#define hmsSetHours(s, x)	(s.hh = (x))
#define hmsSetMinutes(s, x)	(s.mm = (x))
#define hmsSetSeconds(s, x)	(s.ss = (x))

#define jdDecDay(s, x)		(s.dd -= (x))
#define jdDecHours(s, x)	(s.hms.hh -= (x))
#define jdDecMinutes(s, x)	(s.hms.mm -= (x))
#define jdDecSeconds(s, x)	(s.hms.ss -= (x))
#define jdDivDay(s, x)		(s.dd /= (x))
#define jdDivHours(s, x)	(s.hms.hh /= (x))
#define jdDivMinutes(s, x)	(s.hms.mm /= (x))
#define jdDivSeconds(s, x)	(s.hms.ss /= (x))
#define jdGetDay(s)		(s.dd)
#define jdGetHours(s)		(s.hms.hh)
#define jdGetMinutes(s)		(s.hms.mm)
#define jdGetSeconds(s)		(s.hms.ss)
#define jdIncDay(s, x)		(s.dd += (x))
#define jdIncHours(s, x)	(s.hms.hh += (x))
#define jdIncMinutes(s, x)	(s.hms.mm += (x))
#define jdIncSeconds(s, x)	(s.hms.ss += (x))
#define jdMulDay(s, x)		(s.dd *= (x))
#define jdMulHours(s, x)	(s.hms.hh *= (x))
#define jdMulMinutes(s, x)	(s.hms.mm *= (x))
#define jdMulSeconds(s, x)	(s.hms.ss *= (x))
#define jdSetDay(s, x)		(s.dd = (x))
#define jdSetHours(s, x)	(s.hms.hh = (x))
#define jdSetMinutes(s, x)	(s.hms.mm = (x))
#define jdSetSeconds(s, x)	(s.hms.ss = (x))

#define ymdDecDay(s, x)		(s.dd -= (x))
#define ymdDecHours(s, x)	(s.hms.hh -= (x))
#define ymdDecMinutes(s, x)	(s.hms.mm -= (x))
#define ymdDecMonth(s, x)	(s.m -= (x))
#define ymdDecSeconds(s, x)	(s.hms.ss -= (x))
#define ymdDecYear(s, x)	(s.y -= (x))
#define ymdDivDay(s, x)		(s.dd /= (x))
#define ymdDivHours(s, x)	(s.hms.hh /= (x))
#define ymdDivMinutes(s, x)	(s.hms.mm /= (x))
#define ymdDivMonth(s, x)	(s.m /= (x))
#define ymdDivSeconds(s, x)	(s.hms.ss /= (x))
#define ymdDivYear(s, x)	(s.y /= (x))
#define ymdGetDay(s)		(s.dd)
#define ymdGetHours(s)		(s.hms.hh)
#define ymdGetMinutes(s)	(s.hms.mm)
#define ymdGetMonth(s)		(s.m)
#define ymdGetSeconds(s)	(s.hms.ss)
#define ymdGetYear(s)		(s.y)
#define ymdIncDay(s, x)		(s.dd += (x))
#define ymdIncHours(s, x)	(s.hms.hh += (x))
#define ymdIncMinutes(s, x)	(s.hms.mm += (x))
#define ymdIncMonth(s, x)	(s.m += (x))
#define ymdIncSeconds(s, x)	(s.hms.ss += (x))
#define ymdIncYear(s, x)	(s.y += (x))
#define ymdMulDay(s, x)		(s.dd *= (x))
#define ymdMulHours(s, x)	(s.hms.hh *= (x))
#define ymdMulMinutes(s, x)	(s.hms.mm *= (x))
#define ymdMulMonth(s, x)	(s.m *= (x))
#define ymdMulSeconds(s, x)	(s.hms.ss *= (x))
#define ymdMulYear(s, x)	(s.y *= (x))
#define ymdSetDay(s, x)		(s.dd = (x))
#define ymdSetHours(s, x)	(s.hms.hh = (x))
#define ymdSetMinutes(s, x)	(s.hms.mm = (x))
#define ymdSetMonth(s, x)	(s.m = (x))
#define ymdSetSeconds(s, x)	(s.hms.ss = (x))
#define ymdSetYear(s, x)	(s.y = (x))

/* define some short-cut macros */

/* these are repeated in vec.h */
#ifndef VEC_H
#define d2h(d)			((d)/15.0)
#define h2d(h)			((h)*15.0)
#define d2r(d)			((d)*(M_PI/180.0))
#define r2d(r)			((r)*(180.0/M_PI))
#define h2r(h)			((h)*(M_PI/12.0))
#define r2h(r)			((r)*(12.0/M_PI))
#define d2as(d)			((d)*3600.0)
#define as2d(x)			((x)/3600.0)
#define as2h(x)			(d2h(as2d(x)))
#define h2as(h)			(d2as(h2d(h)))
#define r2as(r)			(d2as(r2d(r)))
#define as2r(x)			(d2r(as2d(x)))
#endif

#define d2hms(d)		(h2hms(d2h(d)))
#define dms2h(dms)		(d2h(dms2d(dms)))
#define dms2r(dms)		(d2r(dms2d(dms)))
#define fmt_dms(dms)		(fmt_d(dms2d(dms)))
#define fmt_hms(hms)		(fmt_h(hms2h(hms)))
#define fmt_jd(jd)		(fmt_j(jd2j(jd)))
#define fmt_r(r)		(fmt_d(r2d(r)))
#define fmt_y(y)		(fmt_ymd(y2ymd(y)))
#define h2dms(h)		(d2dms(h2d(h)))
#define hms2d(hms)		(h2d(hms2h(hms)))
#define hms2r(hms)		(h2r(hms2h(hms)))
#define j2j(j)			(j)
#define j2rdb(j)		(jd2rdb(j2jd(j)))
#define j2y(j)			(jd2y(j2jd(j)))
#define j2ymd(j)		(jd2ymd(j2jd(j)))
#define jd2rdb(jd)		(ymd2rdb(jd2ymd(jd)))
#define jd2y(jd)		(ymd2y(jd2ymd(jd)))
#define r2dms(r)		(d2dms(r2d(r)))
#define r2hms(r)		(h2hms(r2h(r)))
#define rdb2j(rdb)		(jd2j(rdb2jd(rdb)))
#define rdb2jd(rdb)		(ymd2jd(rdb2ymd(rdb)))
#define rdb2rdb(rdb)		(ymd2rdb(rdb2ymd(rdb)))
#define rdb2y(rdb)		(ymd2y(rdb2ymd(rdb)))
#define rdb_diff(rdb1,rdb2)	(jd_diff(rdb2jd(rdb1),rdb2jd(rdb2)))
#define y2j(y)			(jd2j(y2jd(y)))
#define y2jd(y)			(ymd2jd(y2ymd(y)))
#define y2rdb(y)		(ymd2rdb(y2ymd(y)))
#define y2y(y)			(y)
#define ymd2j(ymd)		(jd2j(ymd2jd(ymd)))
#define ymd_diff(ymd1,ymd2)	(jd_diff(ymd2jd(ymd1),ymd2jd(ymd2)))

/* EXTERN_START */
extern DMS d2dms(double d);
extern DMS dms2dms(DMS dms);
extern DMS dms_diff(DMS dms1, DMS dms2);
extern DMS dms_sum(DMS dms1, DMS dms2);
extern DMS hms2dms(HMS hms);
extern HMS dms2hms(DMS dms);
extern HMS h2hms(double h);
extern HMS hms2hms(HMS hms);
extern HMS hms_diff(HMS hms1, HMS hms2);
extern HMS hms_sum(HMS hms1, HMS hms2);
extern JD j2jd(double j);
extern JD jd2jd(JD jd);
extern JD jd_diff(JD jd1, JD jd2);
extern JD jd_now(void);
extern JD jd_sum(JD jd1, JD jd2);
extern JD ymd2jd(YMD ymd);
extern YMD jd2ymd(JD jd);
extern YMD rdb2ymd(double rdb);
extern YMD y2ymd(double y);
extern YMD ydd2ymd(int y, double dd);
extern YMD ymd2ymd(YMD ymd);
extern char *fmt_alpha(double alpha);
extern char *fmt_d(double d);
extern char *fmt_delta(double delta);
extern char *fmt_h(double h);
extern char *fmt_j(double j);
extern char *fmt_rdb(double rdb);
extern char *fmt_ymd(YMD ymd);
extern char *fmt_ymd_raw(YMD ymd);
extern double d2d(double d);
extern double dms2d(DMS dms);
extern double gcal2j(int y, int m, int d);
extern double h2h(double h);
extern double hms2h(HMS hms);
extern double jcal2j(int y, int m, int d);
extern double jd2j(JD jd);
extern double r2r(double r);
extern double utc_now(void);
extern double ymd2dd(YMD ymd);
extern double ymd2rdb(YMD ymd);
extern double ymd2y(YMD ymd);
extern int argv2dms(DMS *dms, char *argv[], int argnum, int cooked);
extern int argv2hms(HMS *hms, char *argv[], int argnum, int cooked);
extern int argv2ymd(YMD *ymd, char *argv[], int argnum, int cooked);
extern int j2dow(double j);
extern int y2doy(int y);
extern void j2gcal(int *y, int *m, int *d, double j);
extern void j2jcal(int *y, int *m, int *d, double j);
/* EXTERN_STOP */

#endif
