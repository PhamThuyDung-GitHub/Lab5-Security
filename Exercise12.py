import hashlib

def calculate_hashes(input_data, hash_types):
    hashes = {}
    
    for hash_type in hash_types:
        hasher = hashlib.new(hash_type)
        hasher.update(input_data)
        hashes[hash_type] = hasher.hexdigest()
    
    return hashes

def calculate_hashes_from_file(file_path, hash_types):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        return calculate_hashes(file_data, hash_types)

# Test with "UIT Cryptography" as a text string
text_input = "UIT Cryptography".encode()
hash_types = ["md5", "sha1", "sha256"]
text_hashes = calculate_hashes(text_input, hash_types)

# Test with a hex string (e.g., "aabbccddeeff")
hex_input = bytes.fromhex("aabbccddeeff")
hex_hashes = calculate_hashes(hex_input, hash_types)

# Test with the "student.txt" file
file_path = "student.txt"  
file_hashes = calculate_hashes_from_file(file_path, hash_types)

print("Text Hashes:")
for hash_type, hash_value in text_hashes.items():
    print(f"{hash_type.upper()}: {hash_value}")

print("\nHex String Hashes:")
for hash_type, hash_value in hex_hashes.items():
    print(f"{hash_type.upper()}: {hash_value}")

print("\nFile Hashes:")
for hash_type, hash_value in file_hashes.items():
    print(f"{hash_type.upper()}: {hash_value}")
