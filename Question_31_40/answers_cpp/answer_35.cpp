#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>
#include <complex>

const int height = 128, width = 128;

struct fourier_str {
  std::complex<double> coef[height][width];
};

// RGB to Gray scale
cv::Mat BGR2GRAY(cv::Mat img){
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

// Discrete Fourier transformation
fourier_str dft(cv::Mat img, fourier_str fourier_s){
  
  double I;
  double theta;
  std::complex<double> val;

  for ( int l = 0; l < height; l ++){
    for ( int k = 0; k < width; k ++){
      val.real(0);
      val.imag(0);
      for ( int y = 0; y < height; y ++){
        for ( int x = 0; x < width; x ++){
          I = (double)img.at<uchar>(y, x);
          theta = -2 * M_PI * ((double)k * (double)x / (double)width + (double)l * (double)y / (double)height);
          val += std::complex<double>(cos(theta), sin(theta)) * I;
        }
      }
      val /= sqrt(height * width);
      fourier_s.coef[l][k] = val;
    }
  }

  return fourier_s;
}

// Inverse Discrete Fourier transformation
cv::Mat idft(cv::Mat out, fourier_str fourier_s){

  double theta;
  double g;
  std::complex<double> G;
  std::complex<double> val;

  for ( int y = 0; y < height; y ++){
    for ( int x = 0; x < width; x ++){
      val.real(0);
      val.imag(0);
      for ( int l = 0; l < height; l ++){
        for ( int k = 0; k < width; k ++){
          G = fourier_s.coef[l][k];
          theta = 2 * M_PI * ((double)k * (double)x / (double)width + (double)l * (double)y / (double)height);
          val += std::complex<double>(cos(theta), sin(theta)) * G;
        }
      }
      g = std::abs(val) / sqrt(height * width);
      g = fmin(fmax(g, 0), 255);
      out.at<uchar>(y, x) = (uchar)g;
    }
  }

  return out;
}


// Band pass Filter
fourier_str bpf(fourier_str fourier_s, double pass_lower, double pass_upper){

  // filtering
  int r = height / 2;
  int filter_lower = (int)((double)r * pass_lower);
  int filter_upper = (int)((double)r * pass_upper);
  for ( int j = 0; j < height / 2; j++){
    for ( int i = 0; i < width / 2; i++){
      if ((sqrt(i * i + j * j) < filter_lower) || 
          (sqrt(i * i + j * j) > filter_upper)){
        fourier_s.coef[j][i] = 0;
        fourier_s.coef[j][width - i] = 0;
        fourier_s.coef[height - i][i] = 0;
        fourier_s.coef[height - i][width - i] = 0;
      }
    }
  }

  /*
  fourier_str tmp_s;
  // region change
  for ( int j = 0; j < height / 2; j++){
    for ( int i = 0; i < width / 2; i++){
      // left top > right bottom
      tmp_s.coef[height / 2 + j][width / 2 + i] = fourier_s.coef[j][i];
      // right top > left bottom
      tmp_s.coef[height / 2 + j][i] = fourier_s.coef[j][width / 2 + i];
      // left bottom > right top
      tmp_s.coef[j][width / 2 + i] = fourier_s.coef[height / 2 + j][i];
      // right bottom > left top
      tmp_s.coef[j][i] = fourier_s.coef[height / 2 + j][width / 2 + i];
    }
  }

  // filtering
  int r = height / 2;
  int filter_d = (int)((double)r / 2);
  for ( int j = 0; j < height / 2; j++){
    for ( int i = 0; i < width / 2; i++){
      if (sqrt(i * i + j + j) >= filter_d){
        tmp_s.coef[height / 2 - j][width / 2 + i] = 0;
        tmp_s.coef[height / 2 - j][width / 2 - i] = 0;
        tmp_s.coef[height / 2 + i][width / 2 + i] = 0;
        tmp_s.coef[height / 2 + i][width / 2 - i] = 0;
      }
    }
  }

  // return region
  for ( int j = 0; j < height / 2; j++){
    for ( int i = 0; i < width / 2; i++){
      // left top > right bottom
      fourier_s.coef[height / 2 + j][width / 2 + i] = tmp_s.coef[j][i];
      // right top > left bottom
      fourier_s.coef[height / 2 + j][i] = tmp_s.coef[j][width / 2 + i];
      // left bottom > right top
      fourier_s.coef[j][width / 2 + i] = tmp_s.coef[height / 2 + j][i];
      // right bottom > left top
      fourier_s.coef[j][i] = tmp_s.coef[height / 2 + j][width / 2 + i];
    }
  }
  */

  return fourier_s;
}


// Main
int main(int argc, const char* argv[]){

  // read original image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  // Fourier coefficient
  fourier_str fourier_s;

  // output image
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);

  // BGR -> Gray
  cv::Mat gray = BGR2GRAY(img);


  // DFT
  fourier_s = dft(gray, fourier_s);

  // HPF
  fourier_s = bpf(fourier_s, 0.1, 0.5);

  // IDFT
  out = idft(out, fourier_s);
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}

