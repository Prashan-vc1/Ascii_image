from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

input_image = imread("d:\Download\ghhh.jpg")


r,g,b = input_image[:,:,0] , input_image[:,:,1] , input_image[:,:,2]

gamma = 1.04

r_const , g_const , b_const = 0.2126 , 0.7152 , 0.0722

grayscale_image = r_const * r ** gamma + g_const * g**gamma + b_const * b** gamma


fig = plt.figure(1)
img2 =fig.add_subplot(122)


img2.imshow(grayscale_image , cmap= plt.cm.get_cmap('gray'))

fig.show()
plt.show()