from pwn import xor

input_string = "label"
xor_value = 13

xor_result = xor(input_string, xor_value)
output_string = xor_result.decode()

flag = f"crypto{{{output_string}}}"
print(flag)
