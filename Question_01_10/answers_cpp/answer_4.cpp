#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);

  // gray
  int val = 0;
  for (int j = 0; j < height; j++){
    for (int i = 0; i < width; i++){
      val = (int)((float)img.at<cv::Vec3b>(j,i)[0] * 0.0722 + \
		  (float)img.at<cv::Vec3b>(j,i)[1] * 0.7152 + \
		  (float)img.at<cv::Vec3b>(j,i)[2] * 0.2126);
      out.at<uchar>(j,i) = (uchar)val;
    }
  }

  // determine threshold
  double w0 = 0, w1 = 0;
  double m0 = 0, m1 = 0;
  double max_sb = 0, sb = 0;
  int th = 0;

  for (int t = 0; t < 255; t++){
    w0 = 0;
    w1 = 0;
    m0 = 0;
    m1 = 0;
    for (int j = 0; j < height; j++){
      for (int i = 0; i < width; i++){
	val = (int)(out.at<uchar>(j,i));

	if (val < t){
	  w0++;
	  m0 += val;
	} else {
	  w1++;
	  m1 += val;
	}
      }
    }

    m0 /= w0;
    m1 /= w1;
    w0 /= (height * width);
    w1 /= (height * width);
    sb = w0 * w1 * pow((m0 - m1), 2);
    
    if(sb > max_sb){
      max_sb = sb;
      th = t;
    }

  }

  // binalization
  for (int j = 0; j < height; j++){
    for (int i = 0; i < width; i++){
      val = (int)(out.at<uchar>(j,i));
      if (val < th){
	val = 0;
      } else {
	val = 255;
      }
      out.at<uchar>(j,i) = (uchar)val;
    }
  }

  std::cout << "threshold >> " << th << std::endl;
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;

}
