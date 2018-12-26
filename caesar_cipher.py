alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = int(input())
plain = input()
cipher = ""
for letter in plain:
    cipherLetter = (alphabet.find(letter)+key) % 26
    cipher += alphabet[cipherLetter]
print(cipher)
