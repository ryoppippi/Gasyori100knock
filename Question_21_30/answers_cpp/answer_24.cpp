#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>


// gamma correction
cv::Mat gamma_correction(cv::Mat img, double gamma_c, double gamma_g){
  // get height and width
  int width = img.cols;
  int height = img.rows;
  int channel = img.channels();

  // output image
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  double val;

  // gamma correction
  for (int y = 0; y< height; y++){
    for (int x = 0; x < width; x++){
      for (int c = 0; c < channel; c++){
	      val = (double)img.at<cv::Vec3b>(y, x)[c] / 255;

	      out.at<cv::Vec3b>(y, x)[c] = (uchar)(pow(val / gamma_c, 1 / gamma_g) * 255);
      }
    }
  }

  return out;
}


int main(int argc, const char* argv[]){
  // read image
  cv::Mat img = cv::imread("imori_gamma.jpg", cv::IMREAD_COLOR);

  // gamma correction
  cv::Mat out = gamma_correction(img, 1, 2.2);
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();
 
  return 0;
}
