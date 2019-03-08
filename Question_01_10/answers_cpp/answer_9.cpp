#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori_noise.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;
  
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  // prepare kernel
  double s = 1.3;
  int k_size = 3;
  int p = floor(k_size / 2);
  int x = 0, y = 0;
  double k_sum = 0;
  
  float k[k_size][k_size];
  for (int j = 0; j < k_size; j++){
    for (int i = 0; i < k_size; i++){
      y = j - p;
      x = i - p; 
      k[j][i] = 1 / (s * sqrt(2 * M_PI)) * exp( - (x*x + y*y) / (2*s*s));
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
      for (int c = 0; c < 3; c++){
	v = 0;
	for (int _j = -p; _j < p+1; _j++){
	  for (int _i = -p; _i < p+1; _i++){
	    if (((j+_j) >= 0) && ((i+_i) >= 0)){
	      v += (double)img.at<cv::Vec3b>(j+_j, i+_i)[c] * k[_j+p][_i+p];
	    }
	  }
	}
	out.at<cv::Vec3b>(j,i)[c] = v;
      }
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
