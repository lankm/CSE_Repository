#include <stdio.h>
#include <math.h>

// TODO: Actually learn this and do it myself

#define G -4.1642796
#define B -0.170857
#define M 11.34

int UTA_ID = 1001906270;

double summation = 0.0;
int count = 0;

double last = 0;


double PD_control(double theta, double theta_dot, double theta_ref, double theta_dot_ref)
{
  double gravity = G*cos(theta);
  double friction = B*theta_dot;
  double K = 3.0; // arbetrary
  double KP = 2*sqrt(K);
  
  return(K*M*(theta_ref-theta) - gravity - friction - KP*theta_dot);
}
