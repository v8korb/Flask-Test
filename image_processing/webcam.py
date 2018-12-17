import cv2
import numpy as np
import os
import sys


path=os.path.abspath(__file__);
path2= os.path.dirname(path);
path3= os.path.dirname(path2)+'/tmp/';

def webcam():
	cam = cv2.VideoCapture(0)
	ret, frame = cam.read()
	img_name = path3+'img.png'
	cv2.imwrite(img_name, frame)
	cam.release()
	return True

#def webcam():
	#cam = cv2.VideoCapture(0)
	#i=0;
	#while True:
	#	ret, frame = cam.read()
	#        cv2.imshow("Press ESC to take a picture!", frame)
    #  		 key = cv2.waitKey(10)
	#        if key == 27:
    #    	    break
	#img_name = path3+'img.png'
	#cv2.imwrite(img_name, frame)
	#cv2.destroyAllWindows()
	#cam.release()
	#return True

# #Testing
#a=webcam()
# name = str(sys.argv[1])
# r = int(sys.argv[2])
# g = int(sys.argv[3])
# b = int(sys.argv[4])
# k = int(sys.argv[5])
# binarize(name, r, g, b, k)
