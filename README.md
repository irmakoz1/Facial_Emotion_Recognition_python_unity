

# Facial_Emotion_Recognition_python_unity 

###by Irmak Ozarslan

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



