#include <opencv2/opencv.hpp>

static void readImage(){
	cv::Mat image = cv::imread("..\\Tutorial\\imori.jpg");
	cv::imshow("image", image);
	cv::waitKey(0);
}