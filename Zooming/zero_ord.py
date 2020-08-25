import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy
from PIL import Image
import math

# zooming using zero order hold method for rgb images
def zoom(img):
	temp = []
	# zooming row wise
	for i in range(len(img)):
		temp1 = [img[0][0]]
		for j in range(len(img[0])-1):
			a = img[i][j]
			b = img[i][j+1]
			c = [int(math.floor(((int(a[0])+int(b[0]))/2)+0.5)),int(math.floor(((int(a[1])+int(b[1]))/2)+0.5))\
			,int(math.floor(((int(a[2])+int(b[2]))/2)+0.5))]
			temp1.append(numpy.array(c,'uint8'))
			temp1.append(b)
		
		temp.append(temp1)
		temp.append(temp1)
	temp.pop()
	
	# zooming column wise
	for i in range(len(img)-1):
		for j in range(len(img[0])):
			# print(i,j)
			a = temp[2*i][j]
			b = temp[2*(i+1)][j]
			c = [int(math.floor(((int(a[0])+int(b[0]))/2)+0.5)),int(math.floor(((int(a[1])+int(b[1]))/2)+0.5))\
			,int(math.floor(((int(a[2])+int(b[2]))/2)+0.5))]
			temp[(2*i)+1][j] = c
	return temp

def zero_ord(img,n):
	for i in range(n):
		img = zoom(img)
	img = numpy.array(img)
	print('Image shape after zooming: ',img.shape)
	img = Image.fromarray(img.astype('uint8'))
	return img

	



img = input('Enter RGB img path: ')
n = int(input('Enter zooming factor(power of 2): '))
a = math.log(n,2)
b = math.floor(a)

if (a==b):
	img = mpimg.imread(img)
	if len(img[0][0]==3):
		print('Image shape before zooming: (',len(img),',',len(img[0]),',3)')
		zoom_img = zero_ord(img,int(a))
		zoom_img.save('zero_ord(zoom2).jpg')
		print('Output image is saved as zero_ord(zoom2).jpg')
	else:
		print('Please enter RGB image path.')
	
else:
	print('Wrong zooming factor.Please enter zooming factor in terms of power of two.')