# README
# This part of the assignment is about implementing the match_descriptors() function. Other parts such as extract_features() and plot() have code from the professor's github.
# match_descriptors() has the same name as the skimage function and produces the same number of points on the images I tested.

import numpy as np
from skimage import io, color, feature
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch

def main():
    filename1, filename2 = get_args()

    img1 = load_img(filename1)
    img2 = load_img(filename2)

    keypoints1, descriptors1 = extract_features(img1)
    keypoints2, descriptors2 = extract_features(img2)

    matches = match_descriptors(descriptors1, descriptors2)[:] # same name as skimage, but this is my own implementation. Change the bounds if you want to see subsets of the matches
    # matches = feature.match_descriptors(descriptors1, descriptors2, cross_check=True) # library equivelent

    plot(img1, img2, keypoints1, keypoints2, matches)
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
def extract_features(img):
    detector = feature.SIFT()
    detector.detect_and_extract(img)
    keypoints = detector.keypoints
    descriptors = detector.descriptors.astype(np.float32)
    return keypoints, descriptors

def match_descriptors(descriptors1: np.ndarray, descriptors2: np.ndarray) -> np.ndarray:
    # This algorithm is my best guess at the implementation of skimage.feature.match_descriptors()
    matches = []

    for i, descriptor1 in enumerate(descriptors1):
        # closest descriptor2 to descriptor1
        diffs = descriptors2 - descriptor1
        dists = np.sum(diffs * diffs, axis=1)   # ~L2 dist. no square root
        closest = np.argmin(dists)

        # closest descriptor1 to descriptor2
        diffs = descriptors1 - descriptors2[closest]
        dists = np.sum(diffs * diffs, axis=1)
        cross_closest = np.argmin(dists)

        # if both are closest to eachother
        if i == cross_closest:
            matches.append((i,closest))


    return np.array(matches)

def plot(img1, img2, keypoints1, keypoints2, matches):
    # code taken from professor's github
    keypoints1 = keypoints1[matches[:, 0]]
    keypoints2 = keypoints2[matches[:, 1]]

    fig = plt.figure(figsize=(8, 4))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.imshow(img1, cmap='gray')
    ax2.imshow(img2, cmap='gray')

    for i in range(keypoints2.shape[0]):
        coordB = [keypoints1[i, 1], keypoints1[i, 0]]
        coordA = [keypoints2[i, 1], keypoints2[i, 0]]
        con = ConnectionPatch(xyA=coordA, xyB=coordB, coordsA="data", coordsB="data",
                          axesA=ax2, axesB=ax1, color="red")
        ax2.add_artist(con)
        ax1.plot(keypoints1[i, 1], keypoints1[i, 0], 'ro')
        ax2.plot(keypoints2[i, 1], keypoints2[i, 0], 'ro')

    plt.show()


if __name__ == '__main__':
    main()
