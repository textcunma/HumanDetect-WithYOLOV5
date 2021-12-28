"""
入力：MP4ファイル
出力：人間を検知したフレーム数
"""
import csv
from detect import detect_main

def main():
    MP4path="./women_long_jump.mp4"      #MP4ファイルのパス名
    conf=0.80       #信頼度確率（値以上）
    result,numFrame=detect_main(MP4path,conf)

    frameinHuman=[]
    frameinHuman+=[0]*(result[0]-1-1)     #人間が初めて検知されたフレーム数よりも前のフレームを全て[0]とする
    for i in range(len(result)-1):
        frameinHuman+=[1]                 # Personラベルが検知されたフレーム番号なので毎回[1]が入る
        start=result[i]
        end=result[i+1]
        if end-start<24:                  #24フレーム以上人間が出てこない場合
            frameinHuman+=[1]*(end-start-1)
        else:
            frameinHuman+=[1]       #start分
            frameinHuman+=[0]*(end-start-1-1)

    frameinHuman+=[1]       #検知された最後のPersonラベルのあるフレーム数を追加
    frameinHuman+=[0]*(numFrame-result[-1])     #Personラベルのフレームの後にあるフレームは全て人間以外なので[0]を追加

    print(frameinHuman)



if __name__ == "__main__":
    main()