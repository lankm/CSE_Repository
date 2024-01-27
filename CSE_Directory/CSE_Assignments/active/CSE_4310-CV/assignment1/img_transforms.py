# README:
# for more information about each functions execution, set log=True to see important values in stdout
#
# random_crop supports (w,h) tuples as well as integers
# color_jitter supports (min, max) tuples as well as scalars. Does not do input validation.
# extract_patch supports (num_w, num_h). supports non-square images and non-perfectly divisable images.
# resize_img supports (fac_w, fac_h).

import numpy as np
from assignment1_lib import *
import color_space_test

def main():
    filename = get_args()

    rgb_img = img_to_arr(filename)

    # rgb_img = random_crop(rgb_img, (1920,1080), log=True)
    # rgb_img = resize_img(rgb_img, (2.0,0.5))
    rgb_img = color_jitter(rgb_img, hue=360, sat=(-1,1), val=(-1,1), log=True)

    save_as_img(rgb_img, modify_filename(filename, '_modified'))


    # images = extract_patch(rgb_img, (1,5), log=True)
    # for y, row in enumerate(images):
    #     for x, rgb_img in enumerate(row):
    #         save_as_img(rgb_img, modify_filename(filename, f'_{x}_{y}'))
def get_args():
    raw_args = sys.argv[1:]
    num_args = len(raw_args)
    
    if num_args < 1:
        sys.exit('Expected ./img_transforms.py <filename>')
    filename = raw_args[0]

    return filename

def random_crop(rgb_img, size, log=False):
    if type(size) == tuple:
        size_w, size_h = size
    else:
        size_w, size_h = size, size

    h, w = img_size(rgb_img)
    avail_h, avail_w = h-size_h+1, w-size_w+1
    
    if avail_h <= 0 or avail_w <= 0:
        sys.exit(f'Crop size ({size}) is too large.')

    y = np.random.randint(avail_h)
    x = np.random.randint(avail_w)

    if log:
        print('top-left     (%d,%d)' % (x,y))
        print('bottom-right (%d,%d)' % (x+size_w,y+size_h))
    
    return rgb_img[y:y+size_h, x:x+size_w, :]

def extract_patch(rgb_img, num_patches, log=False):
    if type(num_patches) == tuple:
        num_w, num_h = num_patches
    else:
        num_w, num_h = num_patches, num_patches
    
    h, w = img_size(rgb_img)

    avg_h, avg_w = h/num_h, w/num_w
    if avg_h < 1 or avg_w < 1:
        sys.exit('num_patches is too large. Unable to split pixels.')

    images = []
    for patch_y in range(num_h):
        images.append([])
        for patch_x in range(num_w):
            y1, x1 = np.array([avg_h* patch_y,    avg_w* patch_x   ], dtype=np.uint32)
            y2, x2 = np.array([avg_h*(patch_y+1), avg_w*(patch_x+1)], dtype=np.uint32)
            if log:
                print('Patch made from (%d,%d) to (%d,%d)' % (x1,y1,x2,y2))
            image = rgb_img[y1:y2,x1:x2,:]
            images[patch_y].append(image)

    return images

def resize_img(rgb_img, factor):
    if type(factor) == tuple:
        fac_w, fac_h = factor
    else:
        fac_w, fac_h = factor, factor

    if fac_w <= 0 or fac_h <= 0:
        sys.exit('Factor must be greater than 0')

    h, w = img_size(rgb_img)
    resized_h, resized_w = int(h*fac_h), int(w*fac_w)

    resized_rgb_img = np.zeros((resized_h, resized_w, 3))
    for y in range(resized_h):
        for x in range(resized_w):
            mapped_y, mapped_x = np.rint([y/fac_h,x/fac_w]).astype(np.uint32)
            resized_rgb_img[y,x,:] = rgb_img[min(mapped_y,h-1), min(mapped_x,w-1),:]

    return resized_rgb_img

def color_jitter(rgb_img, hue, sat, val, log=False):
    if type(hue) == tuple:
        hue_min, hue_max = hue
    else:
        hue_min, hue_max = 0, hue
    hue_range = hue_max-hue_min

    if type(sat) == tuple:
        sat_min, sat_max = sat
    else:
        sat_min, sat_max = 0, sat
    sat_range = sat_max-sat_min

    if type(val) == tuple:
        val_min, val_max = val
    else:
        val_min, val_max = 0, val
    val_range = val_max-val_min

    hue_mod = np.random.rand() * hue_range + hue_min
    sat_mod = np.random.rand() * sat_range + sat_min
    val_mod = np.random.rand() * val_range + val_min

    if log:
        print('hue modification:        %.3f' % hue_mod)
        print('saturation modification: %.3f' % sat_mod)
        print('value modification:      %.3f' % val_mod)

    hsv_img = color_space_test.rgb_to_hsv(rgb_img)
    hsv_img = color_space_test.mod_img(hsv_img, hue_mod, sat_mod, val_mod)
    rgb_img = color_space_test.hsv_to_rgb(hsv_img)

    return rgb_img

if __name__ == '__main__':
    main()
