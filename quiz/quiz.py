import numpy as np

with open("quiz/module12quizF26.txt", "r") as f:
    data = []
    for line in f:
        data.append(int(line.strip()))
    matrix = np.array(data).reshape(100, 100)

print(matrix)

A = (matrix[73][0] + matrix[73][1] + matrix[73][2]+ matrix[73][3] + matrix[73][4])/5

B_list = [matrix[7][0], matrix[7][1], matrix[7][2], matrix[7][3], matrix[7][4]]
B = min(B_list)

C = max([matrix[60][-1], matrix[60][-2], matrix[60][-3] , matrix[60][-4], matrix[60][-5]])

D = (matrix[0][18] + matrix[1][18] + matrix[2][18])

E = min([matrix[-1][51], matrix[-2][51], matrix[-3][51]])


SHIFT = int(A - B + C - D + E)
print(SHIFT)

plaintext = "abcdefghijklmnopqrstuvwxyz"
ciphertext = plaintext[(len(plaintext)-SHIFT)%len(plaintext):] + plaintext[0:(len(plaintext)-SHIFT)%len(plaintext)]
print(ciphertext)

left_shift = {}
right_shift = {}
for i in range(len(plaintext)):
    left_shift[plaintext[i]] = ciphertext[i]
    right_shift[ciphertext[i]] = plaintext[i]

a = "uzijaktocji"
for letter in a:
    print(left_shift[letter], end="")
print()
for letter in a:
    print(right_shift[letter], end="")
print()

a = "ndhkgzwzoozmocvixjhkgzs"
for letter in a:
    print(left_shift[letter], end="")
print()
for letter in a:
    print(right_shift[letter], end="")