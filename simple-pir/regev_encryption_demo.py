from regev_encryption_schemised import sampleLWE, regevDecrpt, regevEncrypt

import numpy as np
# parameters
n = 2**10
m = 5 # sqrt(N), number of samples

error_values = {
    "loc": 0,
    "sigma": 6.4,
}
q = 2**23
p = 991 # plaintext modulus
scaling_factor = np.floor(q/p)
# x = np.random.choice([i for i in range(0, p+1)], m)
x = np.random.choice([i for i in range(0, 2)], m)

# x = np.array([0, 1])

print(f"scaling_factor = floor(q/p) = {np.floor(q/p)}")
print(f"x = {x}")


secret= np.random.randint(0, q, (n))

A, b = sampleLWE(m,n,q,error_values, secret)

c = regevEncrypt(b, x, p, q)

print(c)

print(f"x = {x}")
d = regevDecrpt(A, secret, q, p, c)

# errors: if d is 991. , it's 0 