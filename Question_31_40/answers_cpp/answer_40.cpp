#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>
#include <complex>


const int height = 128, width = 128, channel = 3;

// DCT hyper-parameter
int T = 8;
int K = 8;


// DCT coefficient
struct dct_str {
  double coef[height][width][channel];
};

// Discrete Cosine transformation
dct_str dct(cv::Mat img, dct_str dct_s){
  
  double I;
  double F;
  double Cu, Cv;

  for (int ys = 0; ys < height; ys += T){
    for (int xs = 0; xs < width; xs += T){
      for (int c = 0; c < channel; c++){
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
      for (int c = 0; c < channel; c++){
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

// Quantization
dct_str quantization(dct_str dct_s){
  // Q table for Y
  double Q1[T][T] = {{16, 11, 10, 16, 24, 40, 51, 61},
                    {12, 12, 14, 19, 26, 58, 60, 55},
                    {12, 12, 14, 19, 26, 58, 60, 55},
                    {14, 17, 22, 29, 51, 87, 80, 62},
                    {18, 22, 37, 56, 68, 109, 103, 77},
                    {24, 35, 55, 64, 81, 104, 113, 92},
                    {49, 64, 78, 87, 103, 121, 120, 101},
                    {72, 92, 95, 98, 112, 100, 103, 99}
                  };

  // Q table for Cb Cr
  double Q2[T][T] = {{17, 18, 24, 47, 99, 99, 99, 99},
                    {18, 21, 26, 66, 99, 99, 99, 99},
                    {24, 26, 56, 99, 99, 99, 99, 99},
                    {47, 66, 99, 99, 99, 99, 99, 99},
                    {99, 99, 99, 99, 99, 99, 99, 99},
                    {99, 99, 99, 99, 99, 99, 99, 99},
                    {99, 99, 99, 99, 99, 99, 99, 99},
                    {99, 99, 99, 99, 99, 99, 99, 99}
                  };

  for (int ys = 0; ys < height; ys += T){
    for (int xs = 0; xs < width; xs += T){
      for(int y = 0; y < T; y++){
        for(int x = 0; x < T; x++){
          dct_s.coef[ys + y][xs + x][0] = round(dct_s.coef[ys + y][xs + x][0] / Q1[y][x]) * Q1[y][x];
          dct_s.coef[ys + y][xs + x][1] = round(dct_s.coef[ys + y][xs + x][1] / Q2[y][x]) * Q2[y][x];
          dct_s.coef[ys + y][xs + x][2] = round(dct_s.coef[ys + y][xs + x][2] / Q2[y][x]) * Q2[y][x];
        }
      }
    }
  }

  return dct_s;
}


// BGR -> Y Cb Cr
cv::Mat BGR2YCbCr(cv::Mat img, cv::Mat out){
  int width = img.rows;
  int height = img.cols;

  //cv::Mat out = cv::Mat::zeros(height, width, CV_32F);
  
  for (int j = 0; j < height; j ++){
    for (int i = 0; i < width; i ++){
      // Y
      out.at<cv::Vec3b>(j, i)[0] = (int)((float)img.at<cv::Vec3b>(j,i)[0] * 0.114 + \
				  (float)img.at<cv::Vec3b>(j,i)[1] * 0.5870 + \
				  (float)img.at<cv::Vec3b>(j,i)[2] * 0.299);

      // Cb
      out.at<cv::Vec3b>(j, i)[1] = (int)((float)img.at<cv::Vec3b>(j,i)[0] * 0.5 + \
				  (float)img.at<cv::Vec3b>(j,i)[1] * (-0.3323) + \
				  (float)img.at<cv::Vec3b>(j,i)[2] * (-0.1687) + 128);

      // Cr
      out.at<cv::Vec3b>(j, i)[2] = (int)((float)img.at<cv::Vec3b>(j,i)[0] * (-0.0813) + \
				  (float)img.at<cv::Vec3b>(j,i)[1] * (-0.4187) + \
				  (float)img.at<cv::Vec3b>(j,i)[2] * 0.5 + 128);
    }
  }
  return out;
}

// Y Cb Cr -> BGR
cv::Mat YCbCr2BGR(cv::Mat ycbcr, cv::Mat out){

  int width = out.rows;
  int height = out.cols;
  int val;
  
  for (int j = 0; j < height; j ++){
    for (int i = 0; i < width; i ++){
      // R
      val = ycbcr.at<cv::Vec3b>(j, i)[0] + (ycbcr.at<cv::Vec3b>(j, i)[2] - 128) * 1.4102;
      val = fmin(255, fmax(0, val));
      out.at<cv::Vec3b>(j, i)[2] = (uchar)val;

      // G
      val = ycbcr.at<cv::Vec3b>(j, i)[0] - (ycbcr.at<cv::Vec3b>(j, i)[1] - 128) * 0.3441 - (ycbcr.at<cv::Vec3b>(j, i)[2] - 128) * 0.7139;
      val = fmin(255, fmax(0, val));
      out.at<cv::Vec3b>(j, i)[1] = (uchar)val;

      // B
      val = ycbcr.at<cv::Vec3b>(j, i)[0] + (ycbcr.at<cv::Vec3b>(j, i)[1] - 128) * 1.7718;
      val = fmin(255, fmax(0, val));
      out.at<cv::Vec3b>(j, i)[0] = (uchar)val;
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
  cv::Mat ycbcr = cv::Mat::zeros(height, width, CV_32FC3);
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC3);

  // BGR -> Y Cb Cr
  ycbcr = BGR2YCbCr(img, ycbcr);

  // DCT
  dct_s = dct(ycbcr, dct_s);

  // Quantization
  dct_s = quantization(dct_s);

  // IDCT
  ycbcr = idct(ycbcr, dct_s);

  // Y Cb Cr -> BGR
  out = YCbCr2BGR(ycbcr, out);

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

