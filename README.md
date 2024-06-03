

# Facial_Emotion_Recognition_python_unity 

by Irmak Ozarslan

This repository is for using Facial Emotion Recognition with Deepface and OpenCV in Unity with a UDP server between Unity and Python.

Thanks to these 2 repositories I was able to develop this repository:

1- Python Unity Socket Communication Created by Youssef Elashry.

2- Facial-Emotion-Recognition-using-OpenCV-and-Deepface by Manish Tipari.

With this, you do not have to pay the OpenCV extension in Unity. Just by changing the code a bit, you can send and receive any data between Python and Unity.

## Steps:


### 1.
 ```sh
pip install -r requirements.txt
```


### 2. Download SplitCam: 
 ```sh
https://splitcam.com


```

Add two medialayers with your webcam (these will be our two virtual cameras, one is accessed by Unity other from python.)


You can change VideoCapture(0) in python emotion recognition to 1 for changing the virtual camera.




### 3. Launch the server in Python: (If you want, change the timing of sending the data.)

run 

 ```sh
server-emotion-recog.py
```


-UdpComms, haarcascade and the python script should be downloaded and put in the same folder.


### 4. In Unity, press play

It already contains a sample scene in Unity. If you press play, you should be able to see your webcam stream and emotion. Emotion data is coded as emotion in the UdpSocket script.



## Notes:

1. Splitcam is needed to stream the video in unity at the same time while python runs in the background. If you do not need the video stream, you do not have to download this. Just change all the cameras to defaul which is [0].

2. Make sure you create a virtual environment in python and install the requirements.txt there.

3. Version : Python: 3.11, OpenCV: 4.9.0 , Unity:2020.3.21f1$

4. If you want to run the application second time, make sure the webcam is not streaming before running, otherwise it won't work.



