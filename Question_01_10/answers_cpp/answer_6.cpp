#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>


// Dedcrease color
cv::Mat decrease_color(cv::Mat img){
  int height = img.cols;
  int width = img.rows;
  int channel = img.channels();

  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  for(int y = 0; y < height; y++){
    for(int x = 0; x < width; x++){
      for(int c = 0; c < channel; c++){
        out.at<cv::Vec3b>(y, x)[c] = (uchar)(floor((double)img.at<cv::Vec3b>(y, x)[c] / 64) * 64 + 32);
      }
    }
  }
  return out;
}

int main(int argc, const char* argv[]){
  // read image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  // decrease color
  cv::Mat out = decrease_color(img);
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
