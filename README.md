# 画像処理100本ノック!!

English is here  (KuKuXia translates into English, so I appreciate his greate effort https://github.com/KuKuXia)

> https://github.com/KuKuXia/Image_Processing_100_Questions 

画像処理の初学者のための問題１００問ですうう(´；ω；｀)

これはイモリと一緒に画像処理の基本的処理の知識を身に着け、アルゴリズムを理解するための100本ノックです。ここに載っている問題はOpenCVでAPIが用意されているものが殆どですが、**あえてそれを自分の手で実装**してください。解答も載っけてますが、それはあくまで解答です。自分で考えながら実装して下さい。

- **問題の難易度の順番はめちゃくちゃです。なるべくポピュラーなものを採用していますが、ネタ切れであんまり聞かないものもあります笑**
- **内容はいろいろな文献を調べて載っけてるので正しくないものもあるかもしれないので注意して下さい** まちがいがあったらプルリクもらえるととても助かります！！
- 【注意】このページを利用して、または関して生じた事に関しては、私は一切責任を負いません。すべて**自己責任**でお願い致します。

PythonとC++の好きな方でやってみてね♡

## Related

**ディープラーニングのノックはこっち** 
> [ディープラーニング∞本ノック!!](https://github.com/yoyoyo-yo/DeepLearningMugenKnock)

## Recent
- 2019.3.25 Q.31 フーリエ系 Q.36 DCT,  Q.47,48 トップハット変換系を修正
- 2019.3.13 Q95-100 Neural Networkを修正
- 2019.3.8 Questions_01_10 にC++の解答を追加！
- 2019.3.7 TutorialにC++用を追加　そろそろC++用の答えもつくろっかなーと
- 2019.3.5 各Questionの答えをanswersディレクトリに収納
- 2019.3.3 Q.18-22. 一部修正
- 2019.2.26 Q.10. メディアンフィルタの解答を一部修正
- 2019.2.25 Q.9. ガウシアンフィルタの解答を一部修正
- 2019.2.23 Q.6. 減色処理のREADMEを修正
- 2019.1.29 HSVを修正

## まずは

gitをインストールします。そして、端末を開いて、このコマンドを実行します。このコマンドでこのディレクトリを丸ごと自分のパソコンにコピーできます。

```bash
$ git clone https://github.com/yoyoyo-yo/Gasyori100knock.git
```

そしたら、PythonかC++のやりたい方を選んで「**チュートリアル**」に進みましょう！

## [チュートリアル](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Tutorial)

| | 内容 | Python | C++ |
|:---:|:---:|:---:|:---:|
| 1 | インストール |  [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Tutorial) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Tutorial/README_opencv_c_install.md) |
| 2 | 画像読み込み・表示 | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Tutorial#%E7%94%BB%E5%83%8F%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF%E8%A1%A8%E7%A4%BA) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Tutorial/README_opencv_c_install.md#%E7%94%BB%E5%83%8F%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF)
| 3 | 画素をいじる| [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Tutorial#%E7%94%BB%E7%B4%A0%E3%82%92%E3%81%84%E3%81%98%E3%82%8B) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Tutorial/README_opencv_c_install.md#%E7%94%BB%E7%B4%A0%E3%82%92%E3%81%84%E3%81%98%E3%82%8B) 
| 4 | 画像のコピー | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Tutorial#%E7%94%BB%E5%83%8F%E3%81%AE%E3%82%B3%E3%83%94%E3%83%BC) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Tutorial/README_opencv_c_install.md#%E7%94%BB%E5%83%8F%E3%81%AE%E3%82%B3%E3%83%94%E3%83%BC) 
| 5 | 画像の保存 | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Tutorial#%E7%94%BB%E5%83%8F%E3%81%AE%E4%BF%9D%E5%AD%98) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Tutorial/README_opencv_c_install.md#%E7%94%BB%E5%83%8F%E3%81%AE%E4%BF%9D%E5%AD%98) |
| 6 | 練習問題 | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Tutorial#%E7%B7%B4%E7%BF%92)| [✓](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/Tutorial/README_opencv_c_install.md#%E7%B7%B4%E7%BF%92%E5%95%8F%E9%A1%8C)

あとは問題を解いていってください。それぞれのフォルダに問題内容が入っています。問題では assets/imori.jpg を使用して下さい。各フォルダのREADME.mdに問題、解答プログラムがあります。```python answers/answer_@@.py```　とすると解答が出ます。

## 問題

詳細な問題内容は各ディレクトリのREADMEにあります。（ディレクトリで下にスクロールすればあります）
- 解答は簡易化のため、main()などは使用しません。
- numpy中心ですが、numpyの基本知識は自分で調べて下さい。

### [問題1 - 10](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10)

|番号|問題| Python | C++ | |番号|問題| Python | C++ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|1|[チャネル入れ替え](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10#q1-%E3%83%81%E3%83%A3%E3%83%8D%E3%83%AB%E5%85%A5%E3%82%8C%E6%9B%BF%E3%81%88)| [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers/answer_1.py) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers_cpp/answer_1.cpp) | |6| [減色処理](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10#q6-%E6%B8%9B%E8%89%B2%E5%87%A6%E7%90%86) |[✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers/answer_6.py) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers_cpp/answer_6.cpp) 
|2|[グレースケール化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10#q2-%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B9%E3%82%B1%E3%83%BC%E3%83%AB%E5%8C%96) |[✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers/answer_2.py) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers_cpp/answer_2.cpp) | |7| [平均プーリング](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10#q7-%E5%B9%B3%E5%9D%87%E3%83%97%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0) |[✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers/answer_7.py) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers_cpp/answer_7.cpp) 
|3|[二値化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10#q3-%E4%BA%8C%E5%80%A4%E5%8C%96) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers/answer_3.py) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers_cpp/answer_3.cpp)  | |8| [Maxプーリング](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10#q8-max%E3%83%97%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0) |[✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers/answer_8.py) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers_cpp/answer_8.cpp) 
|4|[大津の二値化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10#q4-%E5%A4%A7%E6%B4%A5%E3%81%AE%E4%BA%8C%E5%80%A4%E5%8C%96) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers/answer_4.py) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers_cpp/answer_4.cpp)  | |9| [ガウシアンフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10#q9-%E3%82%AC%E3%82%A6%E3%82%B7%E3%82%A2%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers/answer_9.py) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers_cpp/answer_9.cpp) 
|5|[HSV変換](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10#q5-hsv%E5%A4%89%E6%8F%9B) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers/answer_5.py) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers_cpp/answer_5.cpp) | |10| [メディアンフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10#q10-%E3%83%A1%E3%83%87%E3%82%A3%E3%82%A2%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers/answer_10.py) | [✓](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_01_10/answers_cpp/answer_10.cpp) |

### [問題11 - 20](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
|11| [平滑化フィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20#q11-%E5%B9%B3%E6%BB%91%E5%8C%96%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | |16| [Prewittフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20#q16-prewitt%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | 
|12| [モーションフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20#q12-%E3%83%A2%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | |17| [Laplacianフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20#q17-laplacian%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) |
|13| [MAX-MINフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20#q13-max-min%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | |18| [Embossフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20#q18-emboss%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) |
|14| [微分フィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20#q14-%E5%BE%AE%E5%88%86%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | |19| [LoGフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20#q19-log%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | 
|15| [Sobelフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20#q15-sobel%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | |20| [ヒストグラム表示](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_11_20#q20-%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0%E8%A1%A8%E7%A4%BA)  | 

### [問題21 - 30](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
|21| [ヒストグラム正規化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30#q21-%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0%E6%AD%A3%E8%A6%8F%E5%8C%96) | |26| [Bi-linear補間](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30#q26-bi-linear%E8%A3%9C%E9%96%93) |
|22| [ヒストグラム操作](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30#q22-%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0%E6%93%8D%E4%BD%9C) | |27| [Bi-cubic補間](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30#q27-bi-cubic%E8%A3%9C%E9%96%93) |
| 23| [ヒストグラム平坦化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30#q23-%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0%E5%B9%B3%E5%9D%A6%E5%8C%96) | |28| [アフィン変換(平行移動)](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30#q28-%E3%82%A2%E3%83%95%E3%82%A3%E3%83%B3%E5%A4%89%E6%8F%9B%E5%B9%B3%E8%A1%8C%E7%A7%BB%E5%8B%95) |
| 24| [ガンマ補正](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30#q24-%E3%82%AC%E3%83%B3%E3%83%9E%E8%A3%9C%E6%AD%A3) | |29| [アフィン変換(拡大縮小)](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30#q29-%E3%82%A2%E3%83%95%E3%82%A3%E3%83%B3%E5%A4%89%E6%8F%9B%E6%8B%A1%E5%A4%A7%E7%B8%AE%E5%B0%8F) |
|25| [最近傍補間](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30#q25-%E6%9C%80%E8%BF%91%E5%82%8D%E8%A3%9C%E9%96%93) | |30| [アフィン変換(回転)](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_21_30#q30-%E3%82%A2%E3%83%95%E3%82%A3%E3%83%B3%E5%A4%89%E6%8F%9B%E5%9B%9E%E8%BB%A2) |

### [問題31 - 40](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
|31| [アフィン変換(スキュー)](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40#q31-%E3%82%A2%E3%83%95%E3%82%A3%E3%83%B3%E5%A4%89%E6%8F%9B%E3%82%B9%E3%82%AD%E3%83%A5%E3%83%BC) | | 36| [JPEG圧縮 (Step.1)離散コサイン変換](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40#q36-jpeg%E5%9C%A7%E7%B8%AE-step1%E9%9B%A2%E6%95%A3%E3%82%B3%E3%82%B5%E3%82%A4%E3%83%B3%E5%A4%89%E6%8F%9B) |
|32| [フーリエ変換](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40#q32-%E3%83%95%E3%83%BC%E3%83%AA%E3%82%A8%E5%A4%89%E6%8F%9B) | |37| [PSNR](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40#q37-psnr) |
|33| [フーリエ変換 ローパスフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40#q33-%E3%83%95%E3%83%BC%E3%83%AA%E3%82%A8%E5%A4%89%E6%8F%9B%E3%83%AD%E3%83%BC%E3%83%91%E3%82%B9%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | |38| [JPEG圧縮 (Step.2)DCT+量子化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40#q38-jpeg%E5%9C%A7%E7%B8%AE-step2dct%E9%87%8F%E5%AD%90%E5%8C%96) |
|34| [フーリエ変換 ハイパスフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40#q34-%E3%83%95%E3%83%BC%E3%83%AA%E3%82%A8%E5%A4%89%E6%8F%9B%E3%83%8F%E3%82%A4%E3%83%91%E3%82%B9%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | |39| [JPEG圧縮 (Step.3)YCbCr表色系](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40#q39-jpeg%E5%9C%A7%E7%B8%AE-step3ycbcr%E8%A1%A8%E8%89%B2%E7%B3%BB) |
|35| [フーリエ変換 バンドパスフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40#q35-%E3%83%95%E3%83%BC%E3%83%AA%E3%82%A8%E5%A4%89%E6%8F%9B%E3%83%90%E3%83%B3%E3%83%89%E3%83%91%E3%82%B9%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) | | 40| [JPEG圧縮 (Step.4)YCbCr+DCT+量子化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_31_40#q40-jpeg%E5%9C%A7%E7%B8%AE-step4ycbcrdct%E9%87%8F%E5%AD%90%E5%8C%96) |

### [問題41 - 50](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 41 | [Cannyエッジ検出 (Step.1) エッジ強度](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50#q41-canny%E3%82%A8%E3%83%83%E3%82%B8%E6%A4%9C%E5%87%BA-step1-%E3%82%A8%E3%83%83%E3%82%B8%E5%BC%B7%E5%BA%A6) | | 46 | [Hough変換・直線検出 (Step.3) Hough逆変換](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50#q46-hough%E5%A4%89%E6%8F%9B%E7%9B%B4%E7%B7%9A%E6%A4%9C%E5%87%BA-step3-hough%E9%80%86%E5%A4%89%E6%8F%9B) |
| 42 | [Cannyエッジ検出 (Step.2) 細線化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50#q42-canny%E3%82%A8%E3%83%83%E3%82%B8%E6%A4%9C%E5%87%BA-step2-%E7%B4%B0%E7%B7%9A%E5%8C%96) | | 47 | [モルフォロジー処理(膨張)](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50#q47-%E3%83%A2%E3%83%AB%E3%83%95%E3%82%A9%E3%83%AD%E3%82%B8%E3%83%BC%E5%87%A6%E7%90%86%E8%86%A8%E5%BC%B5) |
| 43 | [Cannyエッジ検出 (Step.3) ヒステリシス閾処理](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50#q43-canny%E3%82%A8%E3%83%83%E3%82%B8%E6%A4%9C%E5%87%BA-step3-%E3%83%92%E3%82%B9%E3%83%86%E3%83%AA%E3%82%B7%E3%82%B9%E9%96%BE%E5%87%A6%E7%90%86) | | 48 | [モルフォロジー処理(収縮)](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50#q48-%E3%83%A2%E3%83%AB%E3%83%95%E3%82%A9%E3%83%AD%E3%82%B8%E3%83%BC%E5%87%A6%E7%90%86%E5%8F%8E%E7%B8%AE) |
| 44| [Hough変換・直線検出 (Step.1) Hough変換](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50#q44-hough%E5%A4%89%E6%8F%9B%E7%9B%B4%E7%B7%9A%E6%A4%9C%E5%87%BA-step1-hough%E5%A4%89%E6%8F%9B) | | 49 | [オープニング処理](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50#q49-%E3%82%AA%E3%83%BC%E3%83%97%E3%83%8B%E3%83%B3%E3%82%B0%E5%87%A6%E7%90%86) |
| 45| [Hough変換・直線検出 (Step.2) NMS](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50#q45-hough%E5%A4%89%E6%8F%9B%E7%9B%B4%E7%B7%9A%E6%A4%9C%E5%87%BA-step2-nms) | | 50 | [クロージング処理](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_41_50#q50-%E3%82%AF%E3%83%AD%E3%83%BC%E3%82%B8%E3%83%B3%E3%82%B0%E5%87%A6%E7%90%86) |

### [問題51 - 60](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 51 | [モルフォロジー勾配](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60#q51-%E3%83%A2%E3%83%AB%E3%83%95%E3%82%A9%E3%83%AD%E3%82%B8%E3%83%BC%E5%8B%BE%E9%85%8D) | | 56 | [テンプレートマッチング NCC](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60#q56-%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%83%9E%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0-ncc) |
| 52 |[トップハット変換](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60#q52-%E3%83%88%E3%83%83%E3%83%97%E3%83%8F%E3%83%83%E3%83%88%E5%A4%89%E6%8F%9B) | | 57 | [テンプレートマッチング ZNCC](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60#q57-%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%83%9E%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0-zncc) |
| 53 | [ブラックハット変換](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60#q53-%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF%E3%83%8F%E3%83%83%E3%83%88%E5%A4%89%E6%8F%9B) | | 58 | [ラベリング 4近傍](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60#q58-%E3%83%A9%E3%83%99%E3%83%AA%E3%83%B3%E3%82%B0-4%E8%BF%91%E5%82%8D) |
| 54 | [テンプレートマッチング SSD](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60#q54-%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%83%9E%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0-ssd) | | 59 | [ラベリング 8近傍](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60#q59-%E3%83%A9%E3%83%99%E3%83%AA%E3%83%B3%E3%82%B0-8%E8%BF%91%E5%82%8D) |
| 55 | [テンプレートマッチング SAD](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60#q55-%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%83%9E%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0-sad) | | 60 | [アルファブレンド](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_51_60#q60-%E3%82%A2%E3%83%AB%E3%83%95%E3%82%A1%E3%83%96%E3%83%AC%E3%83%B3%E3%83%89) |

### [問題61 - 70](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 61 | [4-連結数](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70#q61-4-%E9%80%A3%E7%B5%90%E6%95%B0) | | 66 | [HOG (Step.1) 勾配強度・勾配角度](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70#q66-hog-step1-%E5%8B%BE%E9%85%8D%E5%BC%B7%E5%BA%A6%E5%8B%BE%E9%85%8D%E8%A7%92%E5%BA%A6) |
| 62 | [8-連結数](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70#q62-8-%E9%80%A3%E7%B5%90%E6%95%B0) | | 67 | [HOG (Step.2) 勾配ヒストグラム](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70#q67-hog-step2-%E5%8B%BE%E9%85%8D%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0) |
| 63 | [細線化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70#q63-%E7%B4%B0%E7%B7%9A%E5%8C%96%E5%87%A6%E7%90%86) | | 68 | [HOG (Step.3) ヒストグラム正規化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70#q68-hog-step3-%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0%E6%AD%A3%E8%A6%8F%E5%8C%96) |
| 64**未** | [ヒルディッチの細線化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70#q64-%E3%83%92%E3%83%AB%E3%83%87%E3%82%A3%E3%83%83%E3%83%81%E3%81%AE%E7%B4%B0%E7%B7%9A%E5%8C%96) | | 69 | [HOG (Step.4) 特徴量の描画](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70#q69-hog-step4-%E7%89%B9%E5%BE%B4%E9%87%8F%E3%81%AE%E6%8F%8F%E7%94%BB) |
| 65 | [Zhang-Suenの細線化](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70#q65-zhang-suen%E3%81%AE%E7%B4%B0%E7%B7%9A%E5%8C%96) || 70 | [カラートラッキング](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_61_70#q70-%E3%82%AB%E3%83%A9%E3%83%BC%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0)

### [問題71 - 80](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 71 | [マスキング](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80#q71-%E3%83%9E%E3%82%B9%E3%82%AD%E3%83%B3%E3%82%B0) | | 76 | [顕著性マップ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80#q76-%E9%A1%95%E8%91%97%E6%80%A7%E3%83%9E%E3%83%83%E3%83%97) |
| 72 | [マスキング(カラートラッキングとモルフォロジー)](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80#q72-%E3%83%9E%E3%82%B9%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%AB%E3%83%A9%E3%83%BC%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E3%83%A2%E3%83%AB%E3%83%95%E3%82%A9%E3%83%AD%E3%82%B8%E3%83%BC) | | 77 | [ガボールフィルタ](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80#q77-%E3%82%AC%E3%83%9C%E3%83%BC%E3%83%AB%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF) |
| 73 | [縮小と拡大](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80#q73-%E7%B8%AE%E5%B0%8F%E3%81%A8%E6%8B%A1%E5%A4%A7) | | 78 | [ガボールフィルタの回転](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80#q78-%E3%82%AC%E3%83%9C%E3%83%BC%E3%83%AB%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%81%AE%E5%9B%9E%E8%BB%A2) |
| 74 | [ピラミッド差分による高周波成分の抽出](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80#q74-%E3%83%94%E3%83%A9%E3%83%9F%E3%83%83%E3%83%89%E5%B7%AE%E5%88%86%E3%81%AB%E3%82%88%E3%82%8B%E9%AB%98%E5%91%A8%E6%B3%A2%E6%88%90%E5%88%86%E3%81%AE%E6%8A%BD%E5%87%BA) | | 79 | [ガボールフィルタによるエッジ抽出](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80#q79-%E3%82%AC%E3%83%9C%E3%83%BC%E3%83%AB%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%81%AB%E3%82%88%E3%82%8B%E3%82%A8%E3%83%83%E3%82%B8%E6%8A%BD%E5%87%BA) |
| 75 | [ガウシアンピラミッド](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80#q75-%E3%82%AC%E3%82%A6%E3%82%B7%E3%82%A2%E3%83%B3%E3%83%94%E3%83%A9%E3%83%9F%E3%83%83%E3%83%89) | | 80 | [ガボールフィルタによる特徴抽出](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_71_80#q80-%E3%82%AC%E3%83%9C%E3%83%BC%E3%83%AB%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%81%AB%E3%82%88%E3%82%8B%E7%89%B9%E5%BE%B4%E6%8A%BD%E5%87%BA) |

### [問題81 - 90](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 81 | [Hessianのコーナー検出](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90#q81-hessian%E3%81%AE%E3%82%B3%E3%83%BC%E3%83%8A%E3%83%BC%E6%A4%9C%E5%87%BA) | | 86 | [簡単な画像認識 (Step.3) 評価(Accuracy)](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90#q86-%E7%B0%A1%E5%8D%98%E3%81%AA%E7%94%BB%E5%83%8F%E8%AA%8D%E8%AD%98-step3-%E8%A9%95%E4%BE%A1accuracy) |
| 82 | [Harrisのコーナー検出 (Step.1) Sobel + Gaussian](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90#q82-harris%E3%81%AE%E3%82%B3%E3%83%BC%E3%83%8A%E3%83%BC%E6%A4%9C%E5%87%BA-step1-sobel--gauusian) | | 87 | [簡単な画像認識 (Step.4) k-NN](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90#q87-%E7%B0%A1%E5%8D%98%E3%81%AA%E7%94%BB%E5%83%8F%E8%AA%8D%E8%AD%98-step4-k-nn) |
| 83 | [Harrisのコーナー検出 (Step.2) コーナー検出](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90#q83-harris%E3%81%AE%E3%82%B3%E3%83%BC%E3%83%8A%E3%83%BC%E6%A4%9C%E5%87%BA-step2-%E3%82%B3%E3%83%BC%E3%83%8A%E3%83%BC%E6%A4%9C%E5%87%BA) | | 88 | [K-means (Step.1) 重心作成](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90#q88-k-means-step1-%E9%87%8D%E5%BF%83%E4%BD%9C%E6%88%90) |
| 84 | [簡単な画像認識 (Step.1) 減色化 + ヒストグラム](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90#q84-%E7%B0%A1%E5%8D%98%E3%81%AA%E7%94%BB%E5%83%8F%E8%AA%8D%E8%AD%98-step1-%E6%B8%9B%E8%89%B2%E5%8C%96--%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0) | | 89 | [K-means (Step.2) クラスタリング](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90#q89-k-means-step2-%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%AA%E3%83%B3%E3%82%B0) |
| 85 | [簡単な画像認識 (Step.2) クラス判別](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90#q85-%E7%B0%A1%E5%8D%98%E3%81%AA%E7%94%BB%E5%83%8F%E8%AA%8D%E8%AD%98-step2-%E3%82%AF%E3%83%A9%E3%82%B9%E5%88%A4%E5%88%A5) | | 90 | [K-means (Step.3) 初期ラベルの変更](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_81_90#q90-k-means-step3-%E5%88%9D%E6%9C%9F%E3%83%A9%E3%83%99%E3%83%AB%E3%81%AE%E5%A4%89%E6%9B%B4) |

### [問題91 - 100](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100)

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 91 | [K-meansによる減色処理 (Step.1) 色の距離によるクラス分類](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100#q91-k-means%E3%81%AB%E3%82%88%E3%82%8B%E6%B8%9B%E8%89%B2%E5%87%A6%E7%90%86-step1-%E8%89%B2%E3%81%AE%E8%B7%9D%E9%9B%A2%E3%81%AB%E3%82%88%E3%82%8B%E3%82%AF%E3%83%A9%E3%82%B9%E5%88%86%E9%A1%9E) | | 96 | [ニューラルネットワーク (Step.2) 学習](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100#q96-%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%A9%E3%83%AB%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF-step2-%E5%AD%A6%E7%BF%92) |
| 92 | [K-meansによる減色処理 (Step.2) 減色処理](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100#q92-k-means%E3%81%AB%E3%82%88%E3%82%8B%E6%B8%9B%E8%89%B2%E5%87%A6%E7%90%86-step2-%E6%B8%9B%E8%89%B2%E5%87%A6%E7%90%86) | | 97 | [簡単な物体検出 (Step.1) スライディングウィンドウ + HOG](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100#q97-%E7%B0%A1%E5%8D%98%E3%81%AA%E7%89%A9%E4%BD%93%E6%A4%9C%E5%87%BA-step1-%E3%82%B9%E3%83%A9%E3%82%A4%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%82%A6%E3%82%A3%E3%83%B3%E3%83%89%E3%82%A6--hog) |
| 93 | [機械学習の学習データの用意 (Step.1) IoUの計算](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100#q93-%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AE%E5%AD%A6%E7%BF%92%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E7%94%A8%E6%84%8F-step1-iou%E3%81%AE%E8%A8%88%E7%AE%97) | | 98 | [簡単な物体検出 (Step.2) スライディングウィンドウ + NN](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100#q98-%E7%B0%A1%E5%8D%98%E3%81%AA%E7%89%A9%E4%BD%93%E6%A4%9C%E5%87%BA-step2-%E3%82%B9%E3%83%A9%E3%82%A4%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%82%A6%E3%82%A3%E3%83%B3%E3%83%89%E3%82%A6--nn)
| 94 | [機械学習の学習データの用意 (Step.2) ランダムクラッピング](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100#q94-%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AE%E5%AD%A6%E7%BF%92%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E7%94%A8%E6%84%8F-step2-%E3%83%A9%E3%83%B3%E3%83%80%E3%83%A0%E3%82%AF%E3%83%A9%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0) | | 99 | [簡単な物体検出 (Step.3) Non-Maximum Suppression](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100#q99-%E7%B0%A1%E5%8D%98%E3%81%AA%E7%89%A9%E4%BD%93%E6%A4%9C%E5%87%BA-step3-non-maximum-suppression) |
| 95 | [ニューラルネットワーク (Step.1) ディープラーニングにする](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100#q95-%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%A9%E3%83%AB%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF-step1-%E3%83%87%E3%82%A3%E3%83%BC%E3%83%97%E3%83%A9%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%E3%81%AB%E3%81%99%E3%82%8B) | | 100 | [簡単な物体検出 (Step.4) 評価 Precision, Recall, F-score, mAP](https://github.com/yoyoyo-yo/Gasyori100knock/tree/master/Question_91_100#q100-%E7%B0%A1%E5%8D%98%E3%81%AA%E7%89%A9%E4%BD%93%E6%A4%9C%E5%87%BA-step4-%E8%A9%95%E4%BE%A1-precision-recall-f-score-map) |


## TODO

adaptivebinalizatino, poison image blending

## Citation

```bash
@article{yoyoyo-yoGasyori100knock,
    Author = {yoyoyo-yo},
    Title = {Gasyori100knock},
    Journal = {https://github.com/yoyoyo-yo/Gasyori100knock},
    Year = {2019}
}
```

