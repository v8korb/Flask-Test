import cv2
import os
import sys

path=os.path.abspath(__file__);
path2= os.path.dirname(path);

def crop(name, x, y, dx ,dy):
	img = cv2.imread(name)
	crop_img = img[y:y+dy, x:x+dx]
	path3, img_name = os.path.split(name)
	filename, file_extension = os.path.splitext(img_name)
	crop_img_name = os.path.join(os.path.join(path3 , 'crop_'+filename+file_extension))
	cv2.imwrite(crop_img_name, crop_img)
	return True

# #Testing
# name = str(sys.argv[1])
# x = int(sys.argv[2])
# y = int(sys.argv[3])
# dx = int(sys.argv[4])
# dy = int(sys.argv[5])
# crop(name,x,y,dx,dy)

