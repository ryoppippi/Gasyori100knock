# 画像処理100本ノック!!

English is here  >> https://github.com/KuKuXia/Image_Processing_100_Questions 英語に訳してくれた方がいました。(Thanks https://github.com/KuKuXia )

画像処理の初学者のための問題１００問が完成しましたぁぁぁぁぁ（＾ｕ＾）私の修論作品です。

これはイモリと一緒に画像処理の基本的処理の知識を身に着け、アルゴリズムを理解するための100本ノックです。ここに載っている問題はOpenCVでAPIが用意されているものが殆どですが、**あえてそれを自分の手で実装**してください。解答も載っけてますが、それはあくまで解答です。自分で考えながら実装して下さい。

- **問題の難易度の順番はめちゃくちゃです。なるべくポピュラーなものを採用していますが、ネタ切れであんまり聞かないものもあります笑**
- **内容はいろいろな文献を調べて載っけてるので正しくないものもあるかもしれないので注意して下さい**
- 【注意】このページを利用して、または関して生じた事に関しては、私は一切責任を負いません。すべて**自己責任**でお願い致します。


## 環境設定

Python-3.6でやって下さい。(解答はPython-3.6で用意してます)

### 1. Minicondaのインストール

https://conda.io/miniconda.html のサイトからMinicondaをインストールします。これはWindowでもMacOSでも可能です。Minicondaがインストールできたら、端末(Windowでは端末、MacOSではターミナル)を開き、以下コマンドで仮想環境を作成します。

```bash
$ conda create python=3.6 -n gasyori100
```

作成できたら、以下コマンドで仮想環境を動作します。

```bash
$ source actiavte gasyori100
```

するとこうなります。

```bash
(gasyori100) :~/work_space/Gasyori100knock/ :$ 
```

### 2. gitのインストール

gitをインストールします。そして、端末を開いて、以下のコマンドを実行します。このコマンドでこのディレクトリを丸ごと自分のパソコンにコピーできます。

```bash
$ git clone https://github.com/yoyoyo-yo/Gasyori100knock.git
```

### 3. パッケージのインストール

以下のコマンドで必要なパッケージをインストールします。


```bash
$ pip install -r requirement.txt
```

### 4. 画像処理チュートリアル

以下のファイルを作成し sample.py という名前で保存し、実行します。

```python
import cv2

img = cv2.imread("assets/imori.jpg")
cv2.imshow("imori", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

```bash
$ python sample.py
```

これで以下の画像が表示されれば成功です！
何かボタンを押せば消えます。

![](assets/sample.png)

次に画像処理に関するnumpyの扱い方のために**Tutorial**フォルダを見てみて下さい。（もう知ってるという人はスキップして下さい。）

あとは問題を解いていってください。それぞれのフォルダに問題内容が入っています。問題では assets/imori.jpg を使用して下さい。各フォルダのREADME.mdに問題、解答プログラムがあります。python answer_@@.py　とすると解答が出ます。

## 問題

詳細な問題内容は各ディレクトリのREADMEにあります。（ディレクトリで下にスクロールすればあります）
- 解答は簡易化のため、main()などは使用しません。
- numpy中心ですが、numpyの基本知識は自分で調べて下さい。

### [チュートリアル](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Tutorial)

| | 内容 |
|:---:|:---:|
|1| 画像読み込み・表示 |
|2| 画素をいじる |
|3| 画像のコピー |
|4| 画像の保存 |
### [問題1 - 10](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
|1|チャネル入れ替え| |6|減色処理 | |
|2|グレースケール化 | |7|平均プーリング |
|3|二値化 | |8|Maxプーリング | |
|4|大津の二値化 | |9|ガウシアンフィルタ |
|5|HSV変換 | |10|メディアンフィルタ |

### [問題11 - 20](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
|11|平滑化フィルタ | |16|Prewittフィルタ | 
|12|モーションフィルタ | |17|Laplacianフィルタ |
|13|MAX-MINフィルタ | |18|Embossフィルタ |
|14|微分フィルタ | |19|LoGフィルタ | 
|15|Sobelフィルタ | |20|ヒストグラム表示  | 

### [問題21 - 30](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
|21|ヒストグラム正規化 | |26|Bi-linear補間|
|22|ヒストグラム操作 | |27|Bi-cubic補間|
| 23|ヒストグラム平坦化 | |28|アフィン変換(平行移動)|
| 24|ガンマ補正| |29|アフィン変換(拡大縮小)|
|25|最近傍補間| |30|アフィン変換(回転)|

### [問題31 - 40](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
|31|アフィン変換(スキュー)| | 36| JPEG圧縮 (Step.1)離散コサイン変換 |
|32|フーリエ変換 | |37| PSNR|
|33|フーリエ変換 ローパスフィルタ| |38| JPEG圧縮 (Step.2)DCT+量子化|
|34|フーリエ変換 ハイパスフィルタ| |39| JPEG圧縮 (Step.3)YCbCr表色系|
|35|フーリエ変換 バンドパスフィルタ| | 40| JPEG圧縮 (Step.4)YCbCr+DCT+量子化 |

### [問題41 - 50](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 41 | Cannyエッジ検出 (Step.1) エッジ強度 | | 46| Hough変換・直線検出 (Step.3) Hough逆変換 |
| 42 | Cannyエッジ検出 (Step.2) 細線化 | | 47 |モルフォロジー処理(膨張) |
| 43 | Cannyエッジ検出 (Step.3) ヒステリシス閾処理 | | 48 |モルフォロジー処理(収縮) |
| 44| Hough変換・直線検出 (Step.1) Hough変換 | | 49 |オープニング処理 |
| 45| Hough変換・直線検出 (Step.2) NMS | | 50 |クロージング処理 |

### [問題51 - 60](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 51 |モルフォロジー勾配 | | 56 |テンプレートマッチング NCC |
| 52 |トップハット変換 | | 57 |テンプレートマッチング ZNCC |
| 53 |ブラックハット変換 | | 58 |ラベリング 4近傍 |
| 54 |テンプレートマッチング SSD | | 59 |ラベリング 8近傍 |
| 55 |テンプレートマッチング SAD | | 60 |アルファブレンド |

### [問題61 - 70](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 61 | 4-連結数 | | 66 | HOG (Step.1) 勾配強度・勾配角度
| 62 | 8-連結数 | | 67 | HOG (Step.2) 勾配ヒストグラム
| 63 | 細線化 | | 68 | HOG (Step.3) ヒストグラム正規化
| 64**未** | ヒルディッチの細線化 | | 69 | HOG (Step.4) 特徴量の描画
| 65 | Zhang-Suenの細線化 || 70 | カラートラッキング

### [問題71 - 80](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 71 | マスキング | | 76 | 顕著性マップ
| 72 | マスキング(カラートラッキングとモルフォロジー) | | 77 | ガボールフィルタ
| 73 | 縮小と拡大 | | 78 | ガボールフィルタの回転
| 74 | ピラミッド差分による高周波成分の抽出 | | 79 | ガボールフィルタによるエッジ抽出
| 75 | ガウシアンピラミッド | | 80 | ガボールフィルタによる特徴抽出

### [問題81 - 90](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 81 | Hessianのコーナー検出 | | 86 | 簡単な画像認識 (Step.3) 評価(Accuracy) |
| 82 | Harrisのコーナー検出 (Step.1) Sobel + Gaussian | | 87 | 簡単な画像認識 (Step.4) k-NN |
| 83 | Harrisのコーナー検出 (Step.2) コーナー検出 | | 88 | K-means (Step.1) 重心作成 |
| 84 | 簡単な画像認識 (Step.1) 減色化 + ヒストグラム | | 89 | K-means (Step.2) クラスタリング |
| 85 | 簡単な画像認識 (Step.2) クラス判別 | | 90 | K-means (Step.3) 初期ラベルの変更 |

### [問題91 - 100](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 91 | K-meansによる減色処理 (Step.1) 色の距離によるクラス分類 | | 96 | ニューラルネットワーク (Step.2) 学習
| 92 | K-meansによる減色処理 (Step.2) 減色処理 | | 97 | 簡単な物体検出 (Step.1) スライディングウィンドウ + HOG
| 93 | 機械学習の学習データの用意 (Step.1) IoUの計算 | | 98 | 簡単な物体検出 (Step.2) スライディングウィンドウ + NN
| 94 | 機械学習の学習データの用意 (Step.2) ランダムクラッピング | | 99 | 簡単な物体検出 (Step.3) Non-Maximum Suppression
| 95 | ニューラルネットワーク (Step.1) ディープラーニングにする | | 100 | 簡単な物体検出 (Step.4) 評価 Precision, Recall, F-score, mAP


## TODO

adaptivebinalizatino, poison image blending

