import torch

print(torch.__version__)

# Create a random tensor of size 2x2
x = torch.randn(2, 2)

# Print the tensor
print(x)

# Perform a basic operation (e.g., matrix multiplication)
y = torch.matmul(x, x)
print(y)

print(torch.cuda.is_available())
