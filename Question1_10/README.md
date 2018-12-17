# 問題 1~10

## 問題1 チャネル入れ替え

画像を読み込み、RGBをBGRの順に入れ替えよ。

画像の赤成分を取り出すには、以下のコードで可能。
cv2.imread()関数ではチャネルがBGRの順になることに注意！
これで変数redにimori.jpgの赤成分のみが入る。

```python
import cv2
img = cv2.imread("assets/imori.jpg")
red = img[:, :, 2].copy()
```

|入力画像|出力画像|
|---|---|
|![](assets/imori.jpg)|![](assets/answer_1.jpg)|

## 問題2
