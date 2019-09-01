# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:39:39 2018

@author: timot
"""
import moviepy.editor as mp

filename = "myVideo.mp4"
all_clip = mp.VideoFileClip(filename)

total_duration = all_clip.duration
clipIntro = all_clip.subclip(0,10)
clipOutro = all_clip.subclip(total_duration-10,total_duration)

k = 1
for j in range(1,11):
    for i in range(1,6):
        clip = clipIntro.subclip(i,i+5)
        clip.audio.write_audiofile("audioMusic_"+str(k)+".wav")
        
        k = k+1
        clip = clipOutro.subclip(i,i+5)
        clip.audio.write_audiofile("audioMusic_"+str(k)+".wav")
        k = k+1
