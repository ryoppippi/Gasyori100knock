# Q 1~10

## Q.1. チャネル入れ替え

画像を読み込み、RGBをBGRの順に入れ替えよ。

画像の赤成分を取り出すには、以下のコードで可能。
cv2.imread()関数ではチャネルがBGRの順になることに注意！
これで変数redにimori.jpgの赤成分のみが入る。

```python
import cv2
img = cv2.imread("imori.jpg")
red = img[:, :, 2].copy()
```

|入力画像 (imori.jpg)|出力画像 (answer_1.jpg)|
|---|---|
|![](imori.jpg)|![](answer_1.jpg)|

答え >> answer_1.py

## Q.2. グレースケール化

画像をグレースケールにせよ。
グレースケールとは、画像の輝度表現方法の一種であり下式で計算される。

Y = 0.2126 R + 0.7152 G + 0.0722 B

|入力画像 (imori.jpg)|出力画像 (answer_2.jpg)|
|---|---|
|![](imori.jpg)|![](answer_2.jpg)|

答え >> answer_2.py

## Q.3. 二値化

画像を二値化せよ。
二値化とは、画像を黒と白の二値で表現する方法である。
ここでは、グレースケールにおいて閾値を128に設定し、下式で二値化する。

```bash
y = { 0 (if y < 128)
     255 (else) 
```

|入力画像 (imori.jpg)|出力画像 (answer_3.jpg)|
|---|---|
|![](imori.jpg)|![](answer_3.jpg)|

答え >> answer_3.py

## Q.4. 大津の二値化

大津の二値化とは判別分析法と呼ばれ、二値化における分離の閾値を自動決定する手法である。
これは”クラス内分散”と”クラス間分散”の比から計算される。


- 閾値t未満をクラス0, t以上をクラス1とする。
- w0, w1 ... 閾値tにより分離された各クラスの画素数の割合 (w0 + w1 = 1を満たす)
- S0^2, S1^2 ... 各クラスの画素値の分散
- M0, M1 ... 各クラスの画素値の平均値

とすると、

```bash
クラス内分散 Sw^2 = w0 * S0^2 + w1 * S1^2
クラス間分散 Sb^2 = w0 * (M0 - Mt)^2 + w1 * (M1 - Mt)^2 = w0 * w1 * (M0 - M1) ^2
画像全体の画素の分散 St^2 = Sw^2 + Sb^2 = (const)
以上より、分離度は次式で定義される。
分離度 X = Sb^2 / Sw^2 = Sb^2 / (St^2 - Sb^2)
```

となるので、

```bash
argmax_{t} X = argmax_{t} Sb^2
```
となる。すなわち、Sb^2 =  w0 * w1 * (M0 - M1) ^2 となる、閾値tを二値化の閾値とすれば良い。

|入力画像 (imori.jpg)|出力画像 (th = 143) (answer_4.jpg)|
|---|---|
|![](imori.jpg)|![](answer_4.jpg)|

答え >> answer_4.py


## Q.5. HSV変換

HSV変換とは、"Hue(色相)"、"Saturation(彩度)"、"Value(明度)"で色を表現する手法である。

- Hue ... 色合いを0~360度で表現し、赤や青など色の種類を示す。 ( 0 <= H < 360)
- Saturation ... 色の鮮やかさ。Saturationが低いと灰色さが顕著になり、くすんだ色となる。 ( 0<= S < 1)
- Value ... 色の明るさ。Valueが高いほど白に近く、Valueが低いほど黒に近くなる。 ( 0 <= V < 1)

RGB -> HSV変換は以下の式で定義される。

R,G,Bが[0, 1]の範囲にあるとする。

```bash
Max = max(R,G,B)
Min = min(R,G,B)

H =  { 0                            (if Min=Max)
       60 x (G-R) / (Max-Min) + 60  (if Min=B)
       60 x (B-G) / (Max-Min) + 180 (if Min=R)
       60 x (R-B) / (Max-Min) + 300 (if Min=G)
       
V = Max

S = Max - Min
```

HSV -> RGB変換は以下の式で定義される。

```bash
C = S

H' = H // 60

X = C (1 - |H' mod 2 - 1|)

(R,G,B) = (V - C) (1,1,1) = { (0, 0, 0)  (if H is undefined)
                              (C, X, 0)  (if 0 <= H' < 1)
                              (X, C, 0)  (if 1 <= H' < 2)
                              (0, C, X)  (if 2 <= H' < 3)
                              (0, X, C)  (if 3 <= H' < 4)
                              (X, 0, C)  (if 4 <= H' < 5)
                              (C, 0, X)  (if 5 <= H' < 6)
```

ここでは色相Hを反転(180を加算)し、RGBに直し画像を表示せよ。

|入力画像 (imori.jpg)|出力画像 (answer_5.jpg)|
|---|---|
|![](imori.jpg)|![](answer_5.jpg)|

答え >> answer_5.py

## 減色処理

ここでは画像の値を256^3から4^3、すなわちR,G,B in {32, 96, 160, 224}の各4値に減色する．
各値に関して、以下の様に定義する。

```bash
val = {  32  (0 <= val < 63)
         96  (63 <= val < 127)
        160  (127 <= val < 191)
        224  (191 <= val < 256)
```
|入力画像 (imori.jpg)|出力画像 (answer_6.jpg)|
|---|---|
|![](imori.jpg)|![](answer_6.jpg)|

答え >> answer_6.py
