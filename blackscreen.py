import cv2
import numpy as np
import time
fourcc=cv2.VideoWriter_fourcc(*'XVID')
frame=cv2.resize(frame,(640,480))
image=cv2.resize(image,(640,480))
ouput_file=cv2.VideoWriter('ouput.avi',fourcc,20.0,(640,480))
cap=cv2.VideoCapture(0)
time.sleep(2)
bg='bg.png'
cv2.imshow('bg.png')
hsv=cv2.cv2Color(img,cv2.COLOR_BGR2HSV)
u_black=np.array([104,153,70])
I_black=np.array([30,30,0])

mask=cv2.inRange(hsv,I_black,u_black)
res=cv2.bitwise_and(frame,frame,mask=mask)
f=frame - res
f=np.where(f==0,image,f)
final_output=cv2.addWeighted(mask,res,bg)
cv2.imshow(bg,mask,frame)
cv2.waitKey(1)
cap.release()
final_output.release()
cv2.destroyAllWindows()


