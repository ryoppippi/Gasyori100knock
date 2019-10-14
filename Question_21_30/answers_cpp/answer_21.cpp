#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>


// histogram normalization
cv::Mat histogram_normalization(cv::Mat img, int a, int b){
  // get height and width
  int width = img.cols;
  int height = img.rows;
  int channel = img.channels();

  int c, d;
  int val;

  // prepare output
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  // get [c, d]
  for (int y = 0; y < height; y++){
    for (int x = 0; x < width; x++){
      for (int _c = 0; _c < channel; _c++){
        val = (float)img.at<cv::Vec3b>(y, x)[_c];
        c = fmin(c, val);
        d = fmax(d, val);
      }
    }
  }

  // histogram transformation
  for (int y = 0; y < height; y++){
    for ( int x = 0; x < width; x++){
      for ( int _c = 0; _c < 3; _c++){
        val = img.at<cv::Vec3b>(y, x)[_c];
        
        if (val < a){
          out.at<cv::Vec3b>(y, x)[_c] = (uchar)a;
        }
        else if (val <= b){
          out.at<cv::Vec3b>(y, x)[_c] = (uchar)((b - a) / (d - c) * (val - c) + a);
        }
        else {
          out.at<cv::Vec3b>(y, x)[_c] = (uchar)b;
        }
      }
    }
  }

  return out;
}


int main(int argc, const char* argv[]){
  // read image
  cv::Mat img = cv::imread("imori_dark.jpg", cv::IMREAD_COLOR);

  // histogram normalization
  cv::Mat out = histogram_normalization(img, 0, 255);
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();
 
  return 0;
}
