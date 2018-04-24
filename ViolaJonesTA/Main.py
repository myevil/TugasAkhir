import glob
from PIL import Image
import cv2


def is_Grayscale(width, height, image):
    for i in range (width):
        for j in range (height):
            r, g, b = image.convert('RGB').getpixel((i,j))
            if (r == g == b):
                return True
    return False
            
def grayscale(width, height, image):
    img = Image.new(im.mode, im.size)
    pixelsNew = img.load()
    for i in range (width):
        for j in range (height):
            r, g, b = image.convert('RGB').getpixel((i,j))
            total = (r + g + b) / 3
            pixelsNew[i,j] = (int(total),int(total),int(total),255)
    return image

image_list = []
for filename in glob.glob('GetImage/*.jpg'):
    im=Image.open(filename)
    image_list.append(im)

width, height = image_list[0].size

print(is_Grayscale(width,height,image_list[0]))

if(is_Grayscale(width,height,image_list[0]) == True):
    image_list[0] = grayscale(width, height, image_list[0])

image_list[0].show()

