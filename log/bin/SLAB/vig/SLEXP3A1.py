# method to encrypt the plaintext taking key and plaintext
def encrypt(key, ptext):
    key_len = len(key)
    encrypted = []

    for i in range(len(ptext)):
        key_char = key[i % key_len]
      #performing encryption and appending the results to the list
        e = (ptext[i] + key_char) % 26
        encrypted.append(e)
    print('\n Encrypted List is: ',encrypted)

    encrypted_text = ''.join(chr(e + ord('A')) for e in encrypted)
    return encrypted_text

#method to decrypt the encrypted text using key
def decrypt(key, encrypted):
  #generating key length
    key_len = len(key) 
    decrypted = []

    for i in range(len(encrypted)):
        key_char = key[i % key_len]
      #performing decryption and appending the results to the list
        d = (encrypted[i] - key_char + 26) % 26
        decrypted.append(d)
    print('\n Decrypted List is: ',decrypted)
    decrypted_text = ''.join(chr(d + ord('A')) for d in decrypted)
    return decrypted_text

# Taking user input:
ptext = input('Enter thy plaintext: ')
key = input('Enter thy key: ')

k = []
for i in key:
    tempchar = i.upper()
  #converting the characters to their respective ASCII value
    tempk = ord(tempchar) - ord('A')  # Subtract 'A' to get the key values in the range 0-25
    k.append(tempk)

#calling encryption and decryption methods by sending respective ASCII values
encrypted_text = encrypt(k, [ord(c) - ord('A') for c in ptext.upper()])
decrypted_text = decrypt(k, [ord(c) - ord('A') for c in encrypted_text])

#printing the results
print(" ")
print('Encrypted text is:', encrypted_text)
print('Decrypted text is:', decrypted_text)
