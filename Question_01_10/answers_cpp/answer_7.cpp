#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>


// average pooling
cv::Mat average_pooling(cv::Mat img){
  int height = img.rows;
  int width = img.cols;
  int channel = img.channels();

  // prepare output
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  int r = 8;
  double v = 0;
  
  for (int y = 0; y < height; y+=r){
    for (int x = 0; x < width; x+=r){
      for (int c = 0; c < channel; c++){
        v = 0;
        for (int dy = 0; dy < r; dy++){
          for (int dx = 0; dx < r; dx++){
            v += (double)img.at<cv::Vec3b>(y + dy, x + dx)[c];
          }
        }
        v /= (r * r);
        for (int dy = 0; dy < r; dy++){
          for (int dx = 0; dx < r; dx++){
            out.at<cv::Vec3b>(y + dy, x + dx)[c] = (uchar)v;
          }
        }
      }
	  }
	}
  return out;
}

int main(int argc, const char* argv[]){
  // read image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  // average pooling
  cv::Mat out = average_pooling(img);
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
