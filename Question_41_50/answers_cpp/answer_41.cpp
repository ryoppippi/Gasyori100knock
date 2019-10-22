#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>


// RGB to Gray scale
cv::Mat BGR2GRAY(cv::Mat img){
  // get height and width
  int height = img.rows;
  int width = img.cols;
  int channel = img.channels();

  // prepare output
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);
  
  // BGR -> Gray
  for (int y = 0; y < height; y++){
    for (int x = 0; x < width; x++){
      out.at<uchar>(y, x) = (int)((float)img.at<cv::Vec3b>(y, x)[0] * 0.0722 + \
				  (float)img.at<cv::Vec3b>(y, x)[1] * 0.7152 + \
				  (float)img.at<cv::Vec3b>(y, x)[2] * 0.2126);
    }
  }
  return out;
}

float clip(float value, float min, float max){
  return fmin(fmax(value, 0), 255);
}

// gaussian filter
cv::Mat gaussian_filter(cv::Mat img, double sigma, int kernel_size){
  int height = img.rows;
  int width = img.cols;
  int channel = img.channels();

  // prepare output
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);
  if (channel == 1) {
    out = cv::Mat::zeros(height, width, CV_8UC1);
  }

  // prepare kernel
  int pad = floor(kernel_size / 2);
  int _x = 0, _y = 0;
  double kernel_sum = 0;
  
  // get gaussian kernel
  float kernel[kernel_size][kernel_size];

  for (int y = 0; y < kernel_size; y++){
    for (int x = 0; x < kernel_size; x++){
      _y = y - pad;
      _x = x - pad; 
      kernel[y][x] = 1 / (2 * M_PI * sigma * sigma) * exp( - (_x * _x + _y * _y) / (2 * sigma * sigma));
      kernel_sum += kernel[y][x];
    }
  }

  for (int y = 0; y < kernel_size; y++){
    for (int x = 0; x < kernel_size; x++){
      kernel[y][x] /= kernel_sum;
    }
  }

  // filtering
  double v = 0;
  
  for (int y = 0; y < height; y++){
    for (int x = 0; x < width; x++){
      // for BGR
      if (channel == 3){
        for (int c = 0; c < channel; c++){
          v = 0;
          for (int dy = -pad; dy < pad + 1; dy++){
            for (int dx = -pad; dx < pad + 1; dx++){
              if (((x + dx) >= 0) && ((y + dy) >= 0) && ((x + dx) < width) && ((y + dy) < height)){
                v += (double)img.at<cv::Vec3b>(y + dy, x + dx)[c] * kernel[dy + pad][dx + pad];
              }
            }
          }
          out.at<cv::Vec3b>(y, x)[c] = (uchar)clip(v, 0, 255);
        }
      } else {
        // for Gray
        v = 0;
        for (int dy = -pad; dy < pad + 1; dy++){
          for (int dx = -pad; dx < pad + 1; dx++){
            if (((x + dx) >= 0) && ((y + dy) >= 0) && ((x + dx) < width) && ((y + dy) < height)){
              v += (double)img.at<uchar>(y + dy, x + dx) * kernel[dy + pad][dx + pad];
            }
          }
        }
        out.at<uchar>(y, x) = (uchar)clip(v, 0, 255);
      }
    }
  }
  return out;
}

// Sobel filter
cv::Mat sobel_filter(cv::Mat img, int kernel_size, bool horizontal){
  int height = img.rows;
  int width = img.cols;
  int channel = img.channels();

  // prepare output
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);

  // prepare kernel
  double kernel[kernel_size][kernel_size] = {{1, 2, 1}, {0, 0, 0}, {-1, -2, -1}};

  if (horizontal){
    kernel[0][1] = 0;
    kernel[0][2] = -1;
    kernel[1][0] = 2;
    kernel[1][2] = -2;
    kernel[2][0] = 1;
    kernel[2][1] = 0;
  }

  int pad = floor(kernel_size / 2);

  double v = 0;

  // filtering  
  for (int y = 0; y < height; y++){
    for (int x = 0; x < width; x++){
      v = 0;
      for (int dy = -pad; dy < pad + 1; dy++){
        for (int dx = -pad; dx < pad + 1; dx++){
          if (((y + dy) >= 0) && (( x + dx) >= 0) && ((y + dy) < height) && ((x + dx) < width)){
            v += (double)img.at<uchar>(y + dy, x + dx) * kernel[dy + pad][dx + pad];
          }
        }
      }
      out.at<uchar>(y, x) = (uchar)clip(v, 0, 255);
    }
  }
  return out;
}

// get edge
cv::Mat get_edge(cv::Mat fx, cv::Mat fy){
  // get height and width
  int height = fx.rows;
  int width = fx.cols;

  // prepare output
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);

  double _fx, _fy;

  for(int y = 0; y < height; y++){
    for(int x = 0; x < width; x++){
      _fx = (double)fx.at<uchar>(y, x);
      _fy = (double)fy.at<uchar>(y, x);

      out.at<uchar>(y, x) = (uchar)clip(sqrt(_fx * _fx + _fy * _fy), 0, 255);
    }
  }

  return out;
}

// get angle
cv::Mat get_angle(cv::Mat fx, cv::Mat fy){
  // get height and width
  int height = fx.rows;
  int width = fx.cols;

  // prepare output
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);

  double _fx, _fy;
  double angle;

  for(int y = 0; y < height; y++){
    for(int x = 0; x < width; x++){
      _fx = fmax((double)fx.at<uchar>(y, x), 0.000001);
      _fy = (double)fy.at<uchar>(y, x);

      angle = atan2(_fy, _fx);
      angle = angle / M_PI * 180;

      if(angle < -22.5){
        angle = 180 + angle;
      } else if (angle >= 157.5) {
        angle = angle - 180;
      }

      //std::cout << angle << " " ;

      // quantization
      if (angle <= 22.5){
        out.at<uchar>(y, x) = 0;
      } else if (angle <= 67.5){
        out.at<uchar>(y, x) = 45;
      } else if (angle <= 112.5){
        out.at<uchar>(y, x) = 90;
      } else {
        out.at<uchar>(y, x) = 135;
      }
    }
  }

  return out;
}


// Canny step 1
int Canny_step1(cv::Mat img){
  // BGR -> Gray
  cv::Mat gray = BGR2GRAY(img);

  // gaussian filter
  cv::Mat gaussian = gaussian_filter(gray, 1.4, 5);

  // sobel filter (vertical)
  cv::Mat fy = sobel_filter(gaussian, 3, false);

  // sobel filter (horizontal)
  cv::Mat fx = sobel_filter(gaussian, 3, true);

  // get edge
  cv::Mat edge = get_edge(fx, fy);

  // get angle
  cv::Mat angle = get_angle(fx, fy);
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer(edge)", edge);
  cv::imshow("answer(angle)", angle);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}

int main(int argc, const char* argv[]){
  // read image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  // Canny step 1
  Canny_step1(img);

  return 0;
}
