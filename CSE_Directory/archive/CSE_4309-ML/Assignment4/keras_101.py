import tensorflow as tf
import numpy as np

print(tf.__version__)

from uci_data import *

#%%

# loading the dataset

(training_set, test_set) = read_uci1("uci_datasets", "pendigits")
(training_inputs, training_labels) = training_set
(test_inputs, test_labels) = test_set

#%%

# Creating the model

input_shape = training_inputs[0].shape
number_of_classes = np.max([np.max(training_labels), np.max(test_labels)]) + 1

model = tf.keras.Sequential([
    tf.keras.Input(shape = input_shape),
#    tf.keras.layers.Dense(50, activation='sigmoid'),
#    tf.keras.layers.Dense(50, activation='sigmoid'),
    tf.keras.layers.Dense(number_of_classes, activation='sigmoid')])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])


# Training the model
model.fit(training_inputs, training_labels, epochs=10)

# Testing the model
test_loss, test_acc = model.evaluate(test_inputs,  test_labels, verbose=0)
print('\nTest accuracy: %.2f%%' % (test_acc * 100))

