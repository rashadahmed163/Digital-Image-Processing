import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy
from PIL import Image

img = mpimg.imread('rgb.jpg')
avg_img = []
weight_img = []

for i in range(len(img)):
	row1 = []
	row2 = []
	for j in range(len(img[0])):
		temp = img[i][j]
		# Average method
		row1.append( (int(temp[0]) + int(temp[1]) + int(temp[2]))/3 )

		# weighted method
		row2.append( (int(temp[0])*0.3) + (int(temp[1])*0.59) + (int(temp[2])*0.11) )
	avg_img.append(row1)
	weight_img.append(row2)

avg_img = numpy.array(avg_img)
avg_img = Image.fromarray(avg_img.astype('uint8'))
avg_img.save('average.png')
weight_img = numpy.array(weight_img)
weight_img = Image.fromarray(weight_img.astype('uint8'))
weight_img.save('weighted.png')
print('Gray image using Average method is stored as average.png')
print('Gray image using Weighted average method is stored as weighted.png')