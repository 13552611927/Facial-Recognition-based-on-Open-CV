#导入cv模块
import cv2 as cv


#建立检测函数
def face_detect_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #加载分类器
    face_detect = cv.CascadeClassifier("C:/Users/31598/PycharmProjects/pythonProject3/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    face = face_detect.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
    cv.imshow("result",img)

if __name__ == '__main__':
    #读取摄像头
    cap = cv.VideoCapture(0)   #cap = cv.VideoCapture("1.mp4")

    #循环
    while True:
        flag,frame=cap.read()
        if not flag:
            break
        face_detect_demo(frame)
        if ord("q")==cv.waitKey(1):
            break
    #释放内存
    cv.destroyAllWindows()
    #释放摄像头
    cap.release()