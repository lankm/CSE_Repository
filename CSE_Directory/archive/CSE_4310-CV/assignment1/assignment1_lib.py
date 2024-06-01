import numpy as np
import sys
import os
from PIL import Image

def modify_filename(filename, append):
    base, extension = os.path.splitext(filename)
    return f'{base}{append}{extension}'

def img_to_arr(file):
    img = Image.open(file)
    rgb_img = np.array(img)
    img.close()

    # remove alpha channel
    if rgb_img.shape[2] == 4:
        rgb_img = rgb_img[:, :, :3]

    return rgb_img.astype(np.float64)
def save_as_img(rgb_img, filename):
    image = Image.fromarray(rgb_img.astype(np.uint8))

    image.save(filename)
    print(f'Image saved to {filename}')

def img_size(img):
    return np.array(img[:,:,0].shape, dtype=np.uint32)
