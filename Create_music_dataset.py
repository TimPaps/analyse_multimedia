# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:39:39 2018

@author: timot
"""
import glob
import os
from pydub import AudioSegment
AudioSegment.converter = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\Program Files\\ffmpeg\\bin\\ffprobe.exe"

parent_dir = "tracks"
k = 1
for fn in glob.glob(os.path.join(parent_dir, "*.mp3")):
    sound = AudioSegment.from_file(fn)
    
    for i in range(1,10):
        abstract = sound[20+(i-1)*5:20+i*5]
        abstract.export("audioMusic_"+str(k)+".wav", format="wav")
        k = k+1