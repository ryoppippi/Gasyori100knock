#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

// BGR -> Gray
cv::Mat BGR2GRAY(cv::Mat img){
  // get height and width
  int width = img.cols;
  int height = img.rows;

  // prepare output
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);

  // each y, x
  for (int y = 0; y < height; y++){
    for (int x = 0; x < width; x++){
      // BGR -> Gray
      out.at<uchar>(y, x) = 0.2126 * (float)img.at<cv::Vec3b>(y, x)[2] \
        + 0.7152 * (float)img.at<cv::Vec3b>(y, x)[1] \
        + 0.0722 * (float)img.at<cv::Vec3b>(y, x)[0];
    }
  }

  return out;
}

// Gray -> Binary
cv::Mat Binarize_Otsu(cv::Mat gray){
  int width = gray.cols;
  int height = gray.rows;

  // determine threshold
  double w0 = 0, w1 = 0;
  double m0 = 0, m1 = 0;
  double max_sb = 0, sb = 0;
  int th = 0;
  int val;

  // Get threshold
  for (int t = 0; t < 255; t++){
    w0 = 0;
    w1 = 0;
    m0 = 0;
    m1 = 0;
    for (int y = 0; y < height; y++){
      for (int x = 0; x < width; x++){
        val = (int)(gray.at<uchar>(y, x));

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

  std::cout << "threshold:" << th << std::endl;

  // prepare output
  cv::Mat out = cv::Mat::zeros(height, width, CV_8UC1);

  // each y, x
  for (int y = 0; y < height; y++){
    for (int x = 0; x < width; x++){
      // Binarize
      if (gray.at<uchar>(y, x) > th){
        out.at<uchar>(y, x) = 255;
      } else {
        out.at<uchar>(y, x) = 0;
      }
    
    }
  }

  return out;
}

// Morphology Erode
cv::Mat Morphology_Erode(cv::Mat img, int Erode_time){
  int height = img.cols;
  int width = img.rows;

  // output image
  cv::Mat tmp_img;
  cv::Mat out = img.clone();

  // for erode time
  for (int i = 0; i < Erode_time; i++){
    tmp_img = out.clone();

    // each pixel
    for (int y = 0; y < height; y++){
      for (int x = 0; x < width; x++){
        // check left pixel
        if ((x > 0) && (tmp_img.at<uchar>(y, x - 1) == 255)){
          out.at<uchar>(y, x) = 255;
          continue;
        } 

        // check up pixel
        if ((y > 0) && (tmp_img.at<uchar>(y - 1, x) == 255)){
          out.at<uchar>(y, x) = 255;
          continue;
        }

        // check right pixel
        if ((x < width - 1) && (tmp_img.at<uchar>(y, x + 1) == 255)){
          out.at<uchar>(y, x) = 255;
          continue;
        }

        // check left pixel
        if ((y < height - 1) && (tmp_img.at<uchar>(y + 1, x) == 255)){
          out.at<uchar>(y, x) = 255;
          continue;
        }
      }
    }
  }

  return out;
}

// Morphology Dilate
cv::Mat Morphology_Dilate(cv::Mat img, int Dilate_time){
  int height = img.cols;
  int width = img.rows;

  // output image
  cv::Mat tmp_img;
  cv::Mat out = img.clone();

  // for erode time
  for (int i = 0; i < Dilate_time; i++){
    tmp_img = out.clone();

    // each pixel
    for (int y = 0; y < height; y++){
      for (int x = 0; x < width; x++){
        // check left pixel
        if ((x > 0) && (tmp_img.at<uchar>(y, x - 1) == 0)){
          out.at<uchar>(y, x) = 0;
          continue;
        } 

        // check up pixel
        if ((y > 0) && (tmp_img.at<uchar>(y - 1, x) == 0)){
          out.at<uchar>(y, x) = 0;
          continue;
        }

        // check right pixel
        if ((x < width - 1) && (tmp_img.at<uchar>(y, x + 1) == 0)){
          out.at<uchar>(y, x) = 0;
          continue;
        }

        // check left pixel
        if ((y < height - 1) && (tmp_img.at<uchar>(y + 1, x) == 0)){
          out.at<uchar>(y, x) = 0;
          continue;
        }
      }
    }
  }

  return out;
}

// Morphology opening
cv::Mat Morphology_Opening(cv::Mat img, int open_time){

  // Morphology dilate
  img = Morphology_Dilate(img, open_time);

  // Morphology erode
  img = Morphology_Erode(img, open_time);

  return img;
}


int main(int argc, const char* argv[]){
  // read image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  // BGR -> Gray
  cv::Mat gray = BGR2GRAY(img);

  // Gray -> Binary
  cv::Mat bin = Binarize_Otsu(gray);

  // Morphology Opening
  cv::Mat out = Morphology_Opening(bin, 1);

  //cv::imwrite("out.jpg", out);
  cv::imshow("sample", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
