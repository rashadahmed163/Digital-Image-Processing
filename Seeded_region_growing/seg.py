from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from copy import deepcopy
from scipy import ndimage
import random

def seg(img,k):
	height, width = img.shape
	cluster = {}
	rand_points = [ random.randint(0,255) for i in range(k) ]
	initial_diff=(256/(1.5*k+1))
	for i in range(1,k):
		while(abs(rand_points[i] - rand_points[i-1]) < initial_diff):
			rand_points[i] = random.randint(0,255)

	print(rand_points)
	for i in range(k):
		cluster[i] = []





# img=input('Enter image path: ')
Image = cv2.imread('image.jpg')
r, g, b = Image[:,:,0], Image[:,:,1], Image[:,:,2]
gray_img = 0.2989 * r + 0.5870 * g + 0.1140 * b
cv2.imwrite('GracyImage.PNG', gray_img)
seg(deepcopy(gray_img),16)