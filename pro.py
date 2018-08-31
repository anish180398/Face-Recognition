
import cv2
import smtplib
import numpy as np
import pickle
from time import ctime
time= str(ctime())

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
labels = {"person_name":1}
with open("labels.pickle",'rb') as f:
	og_labels= pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)
content = " has been reached to school"
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(your_mail_id,password)
d={"alexcosta":0,"obama":0,"scott":0}
e={"alexcosta":mail_id1,"obama":mail_id2,"scott":mail_id3}
while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	for (x,y,w,h) in faces:
         
         
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]
         id_, conf = recognizer.predict(roi_gray)
         if conf>=65 and conf <=85:
         	
            #print(id_)
         	
            #print(labels[id_])
            

            font = cv2.FONT_HERSHEY_SIMPLEX
            
            name= labels[id_]
            stud_name= name + content 

         	
            c=d[name]

            
            c+=1

            
            d[name]=c

            
            if c==1:
               mail_id=e[name]
               mail.sendmail(your_mail_id,mail_id,stud_name)

            
            color = (255,255,255)
         	
            stroke = 2
         	
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)

         color=(255,0,0)
         stroke=2
         end_cord_x=x+w
         end_cord_y=y+h
         cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)
         

	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
mail.close()
cap.release()
cv2.destroyAllWindows()
