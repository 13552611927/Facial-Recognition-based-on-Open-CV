import cv2
import urllib
import time
import os
import urllib.request
import pywin

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:/Users/31598/Desktop/trainer/trainer.yml')
names=['Evan', 'Mom']
warningtime=0

def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode('utf8'))
    return m.hexdigest()

statusStr={}

def warning():
    smsapi = 'http://api.smsbao.com/'
    user = 'ykz13552611927'
    passward = md5('ykz13552611927')
    content = '【ALERT】\nReason: \nLocation:\nTime:'+ time.asctime()
    phone = '13552611927'
    data = urllib.parse.urlencode({'u':user,'p':passward,'m':phone, 'c':content})
    send_url = smsapi + 'sms?' + data
    response = urllib.request.urlopen(send_url)
    the_page = response.read().decode('utf-8')
    print(statusStr[the_page])


def face_detect_demo(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier("C:/Users/31598/PycharmProjects/pythonProject3/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    face = face_detector.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(300,300))
    #face = face_detector.detectMultiScale(gray)
    for x,y,w,h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
        cv2.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0), thickness=1)
        ids, confidence=recognizer.predict(gray[y:y+h,x:x+w])
        #print('id:',id,'confidence:',confidence)
        if confidence>80:
            global warningtime
            warningtime+=1
            if warningtime>100:
                warning()
                warningtime=0
            cv2.putText(img,'unknown',(x+10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),1)
        else:
            cv2.putText(img,str(names[ids-1]),(x+10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),1)
        cv2.imshow('result',img)
        #print('bug:'ids)


if __name__ == '__main__':
    #读取摄像头
    cap = cv2.VideoCapture(0)   #cap = cv.VideoCapture("1.mp4")

    #循环
    while True:
        flag,frame=cap.read()
        if not flag:
            break
        face_detect_demo(frame)
        if ord(" ")==cv2.waitKey(1):
            break
    #释放内存
    cv2.destroyAllWindows()
    #释放摄像头
    cap.release()