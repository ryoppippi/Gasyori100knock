#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>
#include <complex>

// BGR -> Y Cb Cr
cv::Mat BGR2YCbCr(cv::Mat img, cv::Mat out){
  int width = img.rows;
  int height = img.cols;

  //cv::Mat out = cv::Mat::zeros(height, width, CV_32F);
  
  for (int j = 0; j < height; j ++){
    for (int i = 0; i < width; i ++){
      // Y
      out.at<cv::Vec3b>(j, i)[0] = (int)((float)img.at<cv::Vec3b>(j,i)[0] * 0.114 + \
				  (float)img.at<cv::Vec3b>(j,i)[1] * 0.5870 + \
				  (float)img.at<cv::Vec3b>(j,i)[2] * 0.299);

      // Cb
      out.at<cv::Vec3b>(j, i)[1] = (int)((float)img.at<cv::Vec3b>(j,i)[0] * 0.5 + \
				  (float)img.at<cv::Vec3b>(j,i)[1] * (-0.3323) + \
				  (float)img.at<cv::Vec3b>(j,i)[2] * (-0.1687) + 128);

      // Cr
      out.at<cv::Vec3b>(j, i)[2] = (int)((float)img.at<cv::Vec3b>(j,i)[0] * (-0.0813) + \
				  (float)img.at<cv::Vec3b>(j,i)[1] * (-0.4187) + \
				  (float)img.at<cv::Vec3b>(j,i)[2] * 0.5 + 128);
    }
  }
  return out;
}

// Y Cb Cr -> BGR
cv::Mat YCbCr2BGR(cv::Mat ycbcr, cv::Mat out){

  int width = out.rows;
  int height = out.cols;
  
  for (int j = 0; j < height; j ++){
    for (int i = 0; i < width; i ++){
      // R
      out.at<cv::Vec3b>(j, i)[2] = (uchar)(ycbcr.at<cv::Vec3b>(j, i)[0] + (ycbcr.at<cv::Vec3b>(j, i)[2] - 128) * 1.4102);

      // G
      out.at<cv::Vec3b>(j, i)[1] = (uchar)(ycbcr.at<cv::Vec3b>(j, i)[0] - (ycbcr.at<cv::Vec3b>(j, i)[1] - 128) * 0.3441 - (ycbcr.at<cv::Vec3b>(j, i)[2] - 128) * 0.7139);

      // B
      out.at<cv::Vec3b>(j, i)[0] = (uchar)(ycbcr.at<cv::Vec3b>(j, i)[0] + (ycbcr.at<cv::Vec3b>(j, i)[1] - 128) * 1.7718);
    }
  }
  return out;
}

cv::Mat process(cv::Mat ycbcr){
  int width = ycbcr.rows;
  int height = ycbcr.cols;

  for(int y = 0; y < height; y++){
    for(int x = 0; x < width; x++){
      ycbcr.at<cv::Vec3b>(y, x)[0] *= 0.7;
    }
  }

  return ycbcr;
}


// Main
int main(int argc, const char* argv[]){

  // read original image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  // output image
  cv::Mat ycbcr = cv::Mat::zeros(height, width, CV_32FC3);
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  // BGR -> Y Cb Cr
  ycbcr = BGR2YCbCr(img, ycbcr);

  // Process
  ycbcr = process(ycbcr);

  // Y Cb Cr -> BGR
  out = YCbCr2BGR(ycbcr, out);

  
  cv::imwrite("out.jpg", out);
  //cv::imshow("answer", out);
  //cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}

