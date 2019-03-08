#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori_noise.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;
  
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);
  
  int k_size = 3;
  int p = floor(k_size / 2);
  
  // filtering
  double v = 0;
  int vs[k_size * k_size];
  int count = 0;
  
  for (int j = 0; j < height; j++){
    for (int i = 0; i < width; i++){
      for (int c = 0; c < 3; c++){
	v = 0;
	count = 0;
	
	for (int i = 0; i < k_size * k_size; i++){
	  vs[i] = 999;
	}
	
	for (int _j = -p; _j < p+1; _j++){
	  for (int _i = -p; _i < p+1; _i++){
	    if (((j+_j) >= 0) && ((i+_i) >= 0)){
	      vs[count++] = (int)img.at<cv::Vec3b>(j+_j, i+_i)[c];
	    }
	  }
	}

	std::sort(vs, vs+(k_size * k_size));
	out.at<cv::Vec3b>(j,i)[c] = (uchar)vs[int(floor(count / 2)) + 1];
      }
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
