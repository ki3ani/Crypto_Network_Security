def xor_strings(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

hex_data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
decoded_data = bytes.fromhex(hex_data).decode('latin1')

known_flag_start = "crypto{"

# XOR the beginning of the decoded_data with the known_flag_start to get the beginning of the secret key
partial_key = xor_strings(decoded_data[:len(known_flag_start)], known_flag_start)

# Assuming the key has the same length as the known_flag_start, repeat it to match the length of decoded_data
key = partial_key * (len(decoded_data) // len(partial_key)) + partial_key[:len(decoded_data) % len(partial_key)]

# XOR the decoded_data with the repeated key
decrypted_message = xor_strings(decoded_data, key)

print(f"Key: {partial_key}")
print(f"Message: {decrypted_message}")
