# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:39:39 2018

@author: timot
"""
import moviepy.editor as mp

filename = "myVideo.mp4"
all_clip = mp.VideoFileClip(filename)

total_duration = all_clip.duration
clipIntro = all_clip.subclip(0,20)
clipOutro = all_clip.subclip(total_duration-20,total_duration)

k = 1
for i in range(1,17):
    clip = clipIntro.subclip((i-1),(i-1)+5)
    clip.audio.write_audiofile("audio_emmission_"+str(k)+".wav")
    k = k + 1

for i in range(1,17):    
    clip = clipOutro.subclip((i-1),(i-1)+5)
    clip.audio.write_audiofile("audio_emmission_"+str(k)+".wav")
    k = k + 1