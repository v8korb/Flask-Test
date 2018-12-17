import cv2
import numpy as np
import os
import sys


path=os.path.abspath(__file__);
path2= os.path.dirname(path);


def binarize(name, r, g, b, k):
	img = cv2.imread(name)
	shape = img.shape
	binarize_img = np.zeros((shape[0],shape[1],1), np.uint8)
	for i in range(0, shape[0]):
		for j in range(0, shape[1]):
			binarize_img[i][j]=int((img[i,j,0]*r + img[i,j,1]*g + img[i,j,2]*b) > k);

	path3, img_name = os.path.split(name)
	filename, file_extension = os.path.splitext(img_name)
	binarize_img_name = os.path.join(os.path.join(path3 , 'binarize_'+filename+file_extension))
	cv2.imwrite(binarize_img_name, binarize_img)
	return True


# #Testing
# name = str(sys.argv[1])
# r = int(sys.argv[2])
# g = int(sys.argv[3])
# b = int(sys.argv[4])
# k = int(sys.argv[5])
# binarize(name, r, g, b, k)
