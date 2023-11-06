import numpy as np
import random
from drawing import * # TODO optional: use drawing file to visualize clusters

def input_file(file_name):
  file = open(file_name)
  file_lines = file.readlines()
  file.close()

  rows = len(file_lines)
  cols = len(file_lines[0].split())
  data = np.zeros((rows, cols))

  for (i, row) in enumerate(file_lines):
    for (j, num) in enumerate(row.split()):
      data[i][j] = num

  return data
def initialize(num_rows, K, initialization):
  labels = np.zeros(num_rows, dtype=int)
  match initialization:
    case "round_robin":
      for i in range(num_rows):
        labels[i] = i % K
    case "random":
      for i in range(num_rows):
        labels[i] = random.randint(0,K-1)
  
  return labels

def L2(point, points):
  delta = np.subtract(point, points)
  return np.sqrt(np.sum(np.square(delta), axis = 1))

def k_means(data_file, K, initialization):
  data = input_file(data_file)
  labels = initialize(len(data), K, initialization)
  
  changed = True
  while changed:
    changed = False

    # grouping by label
    grouped = np.hstack((data, labels[:,None])) # combine
    grouped = grouped[grouped[:, -1].argsort()] # sort
    i_groups = np.unique(grouped[:, -1], return_index=True)[1][1:] # groups
    grouped = np.split(grouped[:,:-1], i_groups)

    # mean of each label
    
    means = np.zeros((len(grouped), len(data[0])))
    for (i, group) in enumerate(grouped):
      means[i] = np.mean(group, axis=0)

    # update each data point's label
    for (i, point) in enumerate(data):
      distances = L2(point, means)
      next_label = np.argmin(distances)

      if(labels[i] != next_label):
        labels[i] = next_label
        changed = True

  for (i, point) in enumerate(data):
    print(*["%10.4f" % dim for dim in point], ' --> cluster %d' % (labels[i]+1))

  # comment out if desired or if matplotlib cant handle the number of dimentions.
  draw_assignments(data.T, labels)
  plot.show()
