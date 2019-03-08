#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  double _max, _min;
  double r, g ,b;
  double h, s, v;
  double c, _h, x;
  double _r, _g, _b;
  
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);
  
  for (int j=0; j<height; j++){
    for (int i=0; i<width; i++){
      // HSV
      r = (float)img.at<cv::Vec3b>(j,i)[2] / 255;
      g = (float)img.at<cv::Vec3b>(j,i)[1] / 255;
      b = (float)img.at<cv::Vec3b>(j,i)[0] / 255;

      _max = fmax(r, fmax(g, b));
      _min = fmin(r, fmin(g, b));

      if(_max == _min){
	h = 0;
      } else if (_min == b) {
	h = 60 * (g - r) / (_max - _min) + 60;
      } else if (_min == r) {
	h = 60 * (b - g) / (_max - _min) + 180;
      } else if (_min == g) {
	h = 60 * (r - b) / (_max - _min) + 300;
      }
      v = _max;
      s = _max - _min;

      // inverse hue
      h = fmod((h + 180), 360);
      
      // inverse HSV
      c = s;
      _h = h / 60;
      x = c * (1 - abs(fmod(_h, 2) - 1));

      _r = _g = _b = v - c;
      
      if (_h < 1) {
	_r += c;
	_g += x;
      } else if (_h < 2) {
	_r += x;
	_g += c;
      } else if (_h < 3) {
	_g += c;
	_b += x;
      } else if (_h < 4) {
	_g += x;
	_b += c;
      } else if (_h < 5) {
	_r += x;
	_b += c;
      } else if (_h < 6) {
	_r += c;
	_b += x;
      }

      out.at<cv::Vec3b>(j,i)[0] = (uchar)(_b * 255);
      out.at<cv::Vec3b>(j,i)[1] = (uchar)(_g * 255);
      out.at<cv::Vec3b>(j,i)[2] = (uchar)(_r * 255);
    }
  }
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;

}
