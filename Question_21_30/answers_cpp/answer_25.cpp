#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>


// nearest nieghbor
cv::Mat nearest_neighbor(cv::Mat img, double rx, double ry){
  // get height and width
  int width = img.cols;
  int height = img.rows;
  int channel = img.channels();


  // get resized shape
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

  // nearest neighbor
  cv::Mat out = nearest_neighbor(img, 1.5, 1.5);
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();
 
  return 0;
}
