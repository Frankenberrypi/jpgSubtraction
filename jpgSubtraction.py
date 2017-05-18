# for Python 3.6
# known to work on .jpg and .tif files
# probably works on .png and .gif files
# no workie on .pdf files

from scipy import misc
import numpy as np
import sys

if len(sys.argv) > 1:
    # Get the files from the system command line arguments
    beforeFile = sys.argv[1]
    afterFile = sys.argv[2]
else:
    # Get the files with user input
    beforeFile = input("Enter first file name: ")
    afterFile = input("Enter second file name: ")


# Read files in
#before = misc.imread('Seattle TAC 87.tif',flatten=1)
#after = misc.imread('Seattle TAC 88.tif',flatten=1)
before = misc.imread(beforeFile,flatten=1)
after = misc.imread(afterFile,flatten=1)

subtracted = np.subtract(before,after)

misc.imsave('subtracted.jpg',subtracted)
