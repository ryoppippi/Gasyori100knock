#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  cv::Mat img2 = img.clone();

  //cv::Mat disp(cv::Size(height, width*2+10), CV_8UC3, cv::Scalar(0,0,0));
    
  int i = 0, j = 0;

  for(i=0; i<width/2; i++){
    for(j=0; j<height/2; j++){
      img.at<cv::Vec3b>(j, i)[0] = 0;
      img.at<cv::Vec3b>(j, i)[1] = 400;
      img.at<cv::Vec3b>(j, i)[2] = -200;
    }
  }

  cv::Mat disp;
  cv::Mat tmp[3];
  tmp[0] = img;
  tmp[1] = cv::Mat (cv::Size(10, height), CV_8UC3, cv::Scalar(0,0,0));
  tmp[2] = img2;
  cv::hconcat(tmp, 3, disp);

  cv::imshow("sample", disp);
  cv::waitKey(0);
  cv::destroyAllWindows();

  cv::imwrite("out.jpg", disp);

  return 0;

}
