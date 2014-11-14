from scipy import misc
import numpy as np

before = misc.imread('before.JPG',flatten=0)
after = misc.imread('after.JPG',flatten=0)

subtracted = np.subtract(before,after)

misc.imsave('subtracted.jpg',subtracted)