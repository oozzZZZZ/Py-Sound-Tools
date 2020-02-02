import wave
import numpy as np
import struct

def read(filename):
    #data -> binary data
    with wave.open(filename,mode='rb') as w:
        ch = w.getnchannels()
        samplewidth = w.getsampwidth()
        fs = w.getframerate()
        nframes = w.getnframes()
        frames = w.readframes(nframes)
        
    print(ch,samplewidth,fs,nframes)    
    
    #binary -> float    
    if samplewidth == 2:#16bit
        data = np.frombuffer(frames, dtype='int16')
    
    elif samplewidth == 3:#24bit
        a8 = np.fromstring(frames, dtype=np.uint8)
        tmp = np.empty((nframes, 1, 4), dtype = np.uint8)
        tmp[:, :, :samplewidth] = a8.reshape(-1, 1, samplewidth)
        tmp[:, :, samplewidth:] = (tmp[:, :, samplewidth-1:samplewidth] >> 7) * 255
        data = tmp.view('int32')[:,0,0]
        
    elif samplewidth == 4:#32bit
        data = np.frombuffer(frames, dtype='int32')
    
    #sepalate ch
    if ch !=1:
        list = []
        for i in range(ch):
            chi = data[i::ch]
            list.append(chi)
        data = list
        
    else:
        data=data

    return data,fs

def write(data,filename,ch=1,fs=41000,sampwidth=2):
    data = struct.pack("h" * len(data), *data)
    with wave.open(filename,mode='wb') as w:
        w.setsampwidth(sampwidth)
        w.setnchannels(ch)
        w.setframerate(fs)
        w.writeframes(data)
