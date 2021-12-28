# HumanDetect-WithYOLOV5
YOLOV5を用いた人間検知

**input: MP4 file** <br>
**output: result.csv**

YOLO V5を用いて人間を検知し以下の情報をCSVに書き込みます。
- 人間が登場したフレーム番号
- 信頼度スコア

## SET UP
```
git clone --recursive git@github.com:textcunma/HumanDetect-WithYOLOV5.git
```

```
conda create -n yolov5 python=3.8
conda activate yolov5
pip install -U -r yolov5/requirements.txt
pip install pyqt5
pip install opencv-python-headless
```

### ブランチ
- main : CSV出力
- frameMask : 人間がいるフレームは[1]、いないフレームは[0]とするマスクを出力
- nonHuman  : 　人間がいない区間の秒数を出力