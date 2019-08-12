#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>
#include <complex>


const int height = 128, width = 128, channel = 3;

// DCT hyper-parameter
int T = 8;
int K = 4;

// DCT coefficient
struct dct_str {
  double coef[height][width][channel];
};

// Discrete Cosine transformation
dct_str dct(cv::Mat img, dct_str dct_s){
  double I;
  double F;
  double Cu, Cv;

  for(int ys = 0; ys < height; ys += T){
    for(int xs = 0; xs < width; xs += T){
      for(int c = 0; c < channel; c++){
        for(int v = 0; v < T; v ++){
          for(int u = 0; u < T; u ++){
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
                I = (double)img.at<cv::Vec3b>(ys + y, xs + x)[c];
                F += 2. / T * Cu * Cv * I * cos((2. * x + 1) * u * M_PI / 2. / T) * cos((2. * y + 1) * v * M_PI / 2. / T);
              }
            }

            dct_s.coef[ys + v][xs + u][c] = F;
          }
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
      for(int c = 0; c < channel; c++){
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

                f += 2. / T * Cu * Cv * dct_s.coef[ys + v][xs + u][c] * cos((2. * x + 1) * u * M_PI / 2. / T) * cos((2. * y + 1) * v * M_PI / 2. / T);
              }
            }

            f = fmin(fmax(f, 0), 255);
            out.at<cv::Vec3b>(ys + y, xs + x)[c] = (uchar)f;
          }
        }
      }
    }
  }

  return out;
}

// Compute MSE
double MSE(cv::Mat img1, cv::Mat img2){
  double mse = 0;

  for(int y = 0; y < height; y++){
    for(int x = 0; x < width; x++){
      for(int c = 0; c < channel; c++){
        mse += pow(((double)img1.at<cv::Vec3b>(y, x)[c] - (double)img2.at<cv::Vec3b>(y, x)[c]), 2);
      }
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

  // DCT coefficient
  dct_str dct_s;

  // output image
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  // DCT
  dct_s = dct(img, dct_s);

  // IDCT
  out = idct(out, dct_s);

  // MSE, PSNR
  mse = MSE(img, out);
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

