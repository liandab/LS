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

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Attack")
        print("4. Exit")
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            plain_text = input("Enter the plain text: ")
            key = int(input("Enter the key (an integer from 1 to 25): "))
            encrypted_text = encrypt(plain_text, key)
            print("Encrypted text:", encrypted_text)
        elif choice == 2:
            cipher_text = input("Enter the cipher text: ")
            key = int(input("Enter the key (an integer from 1 to 25): "))
            decrypted_text = decrypt(cipher_text, key)
            print("Decrypted text:", decrypted_text)
        elif choice == 3:
            cipher_text = input("Enter the cipher text: ")
            decrypted_messages = brute_force_attack(cipher_text)
            print("Brute Force Attack Results:")
            for key, decrypted_text in decrypted_messages.items():
                print(f"Key: {key}, Decrypted Text: {decrypted_text}")
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
