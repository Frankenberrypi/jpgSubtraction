# for Python 3.6
# known to work on .jpg and .tif files
# probably works on .png and .gif files
# no workie on .pdf files

from scipy import misc
import numpy as np

# Get the files
print("Enter first file name")
beforeFile = input()
print("Enter second file name")
afterFile = input()


# Read files in
#before = misc.imread('Seattle TAC 87.tif',flatten=1)
#after = misc.imread('Seattle TAC 88.tif',flatten=1)
before = misc.imread(beforeFile,flatten=1)
after = misc.imread(afterFile,flatten=1)

subtracted = np.subtract(before,after)

misc.imsave('subtracted.jpg',subtracted)
