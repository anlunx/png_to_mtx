import os
import imageio.v3 as iio
import numpy as np
import scipy

directory = '/Users/anlunx/projects/png_to_mtx/png'

def png_to_mtx(filepath, outputpath):
  im = iio.imread(filepath)
  assert(len(im.shape) == 2)
  rows = []
  cols = []
  data = []
  for (i, j), value in np.ndenumerate(im):
    if (value != 255):
      rows.append(i)
      cols.append(j)
      color = 255 - value
      data.append(color)
  coo_matrix = scipy.sparse.coo_matrix((data, (rows, cols)), shape=im.shape)
  scipy.io.mmwrite(outputpath, coo_matrix)

png_dir = '/Users/anlunx/projects/png_to_mtx/png'
for dir in os.listdir(png_dir):
  if (dir == '.DS_Store'):
    continue
  if (dir == 'filelist.txt'):
    continue
  output_dir = f'/Users/anlunx/projects/png_to_mtx/mtx/{dir}'
  print(f'Processing {dir}')
  for file in os.listdir(f'{png_dir}/{dir}'):
    assert(file.endswith('.png'))
    filepath = f'{png_dir}/{dir}/{file}'
    outputpath = f'{output_dir}/{file[:-4]}.mtx'
    os.makedirs(output_dir, exist_ok=True)
    png_to_mtx(filepath, outputpath)