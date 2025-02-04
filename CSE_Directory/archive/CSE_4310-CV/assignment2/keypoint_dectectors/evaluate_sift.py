# README
# this is very basic code. The primary purpose of having this separated from feature_extraction is to reduce processing times
# The code does show a couple warning but this also occurs in the professors code. The code also works normally still.

import numpy as np
from sklearn.svm import LinearSVC

def main():
    # Load the data from feature_extraction.py
    data = np.load("sift.npz") # dictionary of arrays
    train_histogram = data['X_train'] 
    test_histogram = data['X_test']
    train_labels = data['y_train']
    test_labels = data['y_test']

    # Create an SVM model
    svm = LinearSVC(random_state=42)

    # Train the model
    svm.fit(train_histogram, train_labels)

    # Evaluate the model
    prediction = svm.predict(test_histogram)
    total_matches = sum(prediction==test_labels)
    accuracy = total_matches / len(test_labels)

    print(f'SVM matches: {total_matches:d}')
    print(f'SVM accuracy: {accuracy:.2f}')

if __name__ == '__main__':
    main()
