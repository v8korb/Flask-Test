import cv2
import os
import sys


path=os.path.abspath(__file__);
path2= os.path.dirname(path);

def resize(name, h, w):
	img = cv2.imread(name)
	resize_img = cv2.resize(img, (w, h)) 
	path3, img_name = os.path.split(name)
	filename, file_extension = os.path.splitext(img_name)
	resize_img_name = os.path.join(os.path.join(path3 , 'resize_'+filename+file_extension))
	cv2.imwrite(resize_img_name, resize_img)
	return True

# #Testing
# name = str(sys.argv[1])
# h = int(sys.argv[2])
# w = int(sys.argv[3])
# resize(name, h ,w)

