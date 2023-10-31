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
    
def brute_force_attack(cipher_text):
    decrypted_messages = {}
    for key in range(1, 26):
        decrypted_text = decrypt(cipher_text, key)
        decrypted_messages[key] = decrypted_text
    return decrypted_messages

cipher_text = input("Enter the cipher text: ")
decrypted_messages = brute_force_attack(cipher_text)
print("Brute Force Attack Results:")

for key, decrypted_text in decrypted_messages.items():
    print(f"Key: {key}, Decrypted Text: {decrypted_text}")