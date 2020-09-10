from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math 

#Negative image tranformation
def neg_trans(img):
	height = img.shape[0]
	width = img.shape[1]
	for i in range(height):
		for j in range(width):
			img[i][j] = 255 - int(img[i][j])

	return img

#Logarithmic image transformation
def log_trans(img):
	height = img.shape[0]
	width = img.shape[1]
	val = img.flatten()
	maxv = max(val)
	c = 255/(math.log(1+maxv))
	for i in range(height):
		for j in range(width):
			new_val = int(c * (math.log( 1 + int(img[i][j]) ) ) )
			if new_val > 255:
				new_val = 255
			img[i][j] = new_val

	return img


img = input('Enter image path: ')
Image = cv2.imread(img)
gray_img = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('GracyImage.PNG', gray_img)
neg_img = neg_trans(gray_img)
cv2.imwrite('neg_img.png',neg_img)
print("Negative transformed image is saved as new_img.png.")
log_img = log_trans(gray_img)
cv2.imwrite('log_img.png',log_img)
print("Log-transformation output image is saved as log_img.png.")

