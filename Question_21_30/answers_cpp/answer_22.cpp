#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori_dark.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  double m0 = 128, s0 = 52;
  double m, s;
  double sum = 0., squared_sum = 0.;
  double val;

  // get sum
  for (int i = 0; i < height; i++){
    for (int j = 0; j < width; j++){
      for (int k = 0; k < 3; k++){
	val = (float)img.at<cv::Vec3b>(j, i)[k];
	sum += val;
	squared_sum += (val * val);
      }
    }
  }

  // get standard deviation
  m = sum / (height * width * 3);
  s = sqrt(squared_sum / (height * width * 3) - m * m);


  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  // histogram transformation
  for (int i = 0; i < height; i++){
    for ( int j = 0; j < width; j++){
      for ( int k = 0; k < 3; k++){
	val = img.at<cv::Vec3b>(j, i)[k];
	
	out.at<cv::Vec3b>(j, i)[k] = (uchar)(s0 / s * (val - m) + m0);
      }
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
