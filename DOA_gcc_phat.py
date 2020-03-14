"""
4ch micを用いたGCC-PHATによる簡易音源方向推定プログラム
"""

import numpy as np
from scipy.io.wavfile import read
import math

tap = 2**10

# Import Sound Sorce
dataB = "/content/DOAtest1_B.wav"
dataF = "/content/DOAtest1_F.wav"
dataL = "/content/DOAtest1_F.wav"
dataR = "/content/DOAtest1_F.wav"

rate, dataB = read(dataB)
_, dataF = read(dataF)
_, dataR = read(dataR)
_, dataL = read(dataL)

SOUND_SPEED = 343.2
MIC_DISTANCE_4 = 0.08127
MAX_TDOA_4 = MIC_DISTANCE_4 / float(SOUND_SPEED)

def gcc_phat(sig, refsig, fs=1, max_tau=None, interp=16):
    '''
    この関数は、一般化相互相関-位相変換（GCC-PHAT）メソッドを使用して、
    信号sigと基準信号refsigの間のオフセットを計算します。
    '''
    
    # FFT長をlen(sig) + len(refsig)以上にする
    n = sig.shape[0] + refsig.shape[0]

    # 一般化相互相関(GCC)フェーズ変換
    SIG = np.fft.rfft(sig, n=n)
    REFSIG = np.fft.rfft(refsig, n=n)
    R = SIG * np.conj(REFSIG)

    cc = np.fft.irfft(R / np.abs(R), n=(interp * n))

    max_shift = int(interp * n / 2)
    if max_tau:
        max_shift = np.minimum(int(interp * fs * max_tau), max_shift)

    cc = np.concatenate((cc[-max_shift:], cc[:max_shift+1])) #相関係数

    # 最大相互相関指数を見つける
    shift = np.argmax(np.abs(cc)) - max_shift

    tau = shift / float(interp * fs) #オフセットを求める
    
    return tau, cc
    
# DataList = [dataF,dataR,dataB,dataL]

def My_get_direction(DataList):
  best_guess = None
  MIC_GROUP_N = 2
  tau = [0] * MIC_GROUP_N
  theta = [0] * MIC_GROUP_N

  for i in range(MIC_GROUP_N):
    tau[i], _ = gcc_phat(DataList[i], DataList[i+2], fs=rate, max_tau=MAX_TDOA_4, interp=1)
    theta[i] = math.asin(tau[i] / MAX_TDOA_4) * 180 / math.pi
      
  if np.abs(theta[0]) < np.abs(theta[1]):
    if theta[1] > 0:
      best_guess = (theta[0] + 360) % 360
    else:
      best_guess = (180 - theta[0])
  else:
    if theta[0] < 0:
      best_guess = (theta[1] + 360) % 360
    else:
      best_guess = (180 - theta[1])

    best_guess = (best_guess + 90 + 180) % 360


  best_guess = (-best_guess + 120) % 360

  return best_guess
  
def main():
  i = 0
  while True:
    data1,data2,data3,data4 = dataF[tap*i:tap*(i+1)],dataR[tap*i:tap*(i+1)],dataB[tap*i:tap*(i+1)],dataL[tap*i:tap*(i+1)]
    DataList=[data1,data2,data3,data4]
    direction = My_get_direction(DataList)
    print(direction)
    i+=1


if __name__ == "__main__":
    main()  
