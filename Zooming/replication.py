import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy
from PIL import Image

# Zooming with pixel replication for rgb images
def pixel_repl(img,n):
	temp = []
	for i in range(len(img)):
		temp1 = []
		for j in range(len(img[0])):
		# row pixel replication
			for k in range(n):
				temp1.append(img[i][j])
		# column wise pixel replication
		for k in range(n):
			temp.append(temp1)
	zoom_img = numpy.array(temp)
	print('Image shape after zooming: ',zoom_img.shape)
	zoom_img = Image.fromarray(zoom_img.astype('uint8'))
	return zoom_img


img = input('Enter img path: ')
n = int(input('Enter zooming factor: '))
img = mpimg.imread(img)
if(len(img[0][0]) == 3):
	print('Image shape before zooming: (',len(img),',',len(img[0]),',3)')
	zoom_img = pixel_repl(img, n)
	zoom_img.save('pixel_repl(zoom1).jpg')
	print('Output image is saved as pixel_repl(zoom1).jpg')
else:
	print('Please enter RGB image path.')