import base64, hashlib, binascii

# encoded = base64.b64encode(b'data to be encoded')
# print(encoded.hex())  # shows that final encoding of base64 is actually ASCII octets, NOT the 'mapped' base64 'codepoint'
# #b'ZGF0YSB0byBiZSBlbmNvZGVk'
# data = base64.b64decode(encoded)
# print(data)


result = hashlib.md5(b"Some random input data enough to be somewhat something that sortof could be hashed.")
print(type(result))
print(result.digest_size)  # 16 bytes == 128 bits
print(result.digest())
#print(result.digest().hex())
print(result.hexdigest())  # uses 2 chars to represent each byte in the hash, so 32 chars

#print(b'\x7f\xf6r\x17%'.hex())


encoded = base64.b64encode(result.digest())  # divides the hash into 22 sextets, each of which encodes to a char (total of 24 with padding)
print(encoded)                               # so the resulting string is shorter than the hex representation of the md5 hash
print(encoded.decode('ascii'))
print(encoded.hex())

# s = "text".encode('utf-16')
# print(s.decode('utf-16'))
# print(s.hex())
#
# print("text".encode('utf-8').hex())
# print(binascii.hexlify(b"text"))
print()
print()
t = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKL"
print(t.encode('ascii').hex())
print(base64.b64encode(t.encode('ascii')).decode('ascii'))