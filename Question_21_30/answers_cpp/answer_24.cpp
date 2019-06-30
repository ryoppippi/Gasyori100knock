#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori_gamma.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  double c = 1;
  double g = 2.2;
  double val;

  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  // gamma correction
  for (int i = 0; i < height; i++){
    for (int j = 0; j < width; j++){
      for (int k = 0; k < 3; k++){
	val = (double)img.at<cv::Vec3b>(j, i)[k] / 255;

	out.at<cv::Vec3b>(j, i)[k] = (uchar)(pow(val / c, 1 / g) * 255);
      }
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
