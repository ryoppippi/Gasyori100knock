#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori_dark.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  double Zmax = 255;
  double hist[255];
  double S = height * width * 3;
  int val;
  double hist_sum = 0;

  for (int i = 0; i < 255; i++){
     hist[i] = 0;
  }

  // get histogram sum
  for (int i = 0; i < height; i++){
    for (int j = 0; j < width; j++){
      for (int k = 0; k < 3; k++){
	val = (int)img.at<cv::Vec3b>(j, i)[k];
	hist[val] ++;
      }
    }
  }

  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  // histogram equalization
  for (int i = 0; i < height; i++){
    for (int j = 0; j < width; j++){
      for (int k = 0; k < 3; k++){
	val = (int)img.at<cv::Vec3b>(j, i)[k];

	hist_sum = 0;
	for (int l = 0; l < val; l++){
	  hist_sum += hist[l];
	}
	out.at<cv::Vec3b>(j, i)[k] = (uchar)(Zmax / S * hist_sum);
      }
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
