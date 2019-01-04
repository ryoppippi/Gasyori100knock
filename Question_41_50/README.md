# Q. 41 - 50

## Q.41. **Cannyエッジ検出** (Step.1) エッジ強度

Q.41 - 43 ではエッジ検出手法の一つであるCanny法の理論となる。

Canny法は、
1. ガウシアンフィルタを掛ける
2. x, y方向のSobelフィルタを掛け、それらからエッジ強度とエッジ勾配を求める
3. エッジ勾配の値から、Non-maximum suppression によりエッジの細線化を行う
4. ヒステリシスによる閾値処理を行う

以上により、画像からエッジ部分を抜き出す手法である。

ここでは、1と2の処理を実装する。

処理手順は、
1. 画像をグレースケール化する
2. ガウシアンフィルタ(5x5, s=1.4)をかける
3. x方向、y方向のsobelフィルタを掛け、画像の勾配画像fx, fyを求め、勾配強度と勾配角度を次式で求める。

```bash
勾配強度 edge = sqrt(fx^2 + fy^2)
勾配角度 tan = arctan(fy / fx)
```

4. 勾配角度を次式に沿って、量子化する。

```bash
angle = {   0  (if -0.4142 < tan <= 0.4142)
           45  (if  0.4142 < tan < 2.4142)
           90  (if  |tan| >= 2.4142)
          135  (if -2.4142 < tan <= -0.4142)
```

|入力 (imori.jpg) |出力(勾配強度) (answer_41_1.jpg)|出力(勾配角度) (answer_41_2.jpg)|
|:---:|:---:|:---:|
|![](imori.jpg)|![](answer_41_1.jpg)|![](answer_41_2.jpg)|

答え >> answer_41.py

## Q.42. **Cannyエッジ検出** (Step.2) 細線化

ここでは3を実装する。

Q.41で求めた勾配角度から、Non-maximum suppressionを行い、エッジ線を細くする（細線化）。

Non-maximum suppression(NMS)とは非最大値以外を除去する作業の総称である。（他のタスクでもこの名前はよく出る）

ここでは、注目している箇所の勾配角度の法線方向の隣接ピクセルの３つの勾配強度を比較して、最大値ならそのまま値をいじらずに、最大値でなければ強度を0にする、

つまり、勾配強度edge(x,y)に注目している際に、勾配角度angle(x,y)によって次式のようにedge(x,y)を変更する。

```bash
if angle(x,y)  = 0
 if edge(x,y), edge(x-1,y), edge(x+1,y)で edge(x,y)が最大じゃない
  then edge(x,y) = 0
if angle(x,y)  = 45
 if edge(x,y), edge(x-1,y+1), edge(x+1,y-1)で edge(x,y)が最大じゃない
  then edge(x,y) = 0
if angle(x,y)  = 90
 if edge(x,y), edge(x,y-1), edge(x,y+1)で edge(x,y)が最大じゃない
  then edge(x,y) = 0
if angle(x,y)  = 135
 if edge(x,y), edge(x-1,y-1), edge(x+1,y+1)で edge(x,y)が最大じゃない
  then edge(x,y) = 0
```

|入力 (imori.jpg) |出力 (answer_42.jpg)|
|:---:|:---:|
|![](imori.jpg)|![](answer_42.jpg)|

答え >> answer_42.py

## Q.43. **Cannyエッジ検出** (Step.3) ヒステリシス閾処理

ここでは4を実装する。これがCanny法の最後である。

ここでは、閾値により勾配強度の二値化を行うがCanny法では二つの閾値(HT: high thoresholdとLT: low threshold)を用いる。

はじめに、
1. 勾配強度edge(x,y)がHTより大きい場合はedge(x,y)=255
2. LTより小さい場合はedge(x,y)=0
3.  LT < edge(x,y) < HTの時、周り８ピクセルの勾配強度でHTより大きい値が存在すれば、edge(x,y)=255

ここでは、HT=100, LT=30とする。ちなみに閾値の値は結果を見ながら判断するしかない。

以上のアルゴリズムによって、Canny法が行われる。

|入力 (imori.jpg) |出力 (answer_43.jpg)|
|:---:|:---:|
|![](imori.jpg)|![](answer_43.jpg)|

答え >> answer_43.py

## Q.44. **Hough変換・直線検出** (Step.1) Hough変換

Q.44 - 46 ではHough変換を用いた直線検出を行う。

Hough変換とは、座標を変換することにより数式に沿って直線や円など一定の形状を検出する手法である。

方法としては、
1. エッジ画像からエッジのピクセルにおいてHough変換を行う。
2. Hough変換後の値をヒストグラムをとり、極大点を選ぶ。
3. 極大点のr, tの値をHough逆変換して検出した直線のパラメータを得る。

となる。

ここでは、1のHough変換を行いヒストグラムを作成する。

アルゴリズムは、

1. 画像の対角線の長さrmaxを求める
2. エッジ箇所(x,y)において、t = 0-180で一度ずつtを変えながら、次式によりhough変換を行う

```bash
r = x * cos(t) + y * sin(t)
```
3. t x rmaxのサイズの表を用意し、1で得たtable(t, r) に1を足す

これはすなわち投票(ボーディング)であり、一定の箇所に投票が集中する。

今回は*torino.jpg*を用いて、ボーディングした表を図示せよ。
Cannyのパラメータは, gaussian filter(5x5, s=1.4), HT = 100, LT = 30で使用せよ。

|入力 (imori.jpg) |出力 (answer_44.jpg)|
|:---:|:---:|
|![](imori.jpg)|![](answer_44.jpg)|

答え >> answer_44.py

## Q.45. **Hough変換・直線検出** (Step.2) NMS

ここでは2を実装する。

Q.44で得られた表では、ある一定の箇所付近に多く投票される。
ここでは、その付近の極大値を抜き出す操作を行え。

今回はボーディングが多い箇所を上位10個抜き出し、図示せよ。

NMSのアルゴリズムは、
1. 表において、周囲8マス(8近傍)より注目ピクセルの得票数が多ければそのまま。
2. 注目ピクセルの値が少なければ0にする。

|入力 (imori.jpg) |出力 (answer_45.jpg)|
|:---:|:---:|
|![](imori.jpg)|![](answer_45.jpg)|

答え >> answer_45.py

## Q.46. **Hough変換・直線検出** (Step.3) Hough逆変換

ここではQ.45.で得られた極大値をHough逆変換をして直線を描画する。これで、Hough変換による直線検出が完了する。

アルゴリズムは、
1. 極大点(r, t)を次式で逆変換する。

```bash
y = - cos(t) / sin(t) * x + r / sin(t)
x = - sin(t) / cos(t) * y + r / cos(t)
```

2. 1の逆変換を極大点ごとにy = 0 - H-1, x = 0 - W-1 で行い、入力画像に検出した直線を描画せよ。
ただし、描画するのは赤線(R,G,B) = (255, 0, 0)とする。

|入力 (imori.jpg) |出力 (answer_46.jpg)|
|:---:|:---:|
|![](imori.jpg)|![](answer_46.jpg)|

答え >> answer_46.py
