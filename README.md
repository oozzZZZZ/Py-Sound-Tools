# PySoundTools
Python3 Packages For Sound Signal Processing


# Preparation
## Required packages

```
pip install numpy
pip install pyaudio
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


## measurement.py
