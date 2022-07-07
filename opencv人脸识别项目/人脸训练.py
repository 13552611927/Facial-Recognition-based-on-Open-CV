import os
import cv2
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    facesSamples = []
    ids = []
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    face_detector = cv2.CascadeClassifier('C:/Users/31598/PycharmProjects/pythonProject3/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    for imagePath in imagePaths:
        PIL_img=Image.open(imagePath).convert('L')
        img_numpy=np.array(PIL_img,'uint8')
        faces = face_detector.detectMultiScale(img_numpy)
        id = int(os.path.split(imagePath)[1].split('.')[0])
        for x,y,w,h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y+h,x:x+w])
        print("id:",id)
        print("fs:",facesSamples)
    return facesSamples, ids

if __name__ == '__main__':
    path = 'C:/Users/31598/Desktop/CVSHOTS/'
    faces, ids = getImageAndLabels(path)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))
    recognizer.write('C:/Users/31598/Desktop/trainer/trainer.yml')