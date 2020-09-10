from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Histogram stretching
def hist_stretch(img):
	height = img.shape[0]
	width = img.shape[1]
	val = img.flatten()
	maxv = max(val)
	minv = min(val)
	print('Maximum value: ',maxv,'Minimum value: ',minv)
	for i in range(height):
		for j in range(width):
			new_val = ((img[i][j]-minv) / (maxv-minv))*255
			if new_val > 255:
				img[i][j] = 255
			elif new_val < 0:
				img[i][j] = 0
			else:
				img[i][j] = new_val

	return img


img = input('Enter image path: ')
Image = cv2.imread(img)
gray_img = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
Image = cv2.imread(img)
gray_img2 = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('GracyImage.PNG', gray_img)
new_img = hist_stretch(gray_img)
cv2.imwrite('stretch_img.png',new_img)
print('Output image is saved as stretch_img.png')

vals = gray_img2.flatten()
val1 = new_img.flatten()
old_contrast = max(vals)-min(vals)
new_contrast = max(val1)-min(val1)
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