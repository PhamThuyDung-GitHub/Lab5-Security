import hashlib

def sha1_of_file(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while True:
            # Read file in chunks of 4K
            chunk = f.read(4096)
            if not chunk:
                break
            sha1.update(chunk)
    return sha1.hexdigest()


sha1_hash_1 = sha1_of_file('shattered-1.pdf')
sha1_hash_2 = sha1_of_file('shattered-1.pdf')

print(f'The SHA-1 hash of the first file is: {sha1_hash_1}')
print(f'The SHA-1 hash of the second file is: {sha1_hash_2}')
