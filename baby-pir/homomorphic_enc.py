from lwe_new import random_matrix, random_vector, random_noise_vector
import numpy as np



n = 512
m = 512
p = 3329

n = 2
m = 3
p = 7

noise_distribution = [-3, 3]

def get_LWE_sample(s):
    A = random_matrix(n,m,p)
    e = random_noise_vector(n)    
    # b = A * s + e
    b = ( np.dot(A, s) % p ) + e   
    return (A, b)


def keygen():
    s = random_vector(m, p)
    return s

def encrypt(s, x):
    # assert x == 0 or x == 1 # this is the message
    (A, b) = get_LWE_sample(s)
    c = b + np.floor(p / 2) * x
    return (A, c)

def decrypt(s, A, c):
    # raw = c -A * s
    raw = c - (np.dot(A, s) %p )
    return np.round(raw * 2 / p)

#==================================

s = keygen()
print(f"s: {s}")

# (A, b) = get_LWE_sample(s)
# print(f"b=As+e = {b}\n")     


# message (dim: 1 * m )
x= np.array([0,1])
# x = np.array([[1]])
#
(A, c) = encrypt(s, x)
print(f"A:{A}\n")
print(f"c:{c}\n")

pt = decrypt(s, A, c)
print(f"pt: {pt}")