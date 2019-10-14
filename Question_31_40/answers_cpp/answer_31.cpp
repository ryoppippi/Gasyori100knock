#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

// affine
cv::Mat affine(cv::Mat img, double a, double b, double c, double d, double tx, double ty, double theta, double dx, double dy){
  // get height and width
  int width = img.cols;
  int height = img.rows;
  int channel = img.channels();

  // get detriment
  double det = a * d - b * c;

  if (dx != 0){
    b = dx / height;
  }
  if (dy != 0){
    c = dy / width;
  }

  if (theta != 0){
    // Affine parameters
    double rad = theta / 180. * M_PI;
    a = std::cos(rad);
    b = - std::sin(rad);
    c = std::sin(rad);
    d = std::cos(rad);
    tx = 0;
    ty = 0;

    double det = a * d - b * c;

    // center transition
    double cx = width / 2.;
    double cy = height / 2.;
    double new_cx = (d * cx - b * cy) / det;
    double new_cy = (- c * cx + a * cy) / det;
    tx = new_cx - cx;
    ty = new_cy - cy;
  }

  // Resize width and height
  int resized_width = (int)(width * a + dx);
  int resized_height = (int)(height * d + dy);
  
  if (theta != 0) {
    resized_width = (int)(width + dx);
    resized_height = (int)(height + dy);
  }

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
      for (int _c = 0; _c < channel; _c++){
        out.at<cv::Vec3b>(y, x)[_c] = img.at<cv::Vec3b>(y_before, x_before)[_c];
      }
    }
  }

  return out;
}


int main(int argc, const char* argv[]){
  // read image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  // affine
  cv::Mat out = affine(img, 1, 0, 0, 1, 0, 0, 0, 30, 30);
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();
 
  return 0;
}

