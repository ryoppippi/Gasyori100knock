#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

// weight function
double h(double t){
  double a = -1;
  if (fabs(t) <= 1){
    return (a + 2) * pow(fabs(t), 3) - (a + 3) * pow(fabs(t), 2) + 1;
  } else if(fabs(t) <= 2){
    return a * pow(fabs(t), 3) - 5 * a * pow(fabs(t), 2) + 8 * a * fabs(t) - 4 * a;
  } 
  return 0;
}

// clip value [*, *] -> [min, max]
int val_clip(int x, int min, int max){
  return fmin(fmax(x, min), max);
}


// bicubic
cv::Mat bicubic(cv::Mat img, double rx, double ry){
  // get height and width
  int width = img.cols;
  int height = img.rows;
  int channel = img.channels();


  // get resized shape
  int resized_width = (int)(width * rx);
  int resized_height = (int)(height * ry);
  int x_before, y_before;
  double dx, dy, wx, wy, w_sum;
  double val;
  int _x, _y;

  // output image
  cv::Mat out = cv::Mat::zeros(resized_height, resized_width, CV_8UC3);

  // bi-cubic interpolation
  for (int y = 0; y < resized_height; y++){
    dy = y / ry;
    y_before = (int)floor(dy);
    
    for (int x = 0; x < resized_width; x++){
      dx = x / rx;
      x_before = (int)floor(dx);
      
      
      for (int c = 0; c < channel; c++){
        w_sum = 0;
        val = 0;

        // bi-cubic computation
        for (int j = -1; j < 3; j++){
          _y = val_clip(y_before + j, 0, height - 1);
          wy = h(fabs(dy - _y));
          
          for (int i = -1; i < 3; i++){
            _x = val_clip(x_before + i, 0, width - 1);
            wx = h(fabs(dx - _x));
            w_sum += wy * wx;
            val += (double)img.at<cv::Vec3b>(_y, _x)[c] * wx * wy;
          }
        }

	      val /= w_sum;

	      val = val_clip(val, 0, 255);

        // assign pixel to new position
	      out.at<cv::Vec3b>(y, x)[c] = (uchar)val;
      }
    }
  }
  return out;
}


int main(int argc, const char* argv[]){
  // read image
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  // bicubic
  cv::Mat out = bicubic(img, 1.5, 1.5);
  
  //cv::imwrite("out.jpg", out);
  cv::imshow("answer", out);
  cv::waitKey(0);
  cv::destroyAllWindows();
 
  return 0;
}
