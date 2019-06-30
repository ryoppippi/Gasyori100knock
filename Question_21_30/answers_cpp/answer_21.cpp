#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori_dark.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  double a = 0.;
  double b = 255.;
  double c = 256., d = 0.;
  double val;

  // get [c, d]
  for (int i = 0; i < height; i++){
    for (int j = 0; j < width; j++){
      for (int k = 0; k < 3; k++){
	val = (float)img.at<cv::Vec3b>(j, i)[k];
	c = fmin(c, val);
	d = fmax(d, val);
      }
    }
  }


  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  // histogram transformation
  for (int i = 0; i < height; i++){
    for ( int j = 0; j < width; j++){
      for ( int k = 0; k < 3; k++){
	val = img.at<cv::Vec3b>(j, i)[k];
	
	if (val < a){
	  out.at<cv::Vec3b>(j, i)[k] = (uchar)a;
	}
	else if (val <= b){
	  out.at<cv::Vec3b>(j, i)[k] = (uchar)((b - a) / (d - c) * (val - c) + a);
	}
	else {
	  out.at<cv::Vec3b>(j, i)[k] = (uchar)b;
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
