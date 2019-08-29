# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:39:39 2018

@author: timot
"""
import moviepy.editor as mp

filename = "myVideo.mp4"
all_clip = mp.VideoFileClip(filename)

total_duration = all_clip.duration
clipIntro = mp.VideoFileClip(filename).subclip(0,20)
clipOutro = mp.VideoFileClip(filename).subclip(total_duration-20,total_duration)

clipIntro.audio.write_audiofile("audioGeneric.wav")
clipOutro.audio.write_audiofile("audioOutro.wav")
all_clip.audio.write_audiofile("audioAll.wav")