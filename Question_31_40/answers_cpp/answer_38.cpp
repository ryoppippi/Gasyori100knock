#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>
#include <complex>


const int height = 128, width = 128;

// DCT hyper-parameter
int T = 8;
int K = 4;

// DCT coefficient
struct dct_str {
  double coef[height][width];
};

// RGB to Gray scale
cv::Mat rgb2gray(cv::Mat img){
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);
  
  for (int j = 0; j < height; j ++){
    for (int i = 0; i < width; i ++){
      out.at<uchar>(j, i) = (int)((float)img.at<cv::Vec3b>(j,i)[0] * 0.0722 + \
				  (float)img.at<cv::Vec3b>(j,i)[1] * 0.7152 + \
				  (float)img.at<cv::Vec3b>(j,i)[2] * 0.2126);
    }
  }
  return out;
}

// Discrete Cosine transformation
dct_str dct(cv::Mat img, dct_str dct_s){
  
  double I;
  double F;
  double Cu, Cv;

  for (int ys = 0; ys < height; ys += T){
    for (int xs = 0; xs < width; xs += T){
      for (int v = 0; v < T; v ++){
        for (int u = 0; u < T; u ++){
          F = 0;

          if (u == 0){
            Cu = 1. / sqrt(2);
          } else{
            Cu = 1;
          }

          if (v == 0){
            Cv = 1. / sqrt(2);
          }else {
            Cv = 1;
          }

          for (int y = 0; y < T; y++){
            for(int x = 0; x < T; x++){
              I = (double)img.at<uchar>(ys + y, xs + x);
              F += 2. / T * Cu * Cv * I * cos((2. * x + 1) * u * M_PI / 2. / T) * cos((2. * y + 1) * v * M_PI / 2. / T);
            }
          }

          dct_s.coef[ys + v][xs + u] = F;
        }
      }
    }
  }

  return dct_s;
}

// Inverse Discrete Cosine transformation
cv::Mat idct(cv::Mat out, dct_str dct_s){
  double f;
  double Cu, Cv;

  for (int ys = 0; ys < height; ys += T){
    for (int xs = 0; xs < width; xs += T){
      for (int y = 0; y < T; y++){
        for (int x = 0; x < T; x++){
          f = 0;

        for (int v = 0; v < K; v++){
          for (int u = 0; u < K; u++){
            if (u == 0){
              Cu = 1. / sqrt(2);
            } else {
              Cu = 1;
            }

            if (v == 0){
              Cv = 1. / sqrt(2);
            } else { 
              Cv = 1;
            }

            f += 2. / T * Cu * Cv * dct_s.coef[ys + v][xs + u] * cos((2. * x + 1) * u * M_PI / 2. / T) * cos((2. * y + 1) * v * M_PI / 2. / T);
          }
        }

        f = fmin(fmax(f, 0), 255);
        out.at<uchar>(ys + y, xs + x) = (uchar)f;
        }
      }
    }
  }

  return out;
}

// Quantization
dct_str quantization(dct_str dct_s){
  double Q[T][T] = {{16, 11, 10, 16, 24, 40, 51, 61},
                    {12, 12, 14, 19, 26, 58, 60, 55},
                    {12, 12, 14, 19, 26, 58, 60, 55},
                    {14, 17, 22, 29, 51, 87, 80, 62},
                    {18, 22, 37, 56, 68, 109, 103, 77},
                    {24, 35, 55, 64, 81, 104, 113, 92},
                    {49, 64, 78, 87, 103, 121, 120, 101},
                    {72, 92, 95, 98, 112, 100, 103, 99}
                  };

  for (int ys = 0; ys < height; ys += T){
    for (int xs = 0; xs < width; xs += T){
      for(int y = 0; y < T; y++){
        for(int x = 0; x < T; x++){
          dct_s.coef[ys + y][xs + x] = round(dct_s.coef[ys + y][xs + x] / Q[y][x]) * Q[y][x];
        }
      }
    }
  }

  return dct_s;
}


// Compute MSE
double MSE(cv::Mat img1, cv::Mat img2){
  double mse = 0;

  for(int y = 0; y < height; y++){
    for(int x = 0; x < width; x++){
      mse += pow(((double)img1.at<uchar>(y, x) - (double)img2.at<uchar>(y, x)), 2);
    }
  }

  mse /= (height * width);
  return mse;
}

// Compute PSNR
double PSNR(double mse, double v_max){
  return 10 * log10(v_max * v_max / mse);
}

// Compute bitrate
double BITRATE(){
  return T * K * K / T * T;
}

// Main
int main(int argc, const char* argv[]){

  double mse;
  double psnr;
  double bitrate;

  // read original image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  // Fourier coefficient
  dct_str dct_s;

  // output image
  cv::Mat gray = cv::Mat::zeros(height, width, CV_8UC1);
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);

  // BGR -> Gray
  gray = rgb2gray(img);

  // DCT
  dct_s = dct(gray, dct_s);

  // Quantization
  dct_s = quantization(dct_s);

  // IDCT
  out = idct(out, dct_s);

  // MSE, PSNR
  mse = MSE(gray, out);
  psnr = PSNR(mse, 255);
  bitrate = BITRATE();

  std::cout << "MSE: " << mse << std::endl;
  std::cout << "PSNR: " << psnr << std::endl;
  std::cout << "bitrate: " << bitrate << std::endl;
  
  cv::imwrite("out.jpg", out);
  //cv::imshow("answer", out);
  //cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}

