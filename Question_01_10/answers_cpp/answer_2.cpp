#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);
  
  for (int j=0; j<height; j++){
    for (int i=0; i<width; i++){
      out.at<uchar>(j, i) = (int)((float)img.at<cv::Vec3b>(j,i)[0] * 0.0722 + \
				  (float)img.at<cv::Vec3b>(j,i)[1] * 0.7152 + \
				  (float)img.at<cv::Vec3b>(j,i)[2] * 0.2126);
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;

}
