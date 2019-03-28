#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori_noise.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  // gray scale
  cv::Mat gray = cv::Mat::zeros(height, width, CV_8UC1);
  
  for (int j=0; j<height; j++){
    for (int i=0; i<width; i++){
      gray.at<uchar>(j, i) = (int)((float)img.at<cv::Vec3b>(j,i)[0] * 0.0722 + \
				   (float)img.at<cv::Vec3b>(j,i)[1] * 0.7152 + \
				   (float)img.at<cv::Vec3b>(j,i)[2] * 0.2126);
    }
  }

  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);

  // kernel
  int k_size = 5;
  int p = floor(k_size / 2);

  double k[k_size][k_size];
  double s = 3;
  double k_sum = 0;
  double x, y;
  for (int j = 0; j < k_size; j++){
    for (int i = 0; i < k_size; i++){
      y = j - p;
      x = i - p; 
      k[j][i] = (x*x + y*y - s*s) / (2 * M_PI * pow(s, 6)) * exp( - (x*x + y*y) / (2*s*s));
      k_sum += k[j][i];
    }
  }
  for (int j = 0; j < k_size; j++){
    for (int i = 0; i < k_size; i++){
      k[j][i] /= k_sum;
    }
  }
  
  // filtering
  double v = 0;
  
  for (int j = 0; j < height; j++){
    for (int i = 0; i < width; i++){
      v = 0;
      for (int _j = -p; _j < p+1; _j++){
	for (int _i = -p; _i < p+1; _i++){
	  if (((j+_j) >= 0) && ((i+_i) >= 0) && ((j+_j) < height) && ((i+_i) < width)){
	    v += gray.at<uchar>(j+_j, i+_i) * k[_j+p][_i+p];
	  }
	}
      }
      if(v > 255){
	v = 255;
      }
      if(v < 0){
	v = 0;
      }
      
      out.at<uchar>(j, i) = v;
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
