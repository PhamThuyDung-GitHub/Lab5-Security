# Hexadecimal messages
message_1 = ("d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89"
             "55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8"
             "823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f"
             "33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70")

message_2 = ("d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8"
             "955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd728037"
             "3c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d"
             "248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965a"
             "b6ff72a70")

# Converting hex messages to bytes
message_1_bytes = bytes.fromhex(message_1)
message_2_bytes = bytes.fromhex(message_2)

# Lengths of the messages in bytes
len_message_1 = len(message_1_bytes)
len_message_2 = len(message_2_bytes)

# Maximum length for comparison (shortest of the two messages)
max_length = min(len_message_1, len_message_2)

# Recalculating the byte difference, considering the full lengths
byte_diff_full = sum(1 for b1, b2 in zip(message_1_bytes[:max_length], message_2_bytes[:max_length]) if b1 != b2)

# Including the difference in length as additional differing bytes
total_byte_diff = byte_diff_full + abs(len_message_1 - len_message_2)

total_byte_diff
