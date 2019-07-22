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

  // output image
  cv::Mat out = cv::Mat::zeros(resized_height, resized_width, CV_8UC3);

  // nearest neighbor interpolation
  for (int y = 0; y < resized_height; y++){
    y_before = (int)round(y / ry);
    y_before = fmin(y_before, height - 1);
    
    for (int x = 0; x < resized_width; x++){
      x_before = (int)round(x / rx);
      x_before = fmin(x_before, width - 1);
      
      // assign pixel to new position
      for (int k = 0; k < 3; k++){
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
