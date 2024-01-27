# https://github.com/ajdillhoff/CSE4310/tree/main/assignments/assignment1
# np.uint8 doesn't warn about underflows. I got tired of dealing with types in a language not designed around them, so everything is float64 until saved as uint8.
# the program just uses more memory than I would like.

# README:
# Everything works as expected. 
# There were no clear details about how to apply the modifications so I just did a clampted multiplication.
# Because of this I also increased the accepted bounds: H -> any, S -> [-1,1], V -> [-1,1]. -1 = -100%, 0 = +0%, 1 = +100%,
# More complex modifcation algorithms could be used but it doesn't make too much of a difference.

import numpy as np
from assignment1_lib import *

def main():
    filename, hue_mod, sat_mod, val_mod = get_args()

    rgb_img = img_to_arr(filename)

    hsv_img = rgb_to_hsv(rgb_img)
    hsv_img = mod_img(hsv_img, hue_mod, sat_mod, val_mod)
    rgb_img = hsv_to_rgb(hsv_img)

    save_as_img(rgb_img, modify_filename(filename, '_modified'))
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
    if sat_mod < -1 or sat_mod > 1:
        sys.exit('Expected <saturation modification> in range [-1,1]')

    val_mod = 0.0
    if num_args >= 4:
        val_mod = float(raw_args[3])
    if val_mod < -1 or val_mod > 1:
        sys.exit('Expected <value modification> in range [-1,1]')

    return filename, hue_mod, sat_mod, val_mod

def rgb_to_hsv(rgb_img):
    V = np.max(rgb_img, axis=2)
    C = V - np.min(rgb_img, axis=2)
    S = np.divide(C, V, out=np.zeros_like(C, dtype=float), where=V!=0)
    H = get_H(rgb_img, V, C)

    HSV = np.dstack([H, S, V])
    return HSV
def get_H(rgb_img,V,C):
    R = rgb_img[:,:,0]
    G = rgb_img[:,:,1]
    B = rgb_img[:,:,2]

    zeros = C==0
    C = np.where(zeros, 1, C) # makes division by zero safe

    H = np.zeros_like(V)
    H = np.where(V==R, ((G-B)/C % 6), H)
    H = np.where(V==G, ((B-R)/C + 2), H)
    H = np.where(V==B, ((R-G)/C + 4), H)
    H = np.where(zeros, 0, H)

    return 60 * H

def mod_img(hsv_img, hue_mod, sat_mod, val_mod):
    H = hsv_img[:,:,0]
    S = hsv_img[:,:,1]
    V = hsv_img[:,:,2]

    H = (H + hue_mod) % 360
    S = np.clip(S * (1+sat_mod), 0, 1)
    V = np.clip(V * (1+val_mod), 0, 255)

    return np.dstack([H,S,V])

def hsv_to_rgb(hsv):
    H = hsv[:,:,0]/60
    S = hsv[:,:,1]
    V = hsv[:,:,2]
    
    C = V*S
    X = C*(1-abs(H % 2 - 1))

    R, G, B = get_RGB_p(C,X,H)
    m = V-C
    R, G, B = R+m, G+m, B+m

    return np.dstack([R,G,B])
def get_RGB_p(C,X,H):
    # I don't like how I was forced to do this. *unclean code*
    rgb = np.zeros((*H.shape, 3))
    rgb = np.where(np.repeat((H<6)[:,:,np.newaxis], 3, axis=2), np.dstack([C,np.zeros_like(C),X]), rgb)
    rgb = np.where(np.repeat((H<5)[:,:,np.newaxis], 3, axis=2), np.dstack([X,np.zeros_like(C),C]), rgb)
    rgb = np.where(np.repeat((H<4)[:,:,np.newaxis], 3, axis=2), np.dstack([np.zeros_like(C),X,C]), rgb)
    rgb = np.where(np.repeat((H<3)[:,:,np.newaxis], 3, axis=2), np.dstack([np.zeros_like(C),C,X]), rgb)
    rgb = np.where(np.repeat((H<2)[:,:,np.newaxis], 3, axis=2), np.dstack([X,C,np.zeros_like(C)]), rgb)
    rgb = np.where(np.repeat((H<1)[:,:,np.newaxis], 3, axis=2), np.dstack([C,X,np.zeros_like(C)]), rgb)

    R = rgb[:,:,0]
    G = rgb[:,:,1]
    B = rgb[:,:,2]
    return R, G, B

if __name__ == '__main__':
    main()
