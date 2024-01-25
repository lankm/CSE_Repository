# https://github.com/ajdillhoff/CSE4310/tree/main/assignments/assignment1

import numpy as np
import sys
from PIL import Image

# RGB <-> HSV
# image transformations

def main():
    filename, hue_mod, sat_mod, val_mod = get_args()

    # read and format the image
    img_rgb = png_to_arr(filename)

    # modify
    img_hsv = rgb_to_hsv(img_rgb)
    print(img_hsv)

    # img_hsv = mod_img(img_hsv, hue_mod, sat_mod, val_mod)

    # img_rgb = np.apply_along_axis(lambda x: colorsys.hsv_to_rgb(*x), axis=2, arr=img_hsv)
    # img_rgb = np.apply_along_axis(hsv_to_rgb, axis=2, arr=img_hsv)

    # save as new pngs
    # save_as_png(img_rgb, 'img/modified_img.png')

def get_args():
    raw_args = sys.argv[1:]
    num_args = len(raw_args)
    
    if num_args < 1:
        sys.exit('Expected ./color_space_test.py <filename> <hue modification>? <saturation modification>? <value modification>?')
    filename = raw_args[0]

    hue_mod = 0.0
    if num_args >= 2:
        hue_mod = float(raw_args[1])
    hue_mod = hue_mod % 360.0

    sat_mod = 0.0
    if num_args >= 3:
        sat_mod = float(raw_args[2])
    if sat_mod < 0 or sat_mod > 1:
        sys.exit('Expected <saturation modification> in range [0,1]')

    val_mod = 0.0
    if num_args >= 4:
        val_mod = float(raw_args[3])
    if val_mod < 0 or val_mod > 1:
        sys.exit('Expected <value modification> in range [0,1]')

    return filename, hue_mod, sat_mod, val_mod

def png_to_arr(file):
    img = Image.open(file)
    img_rgb = np.array(img)
    img.close()

    # remove alpha channel
    if img_rgb.shape[2] == 4:
        img_rgb = img_rgb[:, :, :3]

    return img_rgb
def save_as_png(img_rgb, filename):
    image = Image.fromarray(img_rgb.astype('uint8'))

    image.save(filename)
    print(f'Image saved to {filename}')

def rgb_to_hsv(img_rgb):
    V = np.max(img_rgb, axis=2)
    C = V - np.min(img_rgb, axis=2)
    S = np.divide(C, V, out=np.zeros_like(C).astype(float), where=V!=0)
    H = get_H(img_rgb, V, C)

    HSV = np.dstack((H, S, V))
    return HSV
def get_H(img_rgb,V,C):
    R = img_rgb[:,:,0]
    G = img_rgb[:,:,1]
    B = img_rgb[:,:,2]

    H = np.zeros_like(V)
    # H[np.logical_and(C!=0, V==R)] = 60 * ((G-B)/C % 6)
    # H[np.logical_and(C!=0, V==G)] = 60 * ((B-R)/C + 2)
    # H[np.logical_and(C!=0, V==B)] = 60 * ((R-G)/C + 4)

    return H

def hsv_to_rgb(hsv):
    H = hsv[0]/60
    S = hsv[1]
    V = hsv[2]
    
    C = V*S
    X = C*(1-abs(H % 2 - 1))

    r,g,b = get_RGB_p(C,X,H)
    m=V-C
    r+=m
    g+=m
    b+=m

    return (r,g,b)
def get_RGB_p(C,X,H):
    if 0<=H and H<1:
        return (C,X,0)
    elif 1<=H and H<2:
        return (X,C,0)
    elif 2<=H and H<3:
        return (0,C,X)
    elif 3<=H and H<4:
        return (0,X,C)
    elif 4<=H and H<5:
        return (X,0,C)
    else:
        return (C,0,X)

def mod_img(img_hsv, hue_mod, sat_mod, val_mod):
    # TODO
    return img_hsv

if __name__ == '__main__':
    main()