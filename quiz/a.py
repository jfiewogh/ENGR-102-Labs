shift = 5

plaintext = "abcdefghijklmnopqrstuvwxyz"

# right shift
# ciphertext = plaintext[shift%len(plaintext):] + plaintext[0:shift%len(plaintext)]

# left shift
ciphertext = plaintext[(len(plaintext)-shift)%len(plaintext):] + plaintext[0:(len(plaintext)-shift)%len(plaintext)]

print(ciphertext)