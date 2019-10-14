#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>



// histogram equalization
cv::Mat histogram_equalization(cv::Mat img){
  // get height and width
  int width = img.cols;
  int height = img.rows;
  int channel = img.channels();

  // output image
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  // histogram equalization hyper-parameters
  double Zmax = 255;
  double hist[255];
  double S = height * width * channel;
  int val;
  double hist_sum = 0;


  // histogram initialization
  for (int i = 0; i < 255; i++){
     hist[i] = 0;
  }

  // get histogram sum
  for (int y = 0; y < height; y++){
    for (int x = 0; x < width; x++){
      for (int c = 0; c < channel; c++){
        val = (int)img.at<cv::Vec3b>(y, x)[c];
        hist[val] ++;
      }
    }
  }

  // histogram equalization
  for (int y = 0; y < height; y++){
    for (int x = 0; x < width; x++){
      for (int c = 0; c < channel; c++){
        val = (int)img.at<cv::Vec3b>(y, x)[c];

        // get histogram sum <= current pixel value
        hist_sum = 0;
        for (int l = 0; l < val; l++){
          hist_sum += hist[l];
        }
        // assign equalized value
        out.at<cv::Vec3b>(y, x)[c] = (uchar)(Zmax / S * hist_sum);
      }
    }
  }

  return out;
}


int main(int argc, const char* argv[]){
  // read image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  // histogram equalization
  cv::Mat out = histogram_equalization(img);
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();
 
  return 0;
}

