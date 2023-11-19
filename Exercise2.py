import hashlib

# Provided HEX messages
message_1 = "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89" \
            "55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8" \
            "823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f" \
            "33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"
message_2 = "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8" \
            "955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd728037" \
            "3c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d" \
            "248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965a" \
            "b6ff72a70"

# Remove spaces and any non-hexadecimal characters to ensure proper hex format
message_1_clean = ''.join(message_1.split())
message_2_clean = ''.join(message_2.split())

# Calculate the byte difference
byte_difference_clean = sum(1 for x, y in zip(message_1_clean, message_2_clean) if x != y) // 2  # Divide by 2 as each hex digit is half a byte

# MD5 hashes for each message
md5_hash_1_clean = hashlib.md5(bytes.fromhex(message_1_clean)).hexdigest()
md5_hash_2_clean = hashlib.md5(bytes.fromhex(message_2_clean)).hexdigest()

byte_difference_clean, md5_hash_1_clean, md5_hash_2_clean
