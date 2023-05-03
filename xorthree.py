def xor_single_byte_key(hex_data, key):
    decoded_data = bytes.fromhex(hex_data)
    result = ''.join(chr(byte ^ key) for byte in decoded_data)
    return result

hex_data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

for key in range(256):
    decrypted_message = xor_single_byte_key(hex_data, key)
    if "crypto" in decrypted_message:
        print(f"Key: {key}, Message: {decrypted_message}")
        break
