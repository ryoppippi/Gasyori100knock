#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){

  // read original image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  // Affine parameters
  double a = 1., b = 0.0, tx = 30;
  double c = 0.0, d = 1., ty = -30;

  double det = a * d - b * c;

  // Resize width and height
  int resized_width = (int)(width * a);
  int resized_height = (int)(height * d);

  // other parameters
  int x_before, y_before;
  double dx, dy, wx, wy, w_sum;
  double val;
  int _x, _y;

  // output
  cv::Mat out = cv::Mat::zeros(resized_height, resized_width, CV_8UC3);

  // Affine transformation
  for (int y = 0; y < resized_height; y++){    
    for (int x = 0; x < resized_width; x++){

      // get original position x
      x_before = (int)((d * x - b * y) / det - tx);

      if ((x_before < 0) || (x_before >= width)){
        continue;
      }

      // get original position y
      y_before = (int)((-c * x + a * y) / det - ty);

      if ((y_before < 0) || (y_before >= height)){
        continue;
      }

      // assign pixel to new position
      for ( int k = 0; k < 3; k++){
        out.at<cv::Vec3b>(y, x)[k] = img.at<cv::Vec3b>(y_before, x_before)[k];
      }
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}

