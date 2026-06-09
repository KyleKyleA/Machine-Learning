import numpy as np
from matplotlib.image import imread

# Importing image from matplot lib with the imread 
# Declare the image you want to turn into an array just like this panda
panda = imread("Numpy's/images/numpy-panda.jpeg")

# Can print the type of image goes by class just like an html tag
print(type(panda))

# Printing the panda array 
# goes by matrices 
print(panda.shape)
print(panda)

# and goes on and so forth 