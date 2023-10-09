import tensorflow as tf
import numpy as np
from uci_data import *

def nn_keras(directory, dataset, layers, units_per_layer, epochs):
  (training_set, test_set) = read_uci1(directory, dataset)
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
  model.fit(training_inputs, training_labels, epochs=epochs)

  # Testing the model
  test_loss, test_acc = model.evaluate(test_inputs,  test_labels, verbose=0)
  

  #TODO: print('ID=%5d, predicted=%10s, true=%10s, accuracy=%4.2f\n' % (object_id, predicted_class, true_class, accuracy))

  print('classification accuracy=%6.4f\n' % (test_acc))
  return 0