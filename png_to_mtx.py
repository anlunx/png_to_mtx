import os
import imageio.v3 as iio
import numpy as np

directory = '/Users/anlunx/projects/png_to_mtx/png'

count = 0
for root, dirs, files in os.walk(directory):
  for filename in files:
    if filename.endswith('.png'):
      count += 1
      print(root)
      print(dirs)
      print(filename)

filepath = '/Users/anlunx/projects/png_to_mtx/png/airplane/1.png'
im = iio.imread(filepath)
assert(len(im.shape) == 2)
for (i, j), value in np.ndenumerate(im):
  if (value != 255):
    print(i, j, value)