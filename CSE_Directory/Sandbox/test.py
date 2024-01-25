import numpy as np

# Assuming arr is your three-dimensional NumPy array
arr = np.reshape(np.arange(4), (2,2))

print(arr)
# Print the result
print(list(zip(arr,arr)))
