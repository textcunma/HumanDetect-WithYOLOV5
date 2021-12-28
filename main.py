"""
入力：MP4ファイル
出力：人間を検知したフレーム数
"""
import csv
import cv2
from detect import detect_main

def main():
    MP4path="./women_long_jump.mp4"      #MP4ファイルのパス名
    conf=0.80       #信頼度確率（値以上）
    result,numFrame=detect_main(MP4path,conf)

    cap = cv2.VideoCapture(MP4path)
    fps=cap.get(cv2.CAP_PROP_FPS)

    zeroArea=[]

    if result[0]-1-1>0:
        zeroArea.append([1/fps,(result[0]-1)/fps])      #1フレーム目から

    for i in range(len(result)-1):
        start=result[i]
        end=result[i+1]
        if end-start>24:                  #24フレーム以上人間が出てこない場合
            zeroArea.append([(start+1)/fps,(end-1)/fps])

    if numFrame!=result[-1]:
        zeroArea.append([(result[-1]+1)/fps,numFrame/fps])
    print(zeroArea)



if __name__ == "__main__":
    main()