# Q.11 - 20

## Q.11. 平滑化フィルタ

平滑化フィルタ(3x3)を実装せよ。

平滑化フィルタはフィルタ内の画素の平均値を出力するフィルタである。

|入力 (imori.jpg)|出力 (answers/answer_11.jpg)|
|:---:|:---:|
|![](imori.jpg)|![](answers/answer_11.jpg)|

答え
- Python >> [answers/answer_11.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers/answer_11.py)
- C++ >> [answers_cpp/answer_11.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers_cpp/answer_11.cpp)

## Q.12. モーションフィルタ

モーションフィルタ(3x3)を実装せよ。

モーションフィルタとは対角方向の平均値を取るフィルタであり、次式で定義される。

```bash
  1/3  0   0
[  0  1/3  0 ]
   0   0  1/3
```

|入力 (imori.jpg)|出力 (answers/answer_12.jpg)|
|:---:|:---:|
|![](imori.jpg)|![](answers/answer_12.jpg)|

答え
- Python >> [answers/answer_12.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers/answer_12.py)
- C++ >> [answers_cpp/answer_12.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers_cpp/answer_12.cpp)

## Q.13. MAX-MINフィルタ

MAX-MINフィルタ(3x3)を実装せよ。

MAX-MINフィルタとはフィルタ内の画素の最大値と最小値の差を出力するフィルタであり、**エッジ検出**のフィルタの一つである。
エッジ検出とは画像内の線を検出るすることであり、このような画像内の情報を抜き出す操作を**特徴抽出**と呼ぶ。
エッジ検出では多くの場合、グレースケール画像に対してフィルタリングを行う。

|入力 (imori.jpg)|出力 (answers/answer_13.jpg)|
|:---:|:---:|
|![](imori.jpg)|![](answers/answer_13.jpg)|

答え 
- Python >> [answers/answer_13.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers/answer_13.py)
- C++ >> [answers_cpp/answer_13.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers_cpp/answer_13.cpp)

## Q.14. 微分フィルタ

微分フィルタ(3x3)を実装せよ。

微分フィルタは輝度の急激な変化が起こっている部分のエッジを取り出すフィルタであり、隣り合う画素同士の差を取る。

```bash
    (a)縦方向         (b)横方向
      0 -1  0            0 0 0
K = [ 0  1  0 ]   K = [ -1 1 0 ]
      0  0  0            0 0 0
```

|入力 (imori.jpg)|出力・縦方向 (answers/answer_14_v.jpg)|出力・横方向 (answers/answer_14_h.jpg)|
|:---:|:---:|:---:|
|![](imori.jpg)|![](answers/answer_14_v.jpg)|![](answers/answer_14_h.jpg)|

答え
- Python >>[ answers/answer_14.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers/answer_14.py)
- C++ >> [answers_cpp/answer_14.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers_cpp/answer_14.cpp)

## Q.15. Sobelフィルタ

Sobelフィルタ(3x3)を実装せよ。

ソーベルフィルタ(Sobelフィルタ)は特定方向（縦や横）のエッジのみを抽出するフィルタであり、次式でそれぞれ定義される。

```bash
    (a)縦方向       (b)横方向
       1  2  1           1  0 -1
K = [  0  0  0 ]   K = [ 2  0 -2 ]
      -1 -2 -1           1  0 -1
```

|入力 (imori.jpg)|出力・縦方向 (answers/answer_15_v.jpg)|出力・横方向 (answers/answer_15_h.jpg)|
|:---:|:---:|:---:|
|![](imori.jpg)|![](answers/answer_15_v.jpg)|![](answers/answer_15_h.jpg)|

答え
- Python >> [answers/answer_15.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers/answer_15.py)
- C++ >> [answers_cpp/answer_15.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers_cpp/answer_15.cpp)


## Q.16. Prewittフィルタ

Prewittフィルタ(3x3)を実装せよ。

Prewittフィルタはエッジ抽出フィルタの一種であり、次式で定義される。

```bash
    (a)縦方向          (b)横方向
      -1 -1 -1          -1 0 1
K = [  0  0  0 ]  K = [ -1 0 1 ]
       1  1  1          -1 0 1
```

|入力 (imori.jpg)|出力・縦方向 (answers/answer_16_v.jpg)|出力・横方向 (answers/answer_16_h.jpg)|
|:---:|:---:|:---:|
|![](imori.jpg)|![](answers/answer_16_v.jpg)|![](answers/answer_16_h.jpg)|

答え
- Python >> [answers/answer_16.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers/answer_16.py)
- C++ >> [answers_cpp/answer_16.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers_cpp/answer_16.cpp)

## Q.17. Laplacianフィルタ

Laplacianフィルタを実装せよ。

Laplacian（ラプラシアン）フィルタとは輝度の二次微分をとることでエッジ検出を行うフィルタである。

デジタル画像は離散データであるので、x方向・y方向の一次微分は、それぞれ次式で表される。

```bash
Ix(x,y) = (I(x+1, y) - I(x,y)) / ((x+1)-x) = I(x+1, y) - I(x,y)
Iy(x,y) = (I(x, y+1) - I(x,y)) / ((y+1)-y) = I(x, y+1) - I(x,y)
```

さらに二次微分は、次式で表される。

```bash
Ixx(x,y) = (Ix(x,y) - Ix(x-1,y)) / ((x+1)-x) = Ix(x,y) - Ix(x-1,y)
         = (I(x+1, y) - I(x,y)) - (I(x, y) - I(x-1,y))
         = I(x+1,y) - 2 * I(x,y) + I(x-1,y)
Iyy(x,y) = ... = I(x,y+1) - 2 * I(x,y) + I(x,y-1)
```

これらより、ラプラシアン は次式で定義される。

```bash
D^2 I(x,y) = Ixx(x,y) + Iyy(x,y)
           = I(x-1,y) + I(x,y-1) - 4 * I(x,y) + I(x+1,y) + I(x,y+1)
```

これをカーネル化すると、次のようになる。

```bash
      0  1  0
K = [ 1 -4  1 ]
      0  1  0
```

|入力 (imori.jpg)|出力(answers/answer_17.jpg)|
|:---:|:---:|
|![](imori.jpg)|![](answers/answer_17.jpg)||

答え
- Python >> [answers/answer_17.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers/answer_17.py)
- C++ >> [answers_cpp/answer_17.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers_cpp/answer_17.cpp)

## Q.18. Embossフィルタ

Embossフィルタを実装せよ。

Embossフィルタとは輪郭部分を浮き出しにするフィルタで、次式で定義される。

```bash
      -2 -1  0
K = [ -1  1  1 ]
       0  1  2
```

|入力 (imori.jpg)|出力(answers/answer_18.jpg)|
|:---:|:---:|
|![](imori.jpg)|![](answers/answer_18.jpg)|

答え
- Python >> [answers/answer_18.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers/answer_18.py)
- C++ >> [answers_cpp/answer_198.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers_cpp/answer_18.cpp)

## Q.19. LoGフィルタ

LoGフィルタ(s=3、カーネルサイズ=5)を実装し、*imori_noise.jpg*のエッジを検出せよ。

LoGフィルタとはLaplacian of Gaussianであり、ガウシアンフィルタで画像を平滑化した後にラプラシアンフィルタで輪郭を取り出すフィルタである。

Laplcianフィルタは二次微分をとるのでノイズが強調されるのを防ぐために、予めGaussianフィルタでノイズを抑える。

LoGフィルタは次式で定義される。

```bash
LoG(x,y) = (x^2 + y^2 - s^2) / (2 * pi * s^6) * exp(-(x^2+y^2) / (2*s^2))
```

|入力 (imori_noise.jpg)|出力 (answers/answer_19.jpg) |
|:---:|:---:|
|![](imori_noise.jpg)|![](answers/answer_19.jpg)|

答え 
- Python >> [answers/answer_19.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers/answer_19.py)
- C++ >> [answers_cpp/answer_19.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers_cpp/answer_19.cpp)

## Q.20. ヒストグラム表示

matplotlibを用いて*imori_dark.jpg*のヒストグラムを表示せよ。

ヒストグラムとは画素の出現回数をグラフにしたものである。
matplotlibではhist()という関数がすでにあるので、それを利用する。

|入力 (imori_dark.jpg)|出力 (answers/answer_20.png) |
|:---:|:---:|
|![](imori_dark.jpg)|![](answers/answer_20.png)|

答え >> [answers/answer_20.py](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Question_11_20/answers/answer_20.py)

