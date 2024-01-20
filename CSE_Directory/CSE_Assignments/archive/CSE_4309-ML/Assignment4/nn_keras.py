import tensorflow as tf
import numpy as np
from uci_data import *

def nn_keras(directory, dataset, num_layers, units_per_layer, epochs):
  # input and formatting data
  (training_set, test_set, label_int_conversions) = read_uci1(directory, dataset)
  (labels_to_ints, ints_to_labels) = label_int_conversions

  (training_inputs, training_labels) = training_set
  (test_inputs, test_labels) = test_set

  # Normalizing
  max_value = np.max(np.abs(training_inputs))
  training_inputs  = training_inputs / max_value
  test_inputs = test_inputs/ max_value

  # Creating the model
  input_shape = training_inputs[0].shape
  number_of_classes = np.max([np.max(training_labels), np.max(test_labels)]) + 1

  # Adding layers 
  layers = [tf.keras.Input(shape = input_shape)]    # input layer
  for i in range(num_layers-2):     # hidden layer(s)
    layers.append(tf.keras.layers.Dense(units_per_layer, activation='sigmoid'))
  layers.append(tf.keras.layers.Dense(number_of_classes, activation='sigmoid'))    # output layer
  model = tf.keras.Sequential(layers=layers)

  model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])


  # Training the model
  model.fit(training_inputs, training_labels, epochs=epochs)

  # Testing the model
  predictions = model.predict(test_inputs)

  accuracies = []
  for (i, prediction) in enumerate(predictions):
    predicted = np.argmax(prediction)

    accuracy = 0
    if predicted == test_labels[i][0]:
      accuracy = 1 / np.count_nonzero(prediction == prediction[predicted])
    accuracies.append(accuracy)

    print('ID=%5d, predicted=%10s, true=%10s, accuracy=%4.2f' % (
      i+1, 
      ints_to_labels[predicted],
      ints_to_labels[test_labels[i][0]], 
      accuracy))

  test_acc = sum(accuracies)/len(accuracies)
  print('classification accuracy=%6.4f' % (test_acc))
  return test_acc