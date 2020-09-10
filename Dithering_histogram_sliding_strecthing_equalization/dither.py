from PIL import Image
import cv2
import numpy as np

# Dithering using Floyd Steinberg algorithm
img = input('Enter image path: ')
Image = cv2.imread(img)
gray_img = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('GracyImage.PNG', gray_img)
print('Grayscale image is saved as GracyImage.PNG')

height = gray_img.shape[0]
width = gray_img.shape[1]

#Floyd Steinberg algorithm
print('Height:',height,'width:',width)
for i in range(height):
 	for j in range(width):
 		old_value = gray_img[i][j]
 		if int(gray_img[i][j]) < 128:
 			gray_img[i][j] = 0
 		else:
 			gray_img[i][j] = 255
 		error = int(old_value) - int(gray_img[i][j])
 		if(j<width-1):
 			new_val = int(gray_img[i][j+1]) + error*(7/16)
 			if new_val < 0:
 				# print(gray_img[i][j+1])
 				gray_img[i][j+1] = 0
 			elif new_val > 255:
 				gray_img[i][j+1] = 255
 			else:
 				gray_img[i][j+1] = new_val
 		if j>0 and i<height-1:
 			new_val = int(gray_img[i+1][j-1]) + error*(3/16)
 			if new_val < 0:
 				gray_img[i+1][j-1] = 0
 			elif new_val > 255:
 				gray_img[i+1][j-1] = 255
 			else:
 				gray_img[i+1][j-1] = new_val
 		if i<height-1:
 			# print(i)
 			new_val = int(gray_img[i+1][j]) + error*(5/16)
 			if new_val<0:
 				gray_img[i+1][j] = 0
 			elif new_val>255:
 				gray_img[i+1][j] = 255
 			else:
 				gray_img[i+1][j] = new_val
 		if i<height-1 and j<width-1:
 			new_val = int(gray_img[i+1][j+1]) + error*(1/16)
 			if new_val<0:
 				gray_img[i+1][j+1] = 0
 			elif new_val>255:
 				gray_img[i+1][j+1] = 255
 			else:
 				gray_img[i+1][j+1] = new_val
# print(gray_img)
cv2.imwrite('Dither.png',gray_img)
print('Dithered image is saved as Dither.png')



