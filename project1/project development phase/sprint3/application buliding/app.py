import numpy as np
import cv2
import os
from keras.models import load_model 
from flask import Flask, render_template, Response 
import tensorflow as tf
from gtts import gTTS #to convert text to speech
global graph 
global writer
from  skimage.transform import resize
graph = tf.get_default_graph()
writer = None

model = load_model('asl.png1.h5') 

vals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

app = Flask (name

print("[INFO] accessing video stream...") 
vs = cv2.VideoCapture(0) #triggers the local camera

pred=""


#preprocessing the frame captured from camera
def detect(frame):
  img resize(frame, (64,64,1))
  img= np.expand_dims (img, axis=)
 if(np.max(ing)>):
   img = img/255.0 
 with graph.as_default(): 
       prediction model.predict_classes (img)
 print(prediction)
 pred=vals[prediction[0]]
 print (pred) 
 return pred

@app.router('/')
 def index():
     return render_template('index.html')