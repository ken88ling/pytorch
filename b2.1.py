import torch

# Element-wise operations
tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.tensor([4, 5, 6])
element_wise_sum = tensor_a + tensor_b
element_wise_product = tensor_a * tensor_b

# Linear algebra operations
matrix_a = torch.tensor([[1, 2], [3, 4]])
matrix_b = torch.tensor([[5, 6], [7, 8]])
matrix_product = torch.matmul(matrix_a, matrix_b)

# Reduction operations
tensor_c = torch.tensor([1, 2, 3, 4])
sum_all_elements = torch.sum(tensor_c)

print(sum_all_elements)
