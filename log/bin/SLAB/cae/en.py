def encrypt(plain_text, key):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr((ord(char) - 97 + key) % 26 + 97)
            encrypted_text += encrypted_char.upper() if is_upper else encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


plain_text = input("Enter the plain text: ")
key = int(input("Enter the key (an integer from 1 to 25): "))
encrypted_text = encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)
