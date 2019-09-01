# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:30:32 2018

@author: timot
"""

# Beat tracking example
import glob
import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression as LR

# 1. Get the file path to the included audio example
filename = "audioGeneric.wav"
#filename = "audioAll.wav"
dt = 1 #Intervalle en seconde

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
def load_sound_file(file_path):
    y, sr = librosa.load(file_path)
    return y, sr

def plot_waves(y,sr):
    plt.figure()
    librosa.display.waveplot(y, sr=sr)
    plt.title('Chronogram')
    
def plot_specgram(y,sr):
    plt.figure()
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    librosa.display.specshow(D, y_axis='linear')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    
def plot_fft(y):
    stft = np.abs(librosa.stft(y))
    plt.figure()
    plt.plot(stft.sum(1))
    plt.title('Magnitude spectrum')
    
def resize(y,dy):
    y = y[:int(len(y)/dy)*dy]
    ym = np.reshape(y,(dy,int(round(len(y)/dy))))
    return ym 
    
# Features
# Zero Crossing Rates
def plot_ZCR(ym):
    ZCR = abs(ym[:,1:]-ym[:,:-1]).sum(1)/2
    plt.figure()
    plt.plot(ZCR)
    plt.ylabel('Number of crossing')
    plt.show()   

def extract_feature(file_name):
    y, sr = librosa.load(file_name)
    stft = np.abs(librosa.stft(y))
    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T,axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sr).T,axis=0)
    mel = np.mean(librosa.feature.melspectrogram(y, sr=sr).T,axis=0)
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sr).T,axis=0)
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(y),
    sr=sr).T,axis=0)
    return mfccs,chroma,mel,contrast,tonnetz

def parse_audio_files(parent_dir, mylabel, file_ext="*.wav"):
    features, labels = np.empty((0,193)), np.empty(0)
    for fn in glob.glob(os.path.join(parent_dir, file_ext)):
        try:
          mfccs, chroma, mel, contrast,tonnetz = extract_feature(fn)
        except Exception as e:
          print ("Error encountered while parsing file: ", fn)
          continue
        ext_features = np.hstack([mfccs,chroma,mel,contrast,tonnetz])
        features = np.vstack([features,ext_features])
        labels = np.append(labels,mylabel)
    return np.array(features), np.array(labels)

def parse_audio_files_timing(parent_dir, file_ext="*.wav"):
    features, labels = np.empty((0,193)), np.empty(0)
    for fn in glob.glob(os.path.join(parent_dir, file_ext)):
        try:
          mfccs, chroma, mel, contrast,tonnetz = extract_feature(fn)
        except Exception as e:
          print ("Error encountered while parsing file: ", fn)
          continue
        ext_features = np.hstack([mfccs,chroma,mel,contrast,tonnetz])
        features = np.vstack([features,ext_features])
        label = fn.split('_')[3].split('.')[0]
        labels = np.append(labels, label)
    return np.array(features), np.array(labels, dtype = np.int)

## Classifieur
def classification_music_voice(X, y):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
    clf = LR()
    clf.fit(x_train, y_train)
    y_predict = clf.predict(x_test)
    print("Score model:", accuracy_score(y_test,y_predict))
    return clf

# Main
if __name__ == "__main__":
    #y, sr = load_sound_file(filename)
    #plot_waves(y,sr)
    #plot_specgram(y,sr)
    #plot_fft(y)
    #mfccs,chroma,mel,contrast,tonnetz = extract_feature(y,sr)
    voice_features, voice_label = parse_audio_files('voice',0)
    music_features, music_label = parse_audio_files('music',1)
    
    features = np.vstack([voice_features,music_features])
    labels = np.append(voice_label,music_label)
    
    clf = classification_music_voice(features,labels)
    
    emission_features, emission_timing = parse_audio_files_timing('audio_emission')
    emission_labels = clf.predict(emission_features) 
    
test = 'audio_emmission_11'
print(test.split('_'))