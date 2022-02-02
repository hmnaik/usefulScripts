import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import scipy
from scipy import ndimage

fname = "cat.jpg"

image = np.array(ndimage.imread(fname,flatten = False))
plt.imshow(image)
my_image = scipy.misc.imresize(image, size = (64,64)).reshape((1,64*64*3)).T

