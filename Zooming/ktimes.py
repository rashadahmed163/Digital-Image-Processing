import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy
from PIL import Image
import math

# zooming using k-times method for rgb images
def k_zoom(img,k):
	temp = []
	# row zooming
	for i in range(len(img)):
		temp1 = [img[0][0]]
		for j in range(len(img[0])-1):
			a = img[i][j]
			p = []
			for m in range(3):
				p.append(int(a[m]))
			b = img[i][j+1]
			d0 = (int(b[0])-int(a[0]))/k
			d1 = (int(b[1])-int(a[1]))/k
			d2 = (int(b[2])-int(a[2]))/k
			for m in range(k-1):
				c = []
				p[0] = d0 + p[0]
				p[1] = d1 + p[1]
				p[2] = d2 + p[2]
				for n in range(3):
					c.append(p[n])
				temp1.append(numpy.array(c,'uint8'))
			temp1.append(b)
		temp.append(temp1)
		for m in range(k-1):
			temp.append(temp1)

	for m in range(k-1):
		temp.pop()
	# column zooming
	for i in range(len(img)-1):
		for j in range(len(img[0])):
			# print(i,j)
			a = temp[k*i][j]
			b = temp[k*(i+1)][j]
			p = []
			for m in range(3):
				p.append(int(a[m]))
			d0 = (int(b[0])-int(a[0]))/k
			d1 = (int(b[1])-int(a[1]))/k
			d2 = (int(b[2])-int(a[2]))/k
			for m in range(k-1):
				c = []
				p[0] = d0 + p[0]
				p[1] = d1 + p[1]
				p[2] = d2 + p[2]
				for n in range(3):
					c.append(p[n])
				temp[(k*i)+1+m][j] = c
	zoom_img = temp
	zoom_img = numpy.array(zoom_img)
	print('Image shape after zooming: ',zoom_img.shape)
	zoom_img = Image.fromarray(zoom_img.astype('uint8'))
	return zoom_img

img = input('Enter RGB img path: ')
k = int(input('Enter zooming factor(k): '))

img = mpimg.imread(img)
if len(img[0][0]==3):
	print('Image shape before zooming: (',len(img),',',len(img[0]),',3)')
	zoom_img = k_zoom(img,3)
	zoom_img.save('k_zoom(zoom3).jpg')
	print('Output image is saved as k_zoom(zoom3).jpg')
else:
	print('Please enter RGB image path.')