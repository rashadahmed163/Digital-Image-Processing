from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Histogram equalization
def hist_equal(img):
	height = img.shape[0]
	width = img.shape[1]
	val = img.flatten()
	pmf = {}
	for i in range(256):
		pmf[i] = 0
	for i in range(height):
		for j in range(width):
			pmf[img[i][j]] += 1
	for i in range(256):
		pmf[i] = pmf[i] / (height * width)
	cdf = {}
	cdf[0] = pmf[0]
	for i in range(1,256):
		cdf[i] = cdf[i-1] + pmf[i]
	new_gray = {}
	for i in range(256):
		new_gray[i] = int(cdf[i]*255)
		if new_gray[i] > 255:
			new_gray[i] = 255
	for i in range(height):
		for j in range(width):
			img[i][j] = new_gray[img[i][j]]

	return img


img = input('Enter image path: ')
Image = cv2.imread(img)
gray_img = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
Image = cv2.imread(img)
gray_img2 = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('GracyImage.PNG', gray_img)
new_img = hist_equal(gray_img)
cv2.imwrite('equal_img.png',new_img)
print('Output image is saved as equal_img.png')

vals = gray_img2.flatten()
val1 = new_img.flatten()
old_contrast = max(vals)  -min(vals)
new_contrast = max(val1) - min(val1)
print("Old contrast: ",old_contrast,'new contrast: ',new_contrast)
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