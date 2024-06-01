import tensorflow as tf
import numpy as np

print(tf.__version__)

from uci_data import *

#%%

# loading the dataset

(training_set, test_set) = read_uci1("../uci_datasets", "pendigits")
(training_inputs, training_labels) = training_set
(test_inputs, test_labels) = test_set
max_value = np.max(np.abs(training_inputs))
training_inputs  = training_inputs / max_value
test_inputs = test_inputs/ max_value

#%%

# Creating the model

input_shape = training_inputs[0].shape
number_of_classes = np.max([np.max(training_labels), np.max(test_labels)]) + 1

model = tf.keras.Sequential([
    tf.keras.Input(shape = input_shape),
#    tf.keras.layers.Dense(10, activation='sigmoid'),
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

#%%

# applying the model on a specific input vector

test_index = 10 # nothing special about this value
input_vector = test_inputs[test_index,:]
input_vector = np.reshape(input_vector, (1, 16))
nn_output = model.predict(input_vector)
nn_output = nn_output.flatten()

predicted_class = np.argmax(nn_output)
actual_class = test_labels[test_index]
print("predicted: %d\nactual: %d\n" % (predicted_class, actual_class))

(indices,) = np.nonzero(nn_output == nn_output[predicted_class])
print("indices =", indices)
number_of_ties = np.prod(indices.shape)

if (nn_output[actual_class] == nn_output[predicted_class]):
    accuracy = 1.0 / number_of_ties
else:
    accuracy = 0
    
print("accuracy = %.4f" % (accuracy))

#%%


