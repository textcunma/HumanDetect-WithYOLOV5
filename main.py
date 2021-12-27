"""
入力：MP4ファイル
出力：人間を検知したフレーム数
"""
import csv
from detect import detect_main

def main():
    MP4path="./women_long_jump.mp4"      #MP4ファイルのパス名
    conf=0.80       #信頼度確率（値以上）
    result=detect_main(MP4path,conf)

    with open('result.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["frame","Conf Score"])
        for r in result:
            frame=r[0]
            object,score=r[1].split()
            if object=="person":
                writer.writerow([frame,score])

if __name__ == "__main__":
    main()