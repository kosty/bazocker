import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))

import numpy as np

# Create a simple numpy array
arr = np.array([1, 2, 3, 4, 5])

# Print the array
print("Numpy is working! Here is a sample array:")
print(arr)

# Print the sum of elements in the array
print("Sum of the array elements:", np.sum(arr))
