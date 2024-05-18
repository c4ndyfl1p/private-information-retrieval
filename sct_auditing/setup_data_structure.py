#imports
import json
import hashlib
import numpy as np

#=========================================================
#functions

def serialise_and_hash(salt, sct):
    """salt :   <class 'bytes'>
        sct : <class 'dict'>
        return: <class 'str'>
    """
    # Serialize the SCT1 data into a JSON string
    sct_serialized = json.dumps(sct)

    # Define a salt (this should be kept secure and used consistently if needed for verification later)
    # salt = b'my_secure_salt'

    # Create a SHA256 hash object and update it with the salt and the serialized data
    hash_obj = hashlib.sha256()
    hash_obj.update(salt)  # Update with the salt
    hash_obj.update(sct_serialized.encode())  # Update with the serialized SCT1 data

    # Get the hexadecimal representation of the hash
    sct_hashed = hash_obj.hexdigest()

    # Output the hashed SCT1
    return sct_hashed

def get_index_in_bloom_filter( bloom_filter_size, hashed_sct):
    # Convert the hash to an index for the Bloom filter

    hash_as_integer = int(hashed_sct, 16)  # Convert hex hash to an integer
    index = hash_as_integer % bloom_filter_size  # Compute index for the Bloom filter

    # print(f"index is {index}")
   

    # Output the index
    return index

def setup_a_function_bloom_filter(sct_list, bloom_filter_size):
    salt_list= [b'salt0', b'salt1', b'salt2', b'salt3', b'salt4']

    # generate random salts

    no_of_hash_functions = bloom_filter_size
    bloom_filter_1 = np.array(  [[0] * bloom_filter_size] * no_of_hash_functions  ) # Initialize the Bloom filter with zeros
    

    for i, sct in enumerate(sct_list):
        # print(f"i: {i}, sct: {sct}")
        for j, salt in enumerate(salt_list):
            # print(f"j: {j}, salt: {salt}")
            sct_i_hashed = serialise_and_hash( salt, sct)
            index_in_j = get_index_in_bloom_filter( bloom_filter_size, sct_i_hashed)
            # print(f"updating element {j}, {index_in_j}")
            bloom_filter_1[j, index_in_j]=1
            # print(bloom_filter_1)

    return { 
        "a_function_bloom_filter": bloom_filter_1, 
        "salt_list" : salt_list 
        }


# #=========================================================
# #demo

# # read SCTS from a JSON encoded file
# # Path to the JSON file

# file_path = "sct_auditing/Example_SCTs.json"

# # Read the JSON data from the file
# with open(file_path, 'r') as file:
#     sct_list = json.load(file)

# # Output the loaded data to verify
# print(len(sct_list))
# print(type(sct_list[0]))
# print(sct_list[0])

# data_structure_for_sct = setup_a_function_bloom_filter(sct_list, 5)

# print(data_structure_for_sct)
# print(type(data_structure_for_sct))

# print(data_structure_for_sct["a_function_bloom_filter"])

