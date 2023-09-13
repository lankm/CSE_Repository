#include <stdio.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.1415927
#endif


int fwd_kin(double *theta, double x[3])
{
  x[0] = 1.0;
  x[1] = 1.0;
  x[2] = 1.0;

  return 0;
}


int inv_kin(double *x, double theta[6])
{
  theta[0] = 1.0;
  theta[1] = 1.0;
  theta[2] = 1.0;
  theta[3] = 1.0;
  theta[4] = 1.0;
  theta[5] = 1.0;

  return 0;
}
