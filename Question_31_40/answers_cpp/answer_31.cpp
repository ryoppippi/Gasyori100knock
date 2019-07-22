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
  double dx = 30, dy = 30;
  double a = 1, b = dx / height, tx = 0;
  double c = dy / width, d = 1, ty = 0;

  double det = a * d - b * c;

  // Resize width and height
  int resized_width = (int)(width + dx);
  int resized_height = (int)(height + dy);

  // other parameters
  int x_before, y_before;

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

