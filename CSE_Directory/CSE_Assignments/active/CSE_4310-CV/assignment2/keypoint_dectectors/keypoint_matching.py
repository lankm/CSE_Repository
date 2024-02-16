import numpy as np
from skimage import io, color, feature
import sys
import matplotlib.pyplot as plt




def main():
    filename_1, filename_2 = get_args()

    # Load the images
    img1 = load_img(filename_1)
    img2 = load_img(filename_2)

    detector1 = feature.SIFT()
    detector2 = feature.SIFT()
    detector1.detect_and_extract(img1)
    detector2.detect_and_extract(img2)
    keypoints1 = detector1.keypoints
    descriptors1 = detector1.descriptors
    keypoints2 = detector2.keypoints
    descriptors2 = detector2.descriptors

    matches = feature.match_descriptors(descriptors1, descriptors2, cross_check=True)

    plot(img1, img2, kf1, kf2, matches)
def get_args():
    raw_args = sys.argv[1:]
    num_args = len(raw_args)
    
    if num_args < 2:
        sys.exit('Expected ./keypoint_matching.py <filename_1> <filename_2>')
    filename_1 = raw_args[0]
    filename_2 = raw_args[1]

    return filename_1, filename_2
def load_img(filename):
    img = io.imread(filename)
    if img.shape[2] == 4:
        img = color.rgba2rgb(img)
    img = color.rgb2gray(img)
    return img

def match_descriptors(kf1: list, kf2: list) -> list:
    # kf1 & kf2: keypoint features. list of (x,y) tuples.
    # return list of indicies, matching between them
    pass

def plot(img1, img2, kf1, kf2, matches):
    fig = plt.figure(figsize=(8, 4))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.imshow(img1, cmap='gray')
    ax2.imshow(img2, cmap='gray')

    # for loop of matches

    plt.show()


if __name__ == '__main__':
    main()
