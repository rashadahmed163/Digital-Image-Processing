from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from copy import deepcopy

#function to apply filter using convolution concept
def filter(img,mask):
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
			for k in range(3):
				for l in range(3):
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
Image = cv2.imread(img)
gray_img = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('GracyImage.PNG', gray_img)

#Prewitt Operator
print("Applying Prewitt Operator......")
vprewitt = [[-1,0,1],[-1,0,1],[-1,0,1]] #vertical prewitt operator
hprewitt = [[-1,-1,-1],[0,0,0],[1,1,1]] #horizontal prewitt operator
# gray_img=[[2,4,6],[8,10,12],[14,16,18]]
vprew_img = filter(deepcopy(gray_img),vprewitt)
cv2.imwrite('vert_prewitt.png',vprew_img)
print('Vertical edge detected and saved as vert_prewitt.png.')
hprew_img = filter(deepcopy(gray_img),hprewitt)
cv2.imwrite('horz_prewitt.png',hprew_img)
print('Horizontal edge detected and saved as horz_prewitt.png.')
prew_img = np.hypot(vprew_img,hprew_img)
prew_img = np.array(prew_img / prew_img.max() * 255,dtype=np.int8)
cv2.imwrite('prewitt.png',prew_img)
print('Vertical+Horizontal edge detected and saved as prewitt.png.')
print()

#Sobel Operator
print('Applying Sobel Operator......')
vsobel = [[-1,0,1],[-2,0,2],[-1,0,1]] #vertical sobel operator
hsobel = [[-1,-2,-1],[0,0,0],[1,2,1]] #horizontal sobel operator
vsob_img = filter(deepcopy(gray_img),vsobel)
cv2.imwrite('vert_sobel.png',vsob_img)
print('Vertical edge detected and saved as vert_sobel.png.')
hsob_img = filter(deepcopy(gray_img),hsobel)
cv2.imwrite('horz_sobel.png',hsob_img)
print('Horizontal edge detected and saved as horz_sobel.png.')
sob_img = np.hypot(vsob_img,hsob_img)
sob_img = np.array(sob_img / sob_img.max() * 255, dtype=np.int8)
cv2.imwrite('sobel.png',sob_img)
print('Vertical+Horizontal edge detected and saved as sobel.png.')
print()

#Laplacian Operator
print('Applying Laplacian Operator......')
poslap = [[0,1,0],[1,-4,1],[0,1,0]]   #positive laplacian operator
neglap = [[0,-1,0],[-1,4,-1],[0,-1,0]] #negative laplacian operator
#postive laplacian - outward edges
#negative laplacian - inward edges
out_img = filter(deepcopy(gray_img),poslap)
cv2.imwrite('outedge(postive_lap).png',out_img)
print('Outward edge detected and saved as outedge(positive_lap).png.')
in_img = filter(deepcopy(gray_img),neglap)
cv2.imwrite('inedge(negative_lap).png',in_img)
print('Inward edge detected and saved as inedge(negative_lap).png.')
lap_img = np.hypot(out_img,in_img)
lap_img = np.array( lap_img / lap_img.max() * 255, dtype=np.int8)
cv2.imwrite('laplacian.png',lap_img)
print('Inward+Outward edge detected and saved as laplacian.png.')


