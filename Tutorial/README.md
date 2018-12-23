# Tutorial

ここでは画像処理におけるnumpyの基本的な使い方をいくつか紹介していきます。

**numpy**とはpyhtonで用意されたパッケージ(Cでいうライブラリのようなもの)の一種で、行列演算などを得意としています。

また、画像処理では**OpenCV**というライブラリがあり、様々な処理をAPIかしています。

この問題では、numpyをいじって、OpenCVの処理を自分の手で実現することを目標としています。

pythonでのOpenCVはnumpyをベースとしているため、numpyがいじれる=OpenCVもいじれる　ということになっていきます。


ここからはpyファイルでなく、インタプリタ形式でやってみて下さい。


## Python起動

コマンドプロンプト上で「python」と打って下さい。
すると、こんな感じで >>> と出るはずです。

```bash
(gasyori100) :~/work_space/Gasyori100knock/Tutorial :$ python
Python 3.6.7 |Anaconda, Inc.| (default, Oct 23 2018, 14:01:38) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
## インポート

ここから、パッケージをインストールしていきます。
OpenCVはcv2、numpyはnumpyをそれぞれインポートします。
（numpyはよくnpという名前にエイリアスします。）

```bash
>>> import cv2
>>> import numpy as np
```

## 画像読み込み、表示

画像を読み込むのは以下で行います。

```bash
>>> img = cv2.imread("imori.jpg")
```

これで変数imgに画像情報がnumpy形式で保存されます。

画像のサイズ情報をとるにはimg.shapeを使います。
これは(高さ、横、チャネル)の順になっていて、つまり 縦128ピクセル、横128ピクセル、3チャネル(青、緑、赤)を意味します。

```bash
>>> img.shape
(128, 128, 3)
>>>
```

型をとるには、img.dtypeを使用します。
uint8とは符号なしintで8ビットを意味します。画像はRGB成分がそれぞれ通常0~255の256段階で表現されます。
例えば、赤のピクセルは(R,G,B) = (255, 0, 0)、白は(R,G,B) = (255, 255, 255)です。
画像にする時は必ずこの型にしないと画像がおかしくなってしまいます。（あとで説明します。）

```bash
>>> img.dtype
dtype('uint8')
>>>
```

画像の表示はcv2.imshow()を使います。
cv2.imshow()の第一引数にはウィンドウの名前（特に気にしなくて良い）、第二引数には画像が必要です。

cv2.waitKey(0)はキーボードから何かが入力されるまで画像を表示する、という働きがあります。（もっと気になる人は自分で調べて）

```bash
>>> cv2.imshow('', img); cv2.waitKey(0)
102
>>> 
```

|表示 (imori.jpg)|
|:---:|
|![](imori.jpg)|


例えば、imgの型をfloat32にしてみます。
これはastype()を使えばできます。

```bash
>>> _img = img.astype(np.float32)
```

これを表示すると、こうなります。
つまり型がおかしくなるために表示がおかしくなります。（ただし保存はできます。）
なので、画像をいじる時は、
1. cv2.imreadで読み込む
2. 型を**一度np.float32など小数点型に変換する**
3. 画像をいじる
4. 型を**np.uint8に変換して表示・保存する**
この手順にすることをおすすめします。

```bash
>>> cv2.imshow('', _img); cv2.waitKey(0)
102
>>>
```
|表示 (sample1.png)|
|:---:|
|![](sample1.png)|
