from lwe_new import *
from homomorphic_enc import *

n = 512
q = 3329
noise_distribution = [-3, 3]

num_items_in_db = 50
desired_idx = 24
db = [random_bit() for i in range(num_items_in_db)]

def generate_query(desired_idx):
    v = []
    for i in range(num_items_in_db):
        bit = 1 if i == desired_idx else 0
        ct = encrypt(s, bit)
        v.append(ct)
    return v

def answer_query(query, db):
    summed_A = zero_matrix(n, n)
    summed_c = zero_vector(n)
    for i in range(num_items_in_db):
        if db[i] == 1:
            (A, c) = query[i]
            summed_A += A
            summed_c += c
    return (summed_A, summed_c)

s = keygen()
query = generate_query(desired_idx)

print("Sending the query to the server...")

answer = answer_query(query, db)

print("Got the answer back from the server...")

result = decrypt(s, answer)

print("The item at index %d of the database is %d", desired_idx, result)

assert result == db[desired_idx]
print("PIR was correct!")