# Tutorial -C++-

## C++のOpenCVのインストール

Pythonでやりたい人はこっち〜〜 
>> https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Tutorial/README.md

Ubuntu-16.04(18.04でも可)を想定してます。Dockerを使うと便利だと思います。

### パッケージインストール

```bash
$ apt install build-essential cmake checkinstall libgtk-3-dev libjpeg-dev libpng++-dev wget emacs vim sudo
```
### OpenCVのダウンロード

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
### サンプルプログラム

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
$ g++ sample.cpp -o sample -lopencv_core -lopencv_imgcodecs -lopencv_highgui
```

これで、コンパイルが通れば、フォルダ内に *sample* というものができてます。
あとは実行しましょう。

```bash
$ ./sample
```

んでこんなウィンドウが出たら成功です!!

![](assets/sample6.png)

次に画像処理の基本操作を説明していきます。（もう知ってるという人はスキップして、問題に進んでください！）

## 画像読み込み

C++でOepncvを使う時、必ずこれをincludeしなきゃいけません。

```cpp
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
```

画像を読み込むときはこうします。Mat型変数に入れる。opencv系の変数は全てcvという名前の名前空間にあります。

```cpp
cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);
```

画像の高さ、幅を読み取るには、

```cpp
int width = img.rows;
int height = img.cols;
```

## 画像表示

画像の表示にはimshowとwaitKey()を使います。imshowの１つ目の引数は、表示のウィンドウの名前です。今は気にしなくていいです。２つ目の引数は表示したい画像です。なにかキーボードを押すとウィンドウが消えます。

```cpp
cv::imshow("sample", img);
cv::waitKey(0);
cv::destroyAllWindows();
```

![](assets/sample7.png)

## 画素をいじる

画素をいじるにはatメソッドを用いる。これで画素にx=30, y=20の位置にアクセスできます。

```cpp
std::cout << img.at<cv::Vec3b>(30,20) << std::endl;
```

例えば、画像の左上半分を赤にするには、

```cpp
int i = 0, j = 0;
for (i = 0; i < width / 2; i++){
  for (j = 0; j < height / 2; j++){
    img.at<cv::Vec3b>(y,x)[0] = 0;
    img.at<cv::Vec3b>(y,x)[1] = 0;
    img.at<cv::Vec3b>(y,x)[2] = 255;
  }
}
```

![](assets/sample8.png)

ちなみにC++の方では[0, 255]を超える範囲の値を入れると、コンパイル時にオーバーフローのwarningをはいてくれます。

例えば、

```cpp
for(i=0; i<width/2; i++){
  for(j=0; j<height/2; j++){
    img.at<cv::Vec3b>(j, i)[0] = 0;
    img.at<cv::Vec3b>(j, i)[1] = 400;
    img.at<cv::Vec3b>(j, i)[2] = -200;
  }
}
```
として、x=30, y=20の値をとると、

```bash
[0, 144, 56]
```
となる。144 = 400 - 256, 56 = 256 - 200から得られ、画像もあきらかに緑がかっています。

![](assets/sample9.png)

img.at<cv::Vec3b>(j, i)にはunsigned char型で値が入っているので、RGB値を取るには、こんな風にしなきゃいけない。

```cpp
unsigned char tmp = img.at<cv::Vec3b>(j,i);
```

## 画像のコピー 

画像を違う変数にコピーしたいときは、clone()メソッドを使います。

```cpp
cv::Mat img2 = img.clone();
```

## 複数の画像の表示

Opencvで２つ並べた画像を作るにはこんな風に作ります。

```cpp
cv::Mat disp;
cv::Mat tmp[3];
tmp[0] = img;
tmp[1] = cv::Mat (cv::Size(10, height), CV_8UC3, cv::Scalar(0,0,0));
tmp[2] = img2;
cv::hconcat(tmp, 3, disp);

cv::imshow("sample", disp);
cv::waitKey(0);
```

これでこんな表示になる。

![](assets/sample10.png)

## 画像の保存

保存する時は、cv::imwrite()メソッドを使います。

```cpp
cv::imshow("out.jpg", disp);
```

## 練習問題

画像の左半分上のRとBを入れ替えて表示してみましょう。

![](assets/out_practice.jpg)

回答例

```cpp
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

int main(int argc, const char* argv[]){
  cv::Mat img = cv::imread("imori.jpg", cv::IMREAD_COLOR);

  int width = img.rows;
  int height = img.cols;

  cv::Mat out = img.clone();

  for(int i=0; i<width/2; i++){
    for(int j=0; j<height/2; j++){
      unsigned char tmp = out.at<cv::Vec3b>(j, i)[0];
      out.at<cv::Vec3b>(j, i)[0] = out.at<cv::Vec3b>(j, i)[2];
      out.at<cv::Vec3b>(j, i)[2] = tmp;
    }
  }

  cv::imwrite("out.jpg", out);
  cv::imshow("sample", out);
  cv::waitKey(0);
  cv::destroyAllWindows();

  return 0;
}
```

答え >> https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Tutorial/answer.cpp

以上でチュートリアルは終了です。

あとはばんばん問題を解いて下さい！！！！
