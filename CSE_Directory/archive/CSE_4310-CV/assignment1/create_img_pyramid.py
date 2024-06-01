# README:
# Works on non-square images. Also works unbelievably fast (tested on 32k images).

import numpy as np
import sys
from assignment1_lib import *

def main():
    filename, depth = get_args()

    rgb_img = img_to_arr(filename)

    images = create_img_pyrmid(rgb_img, depth)

    for i, rgb_img in enumerate(images[1:]):
        save_as_img(rgb_img, modify_filename(filename, f'_{2**(i+1)}x'))
def get_args():
    raw_args = sys.argv[1:]
    num_args = len(raw_args)
    
    if num_args < 2:
        sys.exit('Expected ./create_img_pyramid.py <filename> <depth>')
    filename = raw_args[0]
    depth = int(raw_args[1])

    if depth <= 1:
        sys.exit('Expected <depth> to be larger than 1')

    return filename, depth

def create_img_pyrmid(rgb_img, depth):
    if 2**(depth-1) > min(img_size(rgb_img)):
        sys.exit('depth/height is too large. Unable to split pixels.')
    
    return split_img(rgb_img, depth)
def split_img(rgb_img, depth):
    if depth <= 1:
        return [rgb_img]
    
    h, w = img_size(rgb_img) // 2
    split_rgb_img = np.reshape(rgb_img[:h*2,:w*2,:], (h,2,w,2,3))
    split_rgb_img = np.mean(split_rgb_img, axis=(1,3))

    return [rgb_img, *split_img(split_rgb_img, depth-1)]

if __name__ == '__main__':
    main()
