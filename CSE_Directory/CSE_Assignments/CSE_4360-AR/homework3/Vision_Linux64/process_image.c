#include <stdio.h>
#include <math.h>
#include <X11/Xlib.h>
#include <float.h>
#include <limits.h>
#include <stdlib.h>

#define DIM 512

/******************************************************************/
/* This structure contains the coordinates of a box drawn with    */
/* the left mouse button on the image window.                     */
/* roi.x , roi.y  - left upper corner's coordinates               */
/* roi.width , roi.height - width and height of the box           */
/******************************************************************/
extern XRectangle roi;


/******************************************************************/
/* Main processing routine. This is called upon pressing the      */
/* Process button of the interface.                               */
/* image  - the original greyscale image                          */
/* size   - the actual size of the image                          */
/* proc_image - the image representation resulting from the       */
/*              processing. This will be displayed upon return    */
/*              from this function.                               */
/******************************************************************/
#define TEMPL_NUM 4
#define TEMPL_DIM 3
#define IMG_REDUC (TEMPL_DIM-1)
float templates[TEMPL_NUM][TEMPL_DIM][TEMPL_DIM] = 
{{{-1.0, -2.0, -1.0},
  { 0.0,  0.0,  0.0}, // vert (transposed in implementation)
  { 1.0,  2.0,  1.0}},
 {{-1.0,  0.0,  1.0},
  {-2.0,  0.0,  2.0}, // hor
  {-1.0,  0.0,  1.0}},
 {{ 0.0,  1.0,  2.0},
  {-1.0,  0.0,  1.0}, // maj. diag
  {-2.0, -1.0,  0.0}},
 {{-2.0, -1.0,  0.0},
  {-1.0,  0.0,  1.0}, // min. diag
  { 0.0,  1.0,  2.0}}};

// TODO: don't assume TEMP_SIZ
float apply_sobel_template(float template[TEMPL_DIM][TEMPL_DIM], unsigned char image[DIM][DIM], int off_x, int off_y) {
  float total = 0.0;
  for(int x=0; x < TEMPL_DIM; x++) {
    for(int y=0; y < TEMPL_DIM; y++) {
      int img_x = off_x + x;
      int img_y = off_y + y;
      total += template[x][y] * image[img_x][img_y];
    }
  }
  return total;
}
float apply_selected_template(unsigned char image[DIM][DIM], int i_off_x, int i_off_y, float mean, float std) {
  float total = 0.0;
  for(int x=0; x < roi.width; x++) {
    for(int y=0; y < roi.height; y++) {
      int img_x = i_off_x + x;
      int img_y = i_off_y + y;
      int templ_x = roi.x + x;
      int templ_y = roi.y + y;
      total += (image[templ_x][templ_y]-mean)/std * image[img_x][img_y];
    }
  }
  return total;
}
float selected_mean(unsigned char image[DIM][DIM]) {
  float total = 0.0;
  for(int x=0; x < roi.width; x++) {
    for(int y=0; y < roi.height; y++) {
      int templ_x = roi.x + x;
      int templ_y = roi.y + y;
      total += image[templ_x][templ_y];
    }
  }
  return total/(roi.width*roi.height);
}
float selected_std(unsigned char image[DIM][DIM], float mean) {
  float total = 0.0;
  for(int x=0; x < roi.width; x++) {
    for(int y=0; y < roi.height; y++) {
      int templ_x = roi.x + x;
      int templ_y = roi.y + y;
      total += abs(image[templ_x][templ_y] - mean);
    }
  }
  float std = total/(roi.width*roi.height);
  if(std==0) {
    return 1;
  } else {
    return std;
  }
}

#define TEMPL_SEL 1
void part_1(unsigned char image[DIM][DIM], int size[2], unsigned char proc_img[DIM][DIM]) {
  int width = size[0];
  int height = size[1];
  int proc_img_width = width-IMG_REDUC;
  int proc_img_height = height-IMG_REDUC;

  float min = FLT_MAX;
  float max = -FLT_MAX;
  float temp_img[proc_img_width][proc_img_height];
  for(int off_x=0; off_x < proc_img_width; off_x++) {
    for(int off_y=0; off_y < proc_img_height; off_y++) {
      float val = apply_sobel_template(templates[TEMPL_SEL], image, off_x, off_y);
      temp_img[off_x][off_y] = val;

      if(val < min) {
        min = val;
      } else if(val > max) {
        max = val;
      }
    }
  }

  for(int x=0; x < DIM; x++) {
    for(int y=0; y < DIM; y++) {
      if(x<proc_img_width && y<proc_img_height) {
        unsigned char val = (unsigned char) (UCHAR_MAX*((temp_img[x][y]-min)/(max-min)));
        proc_img[x][y] = val;
      } else {
        proc_img[x][y] = 127;
      }
    }
  }
}
void part_2(unsigned char image[DIM][DIM], int size[2], unsigned char proc_img[DIM][DIM]) {
  int width = size[0];
  int height = size[1];
  int proc_img_width = width-roi.width+1;
  int proc_img_height = height-roi.height+1;

  float mean = selected_mean(image);
  float std = selected_std(image, mean);

  float min = FLT_MAX;
  float max = -FLT_MAX;
  float temp_img[proc_img_width][proc_img_height];
  for(int off_x=0; off_x < proc_img_width; off_x++) {
    for(int off_y=0; off_y < proc_img_height; off_y++) {
      float val = apply_selected_template(image, off_x, off_y, mean, std);
      temp_img[off_x][off_y] = val;

      if(val < min) {
        min = val;
      } else if(val > max) {
        max = val;
      }
    }
  }

  for(int x=0; x < DIM; x++) {
    for(int y=0; y < DIM; y++) {
      if(x<proc_img_width && y<proc_img_height) {
        unsigned char val = (unsigned char) (UCHAR_MAX*((temp_img[x][y]-min)/(max-min)));
        proc_img[x][y] = val;
      } else {
        proc_img[x][y] = 0;
      }
    }
  }
}

void process_image(unsigned char image[DIM][DIM], int size[2], unsigned char proc_img[DIM][DIM]) {
  part_2(image, size, proc_img);
}
