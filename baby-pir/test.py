import numpy as np

# Define the matrix A and the vector S
A = np.array([[2, 1, 1],
              [4, 5, 3]])
print(A.shape)

S = np.array([[5],
              [4],
              [3]])
print(S.shape)

# Multiply A and S
result = np.dot(A, S)

print("Result of A * S:")
print(result)