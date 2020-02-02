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
        
    return data,fs

def sepalate_read(filename):
    #data -> binary data
    with wave.open(filename,mode='rb') as w:
        ch = w.getnchannels()
        samplewidth = w.getsampwidth()
        fs = w.getframerate()
        nframes = w.getnframes()
        frames = w.readframes(nframes)   
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

def multi_write(datalist,filename,ch=1,fs=41000,sampwidth=2):
    out = []
    for i in range(len(datalist[0])):
        for j in range(len(datalist)):
            ch = datalist[j]
            out=np.append(out,ch[i])   
    data = np.array(out)
    data = struct.pack("h" * len(data), *data)
    with wave.open(filename,mode='wb') as w:
        w.setsampwidth(sampwidth)
        w.setnchannels(ch)
        w.setframerate(fs)
        w.writeframes(data)

def wav2npy(channel, wavPath, npyPath):
	"""
	convert .wav to .npy, only for multi channel

	"""
	for i in range(channel):
		if i == 0:
			source = np.load("%s/%02d.wav"%(wavPath, i+1))
		else:
			source = np.concatenate((source, np.load("%s/%02d.wav"%(wavPath, i+1))), axis=1)
	np.save("%s/sound.npy"%(npyPath))
