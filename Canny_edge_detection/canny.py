from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from copy import deepcopy
from scipy import ndimage

#create gaussian filter
def gauss_kernel(size, sigma=1):
    size = int(size)//2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / ( 2.0 * np.pi * sigma**2)
    g = np.exp( -(( x**2 + y**2)/(2.0 * sigma**2))) * normal

    return g

#gradient calculation using sobel operator
def grad_calc(img):
	vsob = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
	hsob = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

	Iy = ndimage.filters.convolve(img, hsob)
	Ix = ndimage.filters.convolve(img, vsob)

	G = np.hypot(Ix, Iy)
	G = G / G.max() * 255

	theta = np.arctan2(Iy, Ix)

	return G,theta

# Thining the edges using Non-Max-Supression
def non_max_supress(img,theta):
	height, width = img.shape
	new_img = np.zeros((height, width), dtype = np.int32)
	angle = ( theta * 180.0 ) / np.pi
	angle[ angle < 0 ] += 180

	for i in range(1,height-1):
		for j in range(1,width-1):
			q = 255
			r = 255
			if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
				q = img[i, j+1]
				r = img[i, j-1]
			elif (22.5 <= angle[i,j] < 67.5):
				q = img[i+1, j-1]
				r = img[i-1, j+1]
			elif (67.5 <= angle[i,j] < 112.5):
				q = img[i+1, j]
				r = img[i-1, j]
			elif (112.5 <= angle[i,j] < 157.5):
				q = img[i-1, j-1]
				r = img[i+1, j+1]
			if img[i, j] > q and img[i, j] > r:
				new_img[i, j] = img[i, j]
			else:
				new_img[i, j] = 0

	return new_img

# Thresholding and identifying strong,weak and non-relevant pixels
def threshold(img,ltr=0.05,htr=0.09):
	hightrshld = img.max() * htr
	lowtrshld = hightrshld * ltr
	height,width = img.shape
	new_img = np.zeros((height,width), dtype = np.int32)
	weak = np.int32(100)
	strong = np.int32(255)
	strongi, strongj = np.where(img>=hightrshld)
	non_reli, non_relj = np.where(img<lowtrshld)
	weaki, weakj = np.where((lowtrshld<=img) & (img<=hightrshld))
	new_img[strongi, strongj] = strong
	new_img[weaki, weakj] = weak

	return new_img,weak,strong

# Tracking edges using hysteresis
def hysteresis(img,weak,strong=255):
	height, width = img.shape
	for i in range(1,height-1):
		for j in range(1,width-1):
			if img[i, j]==weak:
				if (img[i-1, j-1]==strong or img[i-1, j]==strong or img[i-1, j+1]==strong\
				                        or img[i, j-1]==strong or img[i, j+1]==strong or\
				   img[i+1, j-1]==strong or img[i+1, j]==strong or img[i+1, j+1]==strong):
				   img[i, j]=strong
				else:
					img[i, j]=0

	return img


img=input('Enter image path: ')
Image = cv2.imread(img)
r, g, b = Image[:,:,0], Image[:,:,1], Image[:,:,2]
gray_img = 0.2989 * r + 0.5870 * g + 0.1140 * b
cv2.imwrite('GracyImage.PNG', gray_img)

kernel = gauss_kernel(5,1.4)
print('\nStep-1: Blurring the image using gaussian filter of 5X5.....')
blurr_img = ndimage.filters.convolve(deepcopy(gray_img), kernel)
cv2.imwrite('blurr(step1).png', blurr_img)
print('Blurred image is saved as blurr(step1).png')

print('\nStep-2: Calculating gradient using Sobel operator....')
G, theta = grad_calc(deepcopy(blurr_img))
G = np.array(G,dtype=np.int32)
cv2.imwrite('gradient_intensity(step2).png', G)
print('Gradient image is saved as gradient_intensity(step2).png')

print('\nStep-3: Thining the edges using Non-Max-Supression....')
non_max_sup = non_max_supress(G, theta)
cv2.imwrite('non_max_supress(step3).png', non_max_sup)
print('Non Max Supressed image is saved as non_max_supress(step3).png')

print('\nStep-4: Thresholding and identifying strong,weak and non-relevant pixels....')
thresh_img, weak, strong = threshold(non_max_sup, 0.09, 0.17)
cv2.imwrite('threshold(step4).png',thresh_img)
print('Threshold image is saved as threshold(step4).png')

print('\nStep-5: Tracking edges using hysteresis....')
edge_img=hysteresis(deepcopy(thresh_img),weak,strong)
cv2.imwrite('final_edge(step5).png',edge_img)
print('Final output is saved as final_edge(step5).png\n')

