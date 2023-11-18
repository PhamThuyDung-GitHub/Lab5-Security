import hashlib

def calculate_hash(input_data, hash_type):
    if hash_type not in ('md5', 'sha1', 'sha256'):
        raise ValueError("Invalid hash type. Supported types: md5, sha1, sha256")

    hasher = hashlib.new(hash_type)
    
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')

    hasher.update(input_data)
    return hasher.hexdigest()

# Example 1: Calculate hash values for "UIT Cryptography" as a text string
text_input = "UIT Cryptography"
for hash_type in ['md5', 'sha1', 'sha256']:
    result = calculate_hash(text_input, hash_type)
    print(f"{hash_type.upper()} Hash: {result}")

# Example 2: Calculate hash values for a hex string
hex_input = "1a2b3c4d5e6f"
for hash_type in ['md5', 'sha1', 'sha256']:
    result = calculate_hash(bytes.fromhex(hex_input), hash_type)
    print(f"{hash_type.upper()} Hash for Hex Input: {result}")

# Example 3: Calculate hash values for a file
def calculate_file_hash(file_path, hash_type):
    with open(file_path, 'rb') as file:
        data = file.read()
        return calculate_hash(data, hash_type)

# Create a text file with your name and student ID
with open("student_info.txt", "w") as file:
    file.write("Pham Thuy Dung - 20521214")

# Calculate MD5 and SHA-1 hash values for the file
for hash_type in ['md5', 'sha1']:
    result = calculate_file_hash("student_info.txt", hash_type)
    print(f"{hash_type.upper()} Hash for File: {result}")

