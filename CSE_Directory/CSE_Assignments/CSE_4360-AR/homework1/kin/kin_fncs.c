#include <stdio.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.1415926535897932384626
#endif

double l[] = { .25, 0.2, 0.2, 0.15};
double d[] = { -.04, 0.04, -0.04, -0.04};

int fwd_kin(double t[6], double p[3])
{
  double x1 = 0.0;
  double y1 = 0.0;
  double z1 = l[0];

  // printf("1:( %5f , %5f , %5f )\n", x1, y1, z1);

  double x2 = l[1]*cos(t[1]);
  double y2 = 0.0;
  double z2 = z1 - l[1]*sin(t[1]);

  // printf("2:( %5f , %5f , %5f )\n", x2, y2, z2);

  double x3 = x2 + l[2]*cos(t[1]+t[2]);
  double y3 = 0.0;
  double z3 = z2 - l[2]*sin(t[1]+t[2]);

  // printf("3:( %5f , %5f , %5f )\n", x3, y3, z3);

  double x4 = x3 + d[3]*cos( t[1] + t[2] + (t[3] - M_PI/2.0) );
  double y4 = d[2];
  double z4 = z3 - d[3]*sin( t[1] + t[2] + (t[3] - M_PI/2.0) );

  // printf("4:( %5f , %5f , %5f )\n", x4, y4, z4);
  
  double x5 = x4 + l[3]*cos( t[1] + t[2] + t[3] );
  double y5 = y4;
  double z5 = z4 - l[3]*sin( t[1] + t[2] + t[3] );

  // printf("5:( %5f , %5f , %5f )\n", x5, y5, z5);

  double lf = sqrt( x5*x5 + y5*y5 );
  double tf = atan2( y5, x5 );
  double xf = lf*cos( t[0] + tf );
  double yf = lf*sin( t[0] + tf );
  double zf = z5;

  //printf("f:( %5f , %5f , %5f )\n", xf, yf, zf);

  p[0] = xf;
  p[1] = yf;
  p[2] = zf;

  return 0;
}

int inv_kin(double p[3], double t[6])
{
  double x = p[0], y = p[1], z = p[2];

  // figure out t0
  double lf = sqrt( x*x + y*y );
  double tf = atan2( y, x );
  double t0 = tf - asin(d[3]/lf);
  t[0] = t0;

  // t0 = 0. aka everything is in a plane now.
  x = lf*cos(tf);
  y = lf*sin(tf); // y is always = d3 so its not used.

  t[1] = 1.0;
  t[2] = 1.0;
  t[3] = 1.0;

  t[4] = 0.0; // given
  t[5] = 0.0; // given

  return 0;
}

// int main() {
//   double t[] = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
//   double x[] = { 0.0, 0.0, 0.0};
//   fwd_kin(t,x);

//   return 0;
// }