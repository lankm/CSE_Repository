# README
# This part of the assignment is about implementing the match_descriptors() function. Other parts such as extract_features() and plot() have code from the professor's github.
# match_descriptors() has the same name as the skimage function and does almost the same thing. There is a small difference in the number of returned matches probably due to ties.
# otherwise works fairly well. When tested on the yosemite images, moutain peaks generally match to the same moutain peak in the other image. there is still the noise as expected.

# https://en.wikipedia.org/wiki/Random_sample_consensus

import numpy as np
from skimage import io, color, feature, measure
from skimage.transform import ProjectiveTransform, SimilarityTransform, warp
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch

def compute_affine_transform(keypoint_pairs): # return 3x3 matrix
    pass

def compute_projective_transform(keypoint_pairs): # return 3x3 matrix
    pass

def ransac():
    pass


def main():
    filename1, filename2 = get_args()

    img1, img_gray1 = load_img(filename1)
    img2, img_gray2 = load_img(filename2)

    keypoints1, descriptors1 = extract_features(img_gray1)
    keypoints2, descriptors2 = extract_features(img_gray2)

    matches = feature.match_descriptors(descriptors1, descriptors2, cross_check=True)

    plot_all(img_gray1, img_gray2, keypoints1, keypoints2, matches)

    # TODO
    dst = keypoints1[matches[:, 0]]
    src = keypoints2[matches[:, 1]]
    sk_M, sk_best = measure.ransac((src[:, ::-1], dst[:, ::-1]), ProjectiveTransform, min_samples=4, residual_threshold=1, max_trials=300)
    print(sk_M)

    plot_best(img1, img2, keypoints1, keypoints2, sk_best, matches)

    warp_img(img_gray1, img1, img2, sk_M)


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
    img_gray = color.rgb2gray(img)
    return img, img_gray
def extract_features(img):
    detector = feature.SIFT()
    detector.detect_and_extract(img)
    keypoints = detector.keypoints
    descriptors = detector.descriptors
    return keypoints, descriptors

def plot_all(img_gray1, img_gray2, keypoints1, keypoints2, matches):
    # code taken from professor's github
    keypoints1 = keypoints1[matches[:, 0]]
    keypoints2 = keypoints2[matches[:, 1]]

    fig = plt.figure(figsize=(8, 4))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.imshow(img_gray1, cmap='gray')
    ax2.imshow(img_gray2, cmap='gray')

    for i in range(keypoints2.shape[0]):
        coordB = [keypoints1[i, 1], keypoints1[i, 0]]
        coordA = [keypoints2[i, 1], keypoints2[i, 0]]
        con = ConnectionPatch(xyA=coordA, xyB=coordB, coordsA="data", coordsB="data",
                          axesA=ax2, axesB=ax1, color="red")
        ax2.add_artist(con)
        ax1.plot(keypoints1[i, 1], keypoints1[i, 0], 'ro')
        ax2.plot(keypoints2[i, 1], keypoints2[i, 0], 'ro')

    plt.show()
def plot_best(img1, img2, keypoints1, keypoints2, sk_best, matches):
    src_best = keypoints2[matches[sk_best, 1]][:, ::-1]
    dst_best = keypoints1[matches[sk_best, 0]][:, ::-1]

    fig = plt.figure(figsize=(8, 4))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.imshow(img1)
    ax2.imshow(img2)

    for i in range(src_best.shape[0]):
        coordB = [dst_best[i, 0], dst_best[i, 1]]
        coordA = [src_best[i, 0], src_best[i, 1]]
        con = ConnectionPatch(xyA=coordA, xyB=coordB, coordsA="data", coordsB="data", axesA=ax2, axesB=ax1, color="red")
        ax2.add_artist(con)
        ax1.plot(dst_best[i, 0], dst_best[i, 1], 'ro')
        ax2.plot(src_best[i, 0], src_best[i, 1], 'ro')

    plt.show()

def warp_img(img_gray1, img1, img2, sk_M):
    # Transform the corners of img1 by the inverse of the best fit model
    rows, cols = img_gray1.shape
    corners = np.array([
        [0, 0],
        [cols, 0],
        [0, rows],
        [cols, rows]
    ])

    corners_proj = sk_M(corners)
    all_corners = np.vstack((corners_proj[:, :2], corners[:, :2]))

    corner_min = np.min(all_corners, axis=0)
    corner_max = np.max(all_corners, axis=0)
    output_shape = (corner_max - corner_min)
    output_shape = np.ceil(output_shape[::-1]).astype(int)
    print(output_shape)

    offset = SimilarityTransform(translation=-corner_min)
    dst_warped = warp(img1, offset.inverse, output_shape=output_shape)

    tf_img = warp(img2, (sk_M + offset).inverse, output_shape=output_shape)

    # Combine the images
    foreground_pixels = tf_img[tf_img > 0]
    dst_warped[tf_img > 0] = tf_img[tf_img > 0]

    # Plot the result
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.imshow(dst_warped)

    plt.show()

if __name__ == '__main__':
    main()

