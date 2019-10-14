#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>


// affine
cv::Mat affine(cv::Mat img, double a, double b, double c, double d, double tx, double ty){
  // get height and width
  int width = img.cols;
  int height = img.rows;
  int channel = img.channels();

  // get detriment
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
      for (int c = 0; c < channel; c++){
        out.at<cv::Vec3b>(y, x)[c] = img.at<cv::Vec3b>(y_before, x_before)[c];
      }
    }
  }

  return out;
}


int main(int argc, const char* argv[]){
  // read image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  // affine
  cv::Mat out = affine(img, 1.3, 0, 0, 0.8, 30, -30);
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();
 
  return 0;
}
