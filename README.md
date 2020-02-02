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

filename:Fullpath of wave-format data(monoral, stereo, multi channnel)
return　```floatdata, framerate```

### data, framedata = wavefile.sepalate_read(filename)

wavファイルを読み込み、マルチチャンネルの場合チャンネルごとに分けてリストで出力します

filename:Fullpath of wave-format data(monoral, stereo, multi channnel)
return　```datalist, framerate```
