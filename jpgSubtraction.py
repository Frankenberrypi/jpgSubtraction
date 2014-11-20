#
from scipy import misc
import numpy as np

before = misc.imread('before.JPG',flatten=1)
after = misc.imread('after.JPG',flatten=1)

subtracted = np.subtract(before,after)

misc.imsave('subtracted.jpg',subtracted)
