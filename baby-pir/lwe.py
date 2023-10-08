import numpy as np

def random_matrix(n, m, p):
    """Generate a random matrix of size n x m with entries from Z_p."""
    return np.random.randint(0, p, size=(n, m))

def random_vector(n, p):
    """Generate a random row vector of size 1 x n with entries from Z_p."""
    return np.random.randint(0, p, size=(1, n))

def random_noise_vector(n):
    """Generate a noise vector of size 1 x n with entries as 0 or 1."""
    return np.random.randint(0, 2, size=(1, n))  # Values in range [0, 2) i.e., 0 or 1

# Example usage:
n = 3
m = 2
p = 7
A = random_matrix(n, m, p)
S = random_vector(n, p)
E = random_noise_vector(m)

# Multiplication
result = np.dot(S, A) % p
b = ( np.dot(S, A) % p ) + E
  # Note: Noise vector is of size 1 x m, same as the multiplication result

# Add noise to the result
# noisy_result = (result + E) % p

print("Matrix A:")
print(A)
print("\nRow Vector S:")
print(S)
print("\nResult of multiplication:")
print(result)
print("\nNoise Vector E:")
print(E)
print("\nNoisy Result:")
print(b)