txt = input("Enter Text: ")
kw = input("Enter Keyword: ")
kw=kw.upper()
m = [[' ' for _ in range(5)] for _ in range(5)]

def encrypt(txt,mat):
  txt=txt.upper()
  li=[]
  for c in txt:
    li.append(c)

  print(li,"\n")
  
  for i in range(5):
    for j in range(5):
        if mat[i][j] in li:
            f1 = mat[i][j]
            row = i
            col = j
            print(f"Element {f1} found at row {row}, column {col}")
        
print("\n\n")
flag=0
for i in range(5):
    for j in range(5):
        if flag < len(kw):
            m[i][j] = kw[flag]
            flag += 1
          
import string
alphabet = list(filter(lambda letter: letter != 'J', string.ascii_uppercase))

for i in range(5):
    for j in range(5):
        if m[i][j] == ' ':
            for char in alphabet:
                if char not in [m[x][y] for x in range(5) for y in range(5)]:
                    m[i][j] = char
                    alphabet.remove(char)
                    break
          
for i in range(5):
    for j in range(5):
        print(m[i][j],end=" ")
    print() 

encrypt(txt,m)

  
  # for i in range(5):
  #   for j in range(5):
      