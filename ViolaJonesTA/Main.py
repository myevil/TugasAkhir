import glob
from PIL import Image
from scipy import misc
import numpy as np
import matplotlib.pyplot
import matplotlib.image

def is_Grayscale(width, height, image):
    a = 0
    for i in range (width):
        for j in range (height):
            r, g, b = image.convert('RGB').getpixel((i,j))
            if (r != g != b):
                return False
    return True


def grayscale(image):
    return np

image_list = []
for filename in glob.glob('GetImage/*.jpg'):
    im=Image.open(filename)
    image_list.append(im)

width, height = image_list[0].size

#print(image_list[0])

print(is_Grayscale(width,height,image_list[0]))

if(is_Grayscale(width,height,image_list[0]) != True):
    image_list[0] = rgb2gray(image_list[0])

image_list[0].show()

