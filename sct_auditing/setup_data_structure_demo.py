#imports
import json
import hashlib
import numpy as np
#=========================================================
from setup_data_structure import *
#demo

# read SCTS from a JSON encoded file
# Path to the JSON file

file_path = "sct_auditing/Example_SCTs.json"

# Read the JSON data from the file
with open(file_path, 'r') as file:
    sct_list = json.load(file)

# Output the loaded data to verify
print(len(sct_list))
print(type(sct_list[0]))
print(sct_list[0])

data_structure_for_sct = setup_a_function_bloom_filter(sct_list, 5)

print(data_structure_for_sct)
print(type(data_structure_for_sct))

print(data_structure_for_sct["a_function_bloom_filter"])

