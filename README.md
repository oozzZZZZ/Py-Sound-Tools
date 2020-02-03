# PySoundTools
Python3 Packages For Sound Signal Processing
自分用ツール

# Preparation
## Required packages

```
pip install numpy
pip install pyaudio
pip install librosa
```

# Contents

## wavefile.py
wavファイルを読み込んだり書き出したり

### data, framerate = wavefile.read(filename)
wavファイルを読み込み、floatで出力します

### data, framedata = wavefile.sepalate_read(filename)
wavファイルを読み込み、マルチチャンネルの場合チャンネルごとに分けてリストで出力します

### wavefile.write(data,filename,ch=1,fs=41000,sampwidth=2)
wavファイルを書き出します

### wavefile.multi_write(datalist,filename,ch=1,fs=41000,sampwidth=2)
データのリストを与えてやればマルチチャンネルのwavファイルを書き出します
チャンネル数はリストのサイズから自動で設定します

### wavefile.wav2npy(channel, wavPath, npyPath):
waveファイルをnumpyファイルに変換して保存

### data = wavefile.binary2float(frames, length, sampwidth)
binary -> int変換

### frames = wavefile.float2binary(data, sampwidth)
float -> binary変換



## measurement.py
実験に使ういろいろ

### whitenoisesignal = measurement.whitenoise(t, fs)
ホワイトノイズ信号を作る
    
    t:time
    fs:framelate
    
### pinknoisesignal = measurement.pinknoise(t, fs)
ピンクノイズ信号を作る
    
    t:time
    fs:framelate
    
### ret = make_sweepsound(A, fs, start_freq, end_freq, sec)
スイープサイン信号を作る
    
    A = 1     #振幅
    fs = 44100 #サンプリング周波数
    start_freq = 20  #始まりの周波数
    end_freq = 20000 #終わりの周波数
    sec = 5   #秒 
    
### signal = pluszero(signal)
信号が2の乗数になるように配列の頭にゼロをつける

### ipls = calIR(sample_signal,rec_signal)
インパルス応答を計算する（sample_signalにスイープサイン信号、rec_signalに応答）

### disp_spectrogram(wav)
スペクトログラム表示
スペクトログラム
