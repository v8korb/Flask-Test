import cv2
import os
import sys


path=os.path.abspath(__file__);
path2= os.path.dirname(path);

def face_detection(name,scaleF,minNB):
	img = cv2.imread(name)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	haar_face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
	faces = haar_face_cascade.detectMultiScale(gray, scaleFactor=scaleF, minNeighbors=minNB);   
	
	for (x, y, w, h) in faces:     
	         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)       
	
	path3, img_name = os.path.split(name)
	filename, file_extension = os.path.splitext(img_name)
	face_img_name = os.path.join(os.path.join(path3 , 'face_'+filename+file_extension))
	cv2.imwrite(face_img_name, img)
	return True
	#print len(faces)
	#print x, y, w ,h

# #Testing     #
# name = str(sys.argv[1])
# scaleF = float(sys.argv[2])
# minNB = int(sys.argv[3])
# face_detection(name,scaleF,minNB)
# print 'Faces found: ', len(faces)
# print x,y,w,h
