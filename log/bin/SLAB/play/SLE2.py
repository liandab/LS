class PlayfairCipher:
    def __init__(self):
        self.length = 0
        self.table = []
        self.main()

  #taking user input
    def main(self):
        print('\n')
        key = input("Enter the key: ").upper()
        while key == "":
            key = input("Enter the key: ").upper()
        self.table = self.cipher_table(key)
        input_text = input("Enter the plaintext: ").upper()
        while input_text == "":
            input_text = input("Enter the plaintext: ").upper()
        output = self.cipher(input_text)
        decoded_output = self.decode(output)
        self.key_table(self.table)
        self.print_results(output, decoded_output)

    def parse_string(self, text):
        text = text.upper()
        text = ''.join(filter(str.isalpha, text))
        text = text.replace("J", "I")
        return text

  #generating cypher text
    def cipher_table(self, key):
        playfair_table = [['' for _ in range(5)] for _ in range(5)]
        key_string = self.parse_string(key)
        key_set = set(key_string)
        remaining_letters = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        remaining_letters = [letter for letter in remaining_letters if letter not in key_set]
        
        index = 0
        for i in range(5):
            for j in range(5):
                if index < len(key_string):
                    playfair_table[i][j] = key_string[index]
                    key_set.add(key_string[index])
                    index += 1
                else:
                    playfair_table[i][j] = remaining_letters[index - len(key_string)]
                    index += 1
        
        return playfair_table

    def cipher(self, text):
        # Prepare the text by removing non-alphabet characters and replacing J with I
        text = self.parse_string(text)
        
        # Add padding 'X' if the length is odd
        if len(text) % 2 != 0:
            text += 'X'
        
        # Split the text into digraphs (pairs of characters)
        digraphs = [text[i:i+2] for i in range(0, len(text), 2)]
        
        # Encrypt each digraph using the Playfair algorithm
        enc_digraphs = self.encode_digraph(digraphs)
        
        # Combine the encrypted digraphs into the final encrypted message
        return ''.join(enc_digraphs)

  #generating cyphertext
    def encode_digraph(self, digraphs):
        encipher = []
        for digraph in digraphs:
            a, b = digraph[0], digraph[1]
            r1, c1 = self.get_point(a)
            r2, c2 = self.get_point(b)
            if r1 == r2:
                c1 = (c1 + 1) % 5
                c2 = (c2 + 1) % 5
            elif c1 == c2:
                r1 = (r1 + 1) % 5
                r2 = (r2 + 1) % 5
            else:
                c1, c2 = c2, c1
            encipher.append(self.table[r1][c1] + self.table[r2][c2])
        return encipher

  #decoding the cyphertext
    def decode(self, text):
        decoded = ""
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            r1, c1 = self.get_point(a)
            r2, c2 = self.get_point(b)
            if r1 == r2:
                c1 = (c1 - 1) % 5
                c2 = (c2 - 1) % 5
            elif c1 == c2:
                r1 = (r1 - 1) % 5
                r2 = (r2 - 1) % 5
            else:
                c1, c2 = c2, c1
            decoded += self.table[r1][c1] + self.table[r2][c2]
        return decoded

    def get_point(self, c):
        for i in range(5):
            for j in range(5):
                if c == self.table[i][j]:
                    return i, j
        return 0, 0

  #printing the key table
    def key_table(self, print_table):
        print("\nPlayfair Cipher Key Matrix:")
        print()
        for row in print_table:
            print(' '.join(row))
        print()

  #printing the results
    def print_results(self, encipher, dec):
        print("Encrypted Message:", encipher)
        print("\nDecrypted Message:", dec)


if __name__ == "__main__":
    pf = PlayfairCipher()
