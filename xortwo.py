def xor_hex_strings(a, b):
    return hex(int(a, 16) ^ int(b, 16))[2:]

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_xor_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_xor_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_xor_KEYS = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# Step 1: Get KEY2
KEY2 = xor_hex_strings(KEY1, KEY2_xor_KEY1)

# Step 2: Get KEY3
KEY3 = xor_hex_strings(KEY2, KEY2_xor_KEY3)

# Step 3: Get FLAG
FLAG = xor_hex_strings(FLAG_xor_KEYS, KEY1)
FLAG = xor_hex_strings(FLAG, KEY2)
FLAG = xor_hex_strings(FLAG, KEY3)

# Convert FLAG from hex to ASCII
flag_ascii = bytes.fromhex(FLAG).decode('utf-8')
print(flag_ascii)
