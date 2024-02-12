# -*- coding: utf-8 -*-
"""gender identification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dS2HIN8kvsBYruyuJh5X9K6waG8uhofX
"""

from google.colab import drive
drive.mount('/content/drive')

import glob
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

"""Reading wave file"""

wave_file = "/content/drive/MyDrive/dataset1/f0001_us_f0001_00001.wav"

signal,sample_rate = librosa.load(wave_file)

signal

sample_rate

"""Plotting"""

plt.figure(figsize = (14, 5))
librosa.display.waveshow(signal, sr = 1000)

"""Reading Multiple wave files from folder"""

myfolder = "/content/drive/MyDrive/dataset1"
myfolder

def getwavefile(path):
  wave_files = glob.glob(path + "/*.wav")
  plt.figure(figsize = (14, 5))
  for i  in wave_files:
    signal,sample_rate = librosa.load(i)
    librosa.display.waveshow(signal, sr = 1000)

getwavefile(myfolder)

"""DataFrame"""

import pandas as pd
import glob

myfolder = "/content/drive/MyDrive/dataset1"

def getwavfile(path):
  wave_file = glob.glob(path +"/*.wav")
  return wave_file

data = getwavfile(myfolder)

data

wave_file = glob.glob(myfolder +"/*.wav")
names=[]
label_list=[]
for h in wave_file:
  k=h.split("1/")
  names.append(k[1])
  print(k[1][0])
  if k[1][0]=='f':
    label_list.append("Female")
  else:
    label_list.append("male")

names

label_list

df1 = pd.DataFrame(names, columns = ["names"])
df1

df2 = pd.DataFrame(label_list, columns = ["label_list"])
df2

df3 = pd.DataFrame(data, columns = ["wave_file"])
df3

df=pd.concat([df1,df2,df3],axis=1)
df

"""feature extraction:"""

df5 = pd.DataFrame(signal, columns = ['Signals'])
df5

"""Feature Extraction:"""

import scipy
_path = "/content/drive/MyDrive/dataset1"

meanlist=[]
stdlist=[]
maxvlist=[]
type_list= []
n_list= []

wavefiles=glob.glob(_path+"/*.wav")
# print(wavefiles)

meanlist=[]

stdlist=[]
maxvlist=[]
type_list= []
n_list= []
minvlist = []
medianlist =[]
modelist = []
skew_list=[]
kurt_list=[]
q1_list =[]
q3_list=[]
iqr_list = []

n_list = []
j_list = []
s_list = []
h_list = []

for wav_file in  wavefiles :
  sound = parselmouth.Sound(wav_file) # sound object from wav file
  pitch = sound.to_pitch()
  pulses = parselmouth.praat.call([sound, pitch], "To PointProcess (cc)")

        # name analysis
  name = os.path.basename(wav_file).split(".")[0]

       # jitter
  jitter_local = parselmouth.praat.call(pulses, "Get jitter (local)", 0.0, 0.0, 0.0001, 0.02, 1.3) * 100

        # shimmer
  shimmer_local = parselmouth.praat.call([sound, pulses], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6)

        # HNR
  harmonicity = parselmouth.praat.call(sound, "To Harmonicity (cc)", 0.01, 75, 0.1, 1.0)
  hnr = parselmouth.praat.call(harmonicity, "Get mean", 0, 0)

        # Append to numpy array
  n_list.append(name)
  j_list.append(jitter_local)
  s_list.append(shimmer_local)
  h_list.append(hnr)

  if jitter_local >2.10:
    type_list.append("1")
  else:
    type_list.append("0")

  x, sr = librosa.load(wav_file)
  freqs = np.fft.fftfreq(x.size)






  mean = 0
  std = 0
  maxv = 0
  minv = 0
  median = 0
  mode = 0
  skew = 0
  kurt = 0
  q1 = 0
  q3 = 0
  iqr = 0


  mean = np.mean(freqs)
  std = np.std(freqs)
  maxv = np.amax(freqs)
  minv = np.amin(freqs)
  median = np.median(freqs)
  mode = scipy.stats.mode(freqs)[0][0]
  skew = scipy.stats.skew(freqs)
  kurt = scipy.stats.kurtosis(freqs)
  q1 = np.quantile(freqs, 0.25)
  q3 = np.quantile(freqs, 0.75)
  iqr = scipy.stats.iqr(freqs)

  meanlist.append(mean)
  stdlist.append(std)
  maxvlist.append(maxv)
  minvlist.append(minv)
  medianlist.append(median)
  modelist.append(mode)
  skew_list.append(skew)
  kurt_list.append(kurt)
  q1_list.append(q1)
  q3_list.append(q3)

  iqr_list.append(iqr)

import pandas as pd
def get_voice_data(_path):




  return meanlist,stdlist,maxvlist,minvlist,medianlist, modelist, skew_list, kurt_list,q1_list,iqr_list,n_list,j_list, s_list, h_list

meanlist,stdlist,maxvlist,minvlist,medianlist,modelist, skew_list, kurt_list,q1_list,iqr_list,n_list,j_list, s_list, h_list   = get_voice_data(_path)

cols=["meanlist","stdlist","maxvlist","minvlist","medianlist","modelist", "skew_list", "kurt_list","q1_list","iqr_list", "n_list","j_list", "s_list", "h_list" ]

mean=pd.DataFrame(meanlist, columns = ['Mean'])
std=pd.DataFrame(stdlist, columns = ['Std'])
max=pd.DataFrame(maxvlist, columns = ['Max'])
min=pd.DataFrame(minvlist, columns = ['Min'])
median=pd.DataFrame(medianlist, columns = ['Median'])
mode_ = pd.DataFrame(modelist, columns = ['Mode'])
skew_ = pd.DataFrame(skew_list, columns = ['Skew'])
kurt_ = pd.DataFrame(kurt_list, columns = ['Kurt'])
q1_ = pd.DataFrame(q1_list, columns = ['Q1'])
iqr_ = pd.DataFrame(iqr_list, columns = ['IQR'])
nlist = pd.DataFrame(n_list, columns = ['Name'])
jlist = pd.DataFrame(j_list, columns = ['Jitter'])
slist = pd.DataFrame(s_list, columns = ['Shimmer'])
hlist = pd.DataFrame(h_list, columns = ['HNR'])


Feature = pd.concat([mean, std,max,min,median, mode_,skew_,kurt_, q1_,iqr_, jlist,slist,hlist,df2], axis = 1)

df2

for column in df2.columns:
    plt.hist(df2[column])
    plt.show()

Feature

"""DataFrame to CSV file"""

csv_data = Feature.to_csv(header = True)
Feature.to_csv("/content/drive/MyDrive/feature.csv")

csvFile = pd.read_csv('/content/drive/MyDrive/feature.csv')
metadata=pd.DataFrame(csvFile)

df2

pip install praat-parselmouth

import glob
import parselmouth
import scipy
import os
from sklearn.model_selection import train_test_split

"""Model Building"""

X = Feature.iloc[:,:-1]
y = Feature.label_list

X

X_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state = 1)

X_train.shape

x_test.shape

y_train.shape

y_test.shape

wave_file = glob.glob(myfolder +"/*.wav")

"""Using SVM"""

def score(model):
    print("Training score: ",model.score(X_train,y_train))
    print("Test score: ",model.score(x_test,y_test))

from sklearn.svm import SVC

SVMmodel = SVC(kernel = 'rbf', C=2.0,random_state=0,degree = 3)
SVMmodel.fit(X_train,y_train)
ypred3 = SVMmodel.predict(x_test)
score(SVMmodel)

"""Using Decision Tree"""

from sklearn.tree import DecisionTreeClassifier

DTmodel = DecisionTreeClassifier(min_samples_split = 5,max_depth = 10,random_state = 0)

DTmodel.fit(X_train,y_train)

ypred1 = DTmodel.predict(x_test)
ypred1[:5]

score(DTmodel)

# eval(ypred1,y_test)

""" LogisticRegression¶"""

from sklearn.linear_model import LogisticRegression

LRmodel = LogisticRegression(n_jobs=3,max_iter=1000,random_state=0)

LRmodel.fit(X_train,y_train)

ypred2 = LRmodel.predict(x_test)

score(LRmodel)

# eval(ypred2,y_test)

"""Using  K-Nearest Neighbors"""

from sklearn.neighbors import KNeighborsClassifier

Kmodel = KNeighborsClassifier(n_neighbors = 50,metric ='minkowski',p=1,n_jobs=5,algorithm='ball_tree')

Kmodel.fit(X_train,y_train)

ypred4 = Kmodel.predict(x_test)

score(Kmodel)

"""Precision and recall"""

from sklearn .metrics import accuracy_score
print(accuracy_score(y_test, ypred3))

from sklearn import metrics

from sklearn import metrics
print( metrics.classification_report(y_test, ypred3))