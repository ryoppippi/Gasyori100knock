#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>


// Channel swap
cv::Mat channel_swap(cv::Mat img){
  // get height and width
  int width = img.cols;
  int height = img.rows;

  // prepare output
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  // each y, x
  for (int y = 0; y < height; y++){
    for (int x = 0; x < width; x++){
      // R -> B
      out.at<cv::Vec3b>(y, x)[0] = img.at<cv::Vec3b>(y, x)[2];
      // B -> R
      out.at<cv::Vec3b>(y, x)[2] = img.at<cv::Vec3b>(y, x)[0];
      // G -> G
      out.at<cv::Vec3b>(y, x)[1] = img.at<cv::Vec3b>(y, x)[1];
    }
  }

  return out;
}


int main(int argc, const char* argv[]){
  // read image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  // channel swap
  cv::Mat out = channel_swap(img);

  //cv::imwrite("out.jpg", out);
  cv::imshow("sample", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
