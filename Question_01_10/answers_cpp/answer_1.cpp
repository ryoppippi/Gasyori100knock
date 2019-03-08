#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  cv::Mat out = img.clone();

  for (int j=0; j<height; j++){
    for (int i=0; i<width; i++){
      unsigned char tmp = out.at<cv::Vec3b>(j, i)[0];
      out.at<cv::Vec3b>(j, i)[0] = img.at<cv::Vec3b>(j,i)[2];
      out.at<cv::Vec3b>(j,i)[2] = tmp;
    }
  }

  //cv::imwrite("out.jpg", out);
  cv::imshow("sample", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;

}
