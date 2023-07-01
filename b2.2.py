import torch

tensor = torch.tensor([1, 2, 3, 4, 5, 6])

# Accessing individual elements
print(tensor[0])  # Output: 1

# Slicing
print(tensor[1:4])  # Output: tensor([2, 3, 4])

# Modifying elements
tensor[2] = 10
print(tensor)  # Output: tensor([1, 2, 10, 4, 5, 6])
