#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;
  
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);
  
  for (int j = 0; j < height; j++){
    for (int i = 0; i < width; i++){
      for (int c = 0; c < 3; c++){
	out.at<cv::Vec3b>(j,i)[c] = (uchar)(floor((double)img.at<cv::Vec3b>(j,i)[c] / 64) * 64 + 32);
      }
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
