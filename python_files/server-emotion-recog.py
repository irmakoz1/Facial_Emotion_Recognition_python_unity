# Example of a Python UDP server

import UdpComms as U
import time
import os
import subprocess
import cv2
import time
from deepface import DeepFace
from collections import Counter

#run the classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#start capture
i=0
# Create UDP socket to use for sending (and receiving)
sock = U.UdpComms(udpIP="127.0.0.1", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=True)

#send empty data

while True:
    data = sock.ReadReceivedData() 
    if data != None: # if NEW data has been received since last ReadReceivedData function call
        print(data)
        # read data from unity first in our case
    

 # print new received data

        #if data ==1:
        #script=  os.system('python C:/Users/irmak/Desktop/workspace/python-face-recog-tut/Facial-Emotion-Recognition-using-OpenCV-and-Deepface-main/emotion-recog-30sec.py')
        #put a timer here to update emotion each 30 sec
            #start_time = time.time()
            #capture_duration = 10
    emotions_data=[]

    cap = cv2.VideoCapture(0)
    while True:
            #while( int(time.time() - start_time) < capture_duration ):
            ret, frame = cap.read()
            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert grayscale frame to RGB format
            rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

    # Detect faces in the frame
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
                face_roi = rgb_frame[y:y + h, x:x + w]

        
        # Perform emotion analysis on the face ROI
            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            

    #take the most repeated emotion as output
            def most_frequent(List):
                occurence_count = Counter(List)
                return occurence_count.most_common(1)[0][0]
            
            emotion = result[0]['dominant_emotion']

        #for each in emotion:
            emotion_output=str()
            emotions_data.append(emotion)
            emotion_output =most_frequent(emotions_data)
            sock.SendData(emotion_output)
        #emotion= print(os.system("C:/Users/irmak/Desktop/workspace/python-face-recog-tut/Facial-Emotion-Recognition-using-OpenCV-and-Deepface-main/emotion-recog-30sec.py emotion_output"))
   # sock.SendData('Sent from Python: ' + str(i)) # Send this string to other application change the string as the output of the other script.
    #sock.SendData(emotion)
    #subprocess. check_call(["pkill", "-f", "emotion-recog-30sec.py emotion_output.py"])
            emotion_output=str()
            emotions_data=[]
            time.sleep(10)
            if data==None:
                 time.sleep(360)
                 break
    #cap.release()
    


    
