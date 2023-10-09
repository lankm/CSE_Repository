#include <stdio.h>
#include <math.h>

#define PI 3.1415926535897932384626

#define G 4.16427960
#define b 0.17080023
#define I 0.08825050

int UTA_ID = 1001906270;

// testing variables
double summation = 0.0;
double count = 0;
double last = 0;


double PD_control(double theta, double theta_dot, double theta_ref, double theta_dot_ref)
{
  // // torque = I*theta_dot_dot + B*theta_dot + G*cos(theta)

  // // testing for G
  // double torque = 5*theta_ref;
  // printf("G = %.8f\n", torque/cos(theta));
  // return torque;

  // // testing for B
  // double torque = theta_ref + G*cos(theta);
  // if (theta_ref > 3.0) {
  //   summation += theta_ref/theta_dot;
  //   count += 1;
  //   summation /= 1.0001;
  //   count /= 1.0001;
  // }
  // printf("B = %.8f\n", summation/count);
  // return torque;

  // // testing for M
  // double torque = B*theta_dot;
  // double accel = 500*(theta_dot - last);
  // last = theta_dot;
  // // getting calcualted acceleration only when torque is large
  // if (.01 > fmod(theta, PI) && -.01 < fmod(theta, PI)) {
  //   summation += -G*cos(theta)/accel;
  //   count += 1;
  //   printf("I = %.8f\n", summation/count);
  // }
  // return torque;
  
  double gravity = G*cos(theta);
  double K = 50.0; // arbetrary. change as desired
  double B = 2*sqrt(K);
  //         spring force                  friction 
  return I*(K*(theta_ref - theta) + (B+b)*(theta_dot_ref - theta_dot)) + gravity;
}
