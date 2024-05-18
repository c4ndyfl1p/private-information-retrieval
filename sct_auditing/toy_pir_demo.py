from toy_pir import *
s = keygen()
desired_idx = 3
query = generate_query(desired_idx)

print("Sending the query to the server...")
db = [0,0,0,0,1]
answer = answer_query(query, db)

print("Got the answer back from the server...")

result = decrypt(s, answer)

print("The item at index %d of the database is %d" % (desired_idx, result))