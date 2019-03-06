# C++のOpenCVのインストール

Ubuntu-16.04(18.04でも可)を想定してます。Dockerを使うと便利だと思います。

## パッケージインストール

```bash
$ apt install build-essential cmake checkinstall libgtk-3-dev libjpeg-dev libpng++-dev wget emacs vim sudo
```
## OpenCVのダウンロード

```bash
$ mkdir opencv
$ cd oepncv
$ wget https://github.com/opencv/opencv/archive/3.4.0.tar.gz
$ tar zxvf 3.4.0.tar.gz
$ cd opencv-3.4.0
$ mkdir build
$ cd build
$ cmake ..
$ make -j4
$ make install
```
## サンプルプログラム

以下をsample.cppとして保存

```cpp
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

int main(int argc, const char* argv[]){
    cv::Mat redImg(cv::Size(320, 240), CV_8UC3, cv::Scalar(0, 0, 255));
    cv::namedWindow("red", cv::WINDOW_AUTOSIZE);

    cv::imshow("red", redImg);
    cv::waitKey(0);

    cv::destroyAllWindows();

    return 0;
}
```

次にコンパイル

```bash
$ g++ sample.cpp -o sample  \
               -lopencv_core -lopencv_imgcodecs -lopencv_highgui
```

これで、コンパイルが通れば、フォルダ内に *sample* というものができてます。
あとは実行しましょう。

```bash
$ ./sample
```

んでこんなウィンドウが出たら成功です!!

![](assets/sample.6)
