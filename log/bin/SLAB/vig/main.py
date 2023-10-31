def encrypt (key,ptext):
  key_len=len(key)
  encrypted=[]
  # for i in range (0,key_len):
  #      e=ptext[i]+key[i]
  #      encrypted.append(e)
  # print('\n',encrypted)

  # # for i in range(len(ptext_len)):
  # #       key_char = key[i % key_len]
  # #       e = ptext[i] + key_char
  # #       encrypted.append(e)

  # echar=[]
  # for i in encrypted:
  #   print(i)
  #   temp_echar=chr(i)
  #   # print(temp_echar)
  #   echar.append(temp_echar)
  # print('Encrypted text is: ',echar)
  for i in range(len(ptext)):
        key_char = key[i % key_len]
        e = (ptext[i] + key_char) % 26
        encrypted.append(e)
  encrypted_text = ''.join(chr(e + ord('A')) for e in encrypted)
  print('Encrypted text is:', encrypted_text)
  for i in encrypted_text:
    tempchar = i.upper()
    temp_enc = ord(tempchar) - ord('A')
    encrypted.append(temp_enc)
  decrypt(key,encrypted)
  

# def decrypt (key, encrypted):
#   key_len=len(key)
#   decrypted=[]
#   for i in range (0,key_len):
#       e=encrypted[i]-key[i]
#       decrypted.append(e)
#   print('\n',decrypted)

#   dchar=[]
#   for i in decrypted:
#     print(i)
#     temp_dchar=chr(i)
#     # print(temp_dchar)
#     dchar.append(temp_dchar)
  
#   PText=''.join(dchar)
#   print('Decrypted text is: ',PText)
def decrypt(key, encrypted):
    key_len = len(key)
    decrypted = []

    for i in range(len(encrypted)):
        key_char = key[i % key_len]
        d = (encrypted[i] - key_char + 26) % 26  # Adding 26 to handle negative values
        decrypted.append(d)

    decrypted_text = ''.join(chr(d + ord('A')) for d in decrypted)
    print('Decrypted text is:', decrypted_text)
  

#taking user input
ptext = input('Enter thy plaintext: ')
key = input('Enter thy key: ')
print('\n')

k = []
p = []

for i in key:
    tempchar = i.upper()
    tempk = ord(tempchar)
    k.append(tempk)

print('\nThe key list is:', k)

for i in ptext:
    temp_pt = i.upper()
    temp_pt = ord(temp_pt)
    p.append(temp_pt)

# Repeat the key characters to match the length of plaintext
key_repeated = []
ptext_len = len(ptext)
key_len = len(k)
for i in range(ptext_len):
    key_char = k[i % key_len]
    key_repeated.append(key_char)

print('\nThe key repeated list is:', key_repeated)

encrypt(key_repeated, p)


  

