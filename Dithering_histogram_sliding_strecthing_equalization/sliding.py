from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Histogram sliding
def hist_slide(img,k):
	height = img.shape[0]
	width = img.shape[1]
	for i in range(height):
		for j in range(width):
			if int(img[i][j]) + k > 255:
				img[i][j] = 255
			elif img[i][j] + k < 0:
				img[i][j] = 0
			else:
				img[i][j] = int(img[i][j])+k

	return img


img = input('Enter image path: ')
k = int(input('Enter k value: '))
Image = cv2.imread(img)
gray_img = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
Image = cv2.imread(img)
gray_img2 = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('GracyImage.PNG', gray_img)
new_img = hist_slide(gray_img,50)
cv2.imwrite('slide_img.png',new_img)
print('Output image is saved as slide_img.png')

vals = gray_img2.flatten()
val1 = new_img.flatten()
b, bins, patches = plt.hist(vals, 255, label='old_image')
# b1, bins1, patches1 = plt.hist(val1, 255, alpha=0.5,label='new_img')
plt.title('Histogram of image of old_image')
plt.xlim([0,255])
plt.legend(loc='upper right')
plt.show()
b1, bins1, patches1 = plt.hist(val1, 255, label='new_img')
plt.title('Histogram of image of new_img')
plt.xlim([0,255])
plt.legend(loc='upper right')
plt.show()