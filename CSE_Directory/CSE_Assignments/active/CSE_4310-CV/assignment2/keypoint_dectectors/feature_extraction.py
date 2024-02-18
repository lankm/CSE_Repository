# README
#

import numpy as np
from skimage import io, color, feature, data, exposure
from sklearn import cluster
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfTransformer

def main():
    # Load the pre-split data
    data = np.load("cifar10.npz", allow_pickle=True) # dictionary of arrays

    train_images = to_img(data['X_train'].astype(np.uint8)) # 16000 32x32 images
    test_images = to_img(data['X_test'].astype(np.uint8)) # 4000 32x32 images
    train_labels = data['y_train'].astype(np.uint32) # 16000 numbers (classes)
    test_labels = data['y_test'].astype(np.uint32) # 4000 numbers (classes)

    # Visualize the input data
    # show(X_train)

    # hyperparams
    extract_type='hog'
    vocab_size=50

    # Extract features from the each dataset
    train_descriptors, train_labels = extract(train_images, train_labels, 'Processing training data', extract_type=extract_type)
    test_descriptors, test_labels = extract(test_images, test_labels, 'Processing testing data', extract_type=extract_type)

    # Build a shared vocab set from the training set
    kmeans = build_vocab(train_descriptors, vocab_size)

    # Make histograms with the above vocab set
    train_histograms = get_histogram(kmeans, train_descriptors, vocab_size)
    test_histograms = get_histogram(kmeans, test_descriptors, vocab_size)

    # Save the extracted features to a file
    save_to_file(train_histograms, test_histograms, train_labels, test_labels, f'{extract_type}.npz')

def to_img(dataset):
    cifar_rgb = dataset.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)
    cifar_gray = color.rgb2gray(cifar_rgb)
    return cifar_gray

def extract(images, labels, desc='Processing images', extract_type='sift'):
    sift = feature.SIFT()
    out_descriptors = []
    out_labels = []
    total_features = 0

    for idx in tqdm(range(images.shape[0]), desc=desc):
        try:
            if extract_type=='hog':
                hog_features = feature.hog(images[idx])
                out_descriptors.append([hog_features])
                total_features += 1
            else:
                sift.detect_and_extract(images[idx])
                out_descriptors.append(sift.descriptors)
                total_features += sift.descriptors.shape[0]
            out_labels.append(labels[idx]) # Only stores the label if the features are successfully extracted
        except:
            pass

    print(f'Extracted {total_features} features')
    
    return out_descriptors, out_labels
def build_vocab(all_descriptors, vocab_size=50):
    # Convert the list of SIFT features to a numpy array
    descriptors_np = np.concatenate(all_descriptors)

    # Create a KMeans model to cluster the SIFT features
    kmeans = cluster.KMeans(n_clusters=vocab_size, random_state=42)

    # Fit the KMeans model to the SIFT features
    kmeans.fit(descriptors_np)

    return kmeans
def get_histogram(kmeans, descriptors, vocab_size=50):
    # Build a histogram of the cluster centers for each image using the features already extracted
    image_histograms = []

    for feature in tqdm(descriptors, desc="Building histograms"):
        # Predict the closest cluster for each feature
        clusters = kmeans.predict(feature)
        # Build a histogram of the clusters
        histogram, _ = np.histogram(clusters, bins=vocab_size, range=(0, vocab_size))
        image_histograms.append(histogram)

    # Convert the list of histograms to a numpy array
    image_histograms_np = np.array(image_histograms)

    return image_histograms_np

def save_to_file(X_train, X_test, Y_train, Y_test, filename):
    # map the data
    data = {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": Y_train,
        "y_test": Y_test
    }

    # Save the dictionary to a file
    np.savez(filename, **data)
    print(f'Saved data to {filename}')

def show(images, num=10):
    # make a figure to hold the images
    fig, axes = plt.subplots(1, num, figsize=(num, 1))

    # add the images
    for i, ax in enumerate(axes):
        ax.imshow(images[i], cmap='gray')
        ax.axis('off')
    plt.show()

if __name__ == '__main__':
    main()
