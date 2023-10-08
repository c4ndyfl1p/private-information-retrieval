import numpy as np

def random_matrix(n, m, p):
    """Generate a random matrix of size n x m with entries from Z_p."""
    return np.random.randint(0, p, size=(n, m))

def random_vector(m, p):
    """Generate a random row vector of size m * 1 with entries from Z_p."""
    return np.random.randint(0, p, size=(m, 1))

def random_noise_vector(n):
    """Generate a noise vector of size n * 1 with entries as 0 or 1."""
    return np.random.randint(0, 2, size=(n, 1))  # Values in range [0, 2) i.e., 0 or 1

# Example usage:
n = 2
m = 3
p = 97
A = random_matrix(n, m, p)
print(A.shape)
print("Matrix A:")
print(A)
S = random_vector(m, p)

print(S.shape)
print("\n S:")
print(S)


# Multiplication
result = np.dot(A, S) % p
print("\nResult of multiplication A * S:")
print(result)
print(result.shape)

E = random_noise_vector(n)
print("\nNoise Vector E:")
print(E)
print(E.shape)

# # Add noise to the result
noisy_result = (result + E) % p

print("\nNoisy Result:")
print(noisy_result)