from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from copy import deepcopy
from scipy import ndimage

#function to apply filter
def filter(img,mask,size):
	height = img.shape[0]
	width = img.shape[1]
	img = np.insert(img,0,0,axis=1)
	img = np.insert(img,len(img[0]),0,axis=1)
	img = np.insert(img,0,[0],axis=0)
	img = np.insert(img,len(img),[0],axis=0)
	# print(img,'\n',np.array(vert))
	new_img = []
	for i in range(height):
		temp = []
		for j in range(width):
			new_val = 0
			for k in range(size):
				for l in range(size):
					new_val = new_val + int(img[i+k][j+l]) * mask[k][l]
			if new_val > 255:
				new_val = 255
			elif new_val < 0:
				new_val = 0
			temp.append(new_val)
		new_img.append(temp)
			# print(new_val)

	return np.array(new_img)



img = input('Enter image path: ')
k = int(input('Enter kernel size(3,5,7,11)'))
#blur_kernel is used to blur the image to reduce noise
blur_kernel = np.ones((k, k), np.float32) / (k*k)
#sharp_kernel is used to sharpen the image
sharp_kernel = np.full((k,k), -1/9)
sharp_kernel[int(k/2),int(k/2)] = 1
Image = cv2.imread(img)
r, g, b = Image[:,:,0], Image[:,:,1], Image[:,:,2]
gray_img = 0.2989 * r + 0.5870 * g + 0.1140 * b
cv2.imwrite('GracyImage.PNG', gray_img)

print('Blurring the image to reduce noise.....')
blur_img=filter(deepcopy(gray_img),blur_kernel,k)
cv2.imwrite('blurred.png', blur_img)
cv2.imwrite('noise.png', blur_img)
print('Blurred image is saved as blurred.png')
print('Noise reduced image is saved as noise.png')

print('Sharpening the image.....')
sharp_img = filter(deepcopy(gray_img), sharp_kernel,k)
cv2.imwrite('sharpened.png', sharp_img)
print('Sharpened image is stored as sharpened.png')

