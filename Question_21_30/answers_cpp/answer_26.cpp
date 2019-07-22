#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){

  // read original image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  // resized ratio
  double rx = 1.5, ry = 1.5;

  int resized_width = (int)(width * rx);
  int resized_height = (int)(height * ry);
  int x_before, y_before;
  double dx, dy;
  double val;

  // output image
  cv::Mat out = cv::Mat::zeros(resized_height, resized_width, CV_8UC3);

  // bi-linear interpolation
  for (int y = 0; y < resized_height; y++){
    y_before = (int)floor(y / ry);
    y_before = fmin(y_before, height - 1);
    dy = y / ry - y_before;
    
    for (int x = 0; x < resized_width; x++){
      x_before = (int)floor(x / rx);
      x_before = fmin(x_before, width - 1);
      dx = x / rx - x_before;
      
      // compute bi-linear
      for (int k = 0; k < 3; k++){
        val = (1. - dx) * (1. - dy) * img.at<cv::Vec3b>(y_before, x_before)[k] +
          dx * (1. - dy) * img.at<cv::Vec3b>(y_before, x_before + 1)[k] +
          (1. - dx) * dy * img.at<cv::Vec3b>(y_before + 1, x_before)[k] +
          dx * dy * img.at<cv::Vec3b>(y_before + 1, x_before)[k];

        // assign pixel to new position
        out.at<cv::Vec3b>(y, x)[k] = (uchar)val;
      }
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
