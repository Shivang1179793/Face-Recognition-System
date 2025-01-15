import cv2
fd=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
vid=cv2.VideoCapture(0)
while True :
    flag,img=vid.read()
    img_gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # th,img=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    if flag :
        faces=fd.detectMultiScale(img,1.1,5)
        for x,y,w,h in faces: # w=width , h=height. x and y are points.
            cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(255,0,0),thickness=3) 
        cv2.imshow("Webcam_image",img) 
        key=cv2.waitKey(1)
        if key==ord("q") :
            break
    else:
        break
cv2.destroyAllWindows()
vid.release()