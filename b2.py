import torch

# Create a tensor from a list
tensor_a = torch.tensor([1, 2, 3, 4])

# Create a tensor from a NumPy array
import numpy as np

numpy_array = np.array([5, 6, 7, 8])
tensor_b = torch.from_numpy(numpy_array)

print(tensor_b)
