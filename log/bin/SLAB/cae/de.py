def decrypt(cipher_text, key):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr((ord(char) - 97 - key) % 26 + 97)
            decrypted_text += decrypted_char.upper() if is_upper else decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

cipher_text = input("Enter the cipher text: ")
key = int(input("Enter the key (an integer from 1 to 25): "))
decrypted_text = decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)