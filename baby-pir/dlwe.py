from lwe_new import random_matrix, random_vector, random_noise_vector
import numpy as np

n =2
m=3
p=97


def sample_true():
    
    A = random_matrix(n, m, p)
    s = random_vector(m, p)
    E = random_noise_vector(n)
    # b = A * s + e
    b = ( np.dot(A, s) % p ) + E
    # print(b.shape)
    
    return (A, b)

def sample_random():
    A = random_matrix(n, m, p)
    b = random_vector(n, p)
    
    return (A, b)


print("----")
print("sample True")

A, b = sample_true()

print("Matrix A:")
print(A)
print("\nNoisy Result:")
print(b)

print("==========================")

print("sample_random")
A, b = sample_random()
print("Matrix A:")
print(A)
print("\n random output")
print(b)