#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;
  
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  int r = 8;
  double v = 0;
  
  for (int j = 0; j < height; j+=r){
    for (int i = 0; i < width; i+=r){
      for (int c = 0; c < 3; c++){
	v = 0;
	for (int _j = 0; _j < r; _j++){
	  for (int _i = 0; _i < r; _i++){
	    v += (double)img.at<cv::Vec3b>(j+_j, i+_i)[c];
	  }
	}
	v /= (r * r);
	for (int _j = 0; _j < r; _j++){
	  for (int _i = 0; _i < r; _i++){
	    out.at<cv::Vec3b>(j+_j, i+_i)[c] = (uchar)v;
	  }
	}
      }
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
