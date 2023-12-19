
# ROS 2マイパッケージ
これは、2つのノード間で基本的な通信を行うROS 2のパッケージです。
![test](https://github.com/basiliskv/ros2_mypkg/actions/workflows/test.yml/badge.svg)
## トピック
   このトピックは、`talker` ノードが定期的にカウントと現在時刻をパブリッシュするためのものです。`listener` ノードがこのトピックにサブスクライブし、カウントと現在時刻の文字列を受け取ります。


## 使用方法
   listenerは、talkerから受け取ったカウントと、現在時刻(YYYY-MM-DD HH:MM:SS)を表示します。
   ```bash
    [INFO] [listener]: Listen: 1, Time: 2023-12-13 10:27:21
    [INFO] [listener]: Listen: 2, Time: 2023-12-13 10:27:21
    [INFO] [listener]: Listen: 3, Time: 2023-12-13 10:27:22
   ```

## 実行方法

1. 下記のコマンドを実行して、`talk_listen.launch.py`を使用してトピックのパブリッシャとサブスクライバを同時に起動します。

   ```bash
   $ ros2 launch mypkg talk_listen.launch.py
   ```

   これにより、トピックのパブリッシャ（talker）とサブスクライバ（listener）が同時に起動します。

## ソフトウェア要件

このパッケージを使用するには、以下のソフトウェアが必要です。

- Python 3
- ROS 2

## テスト環境

このパッケージは以下の環境でテストされています。

- Ubuntu 22.04.3 LTS

## ライセンス
  * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
  * このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
      * [https://ryuichiueda.github.io/my_slides/robosys_2022/lesson7.html#/](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson4.html#/)
      * [https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson5.html#/)
      * [https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson6.html#/)
      * [https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10.html#/](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson6.html#/)
      * [https://ryuichiueda.github.io/my_slides/robosys_2022/lesson11.html#/](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson6.html#/)

