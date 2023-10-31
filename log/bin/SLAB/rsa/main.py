from itertools import count 

#function to find factors
def findfactors(n):
  flag=0
  factors = []
  for i in count(2):
    if (n%i==0):
      if(flag<2):
        factors.append(i)
        flag=flag+1
      else:
        break
  print("Factors are : ",factors)
  return factors  

# function to find e or d
def findeord(phyn, eord):
    for k in count(1):
        if (phyn * k + 1) % eord == 0:
            d = (phyn * k + 1) // eord
            print("Your d is: ", d)
            break
    return d

#function to encrypt
def encryption(C, e, n):
    M = pow(C, e, n)
    CT = M % n
    print("Your Encryption is: ", CT)
    return CT

#function to decrypt
def decryption(CT, d, n):
    M = pow(CT, d, n)
    DE = M % n
    print("Decryption is: ", DE)
  
#taking user inputs

# if quest.lower() == 'n':
#   n=int(input("Enter the value of n : "))
#   factors=findfactors(n)
#   p=factors[0]
#   q=factors[1]
# else:
#     p = int(input("Enter value of p: "))
#     q = int(input("Enter value of q: "))

Ea = int(input("Enter e for A: "))
na=int(input("Enter the value of n for A: "))
factors=findfactors(na)
pa=factors[0]
qa=factors[1]

print("\n")
Eb = int(input("Enter e for B: "))
nb=int(input("Enter the value of n for B: "))
factors=findfactors(nb)
pb=factors[0]
qb=factors[1]

newdA = findeord((pa - 1) * (qa - 1), Ea)
newdB = findeord((pb - 1) * (qb - 1), Eb)

ch = int(input("1. A -> B\n2. B -> A\n"))
if ch==1:
  M = int(input("Enter plaintext value: "))
  CT = encryption(M, Eb, nb)
  decryption(CT, newdB, nb)
else:
  M = int(input("Enter plaintext value: "))
  CT = encryption(M, Ea, na)
  decryption(CT, newdA, na)
  
# erd = input("Are you giving the value of 'e' or 'd'? : ")
# if erd.lower() == 'e':
  # e = int(input("Enter value of e: "))
  # newd = findeord((p - 1) * (q - 1), e)
# else:
#   d = int(input("Enter value of d: "))
#   newd = d

# n = p * q
# phyn = (p - 1) * (q - 1)
  
# print("Value of n is ", n, " and phyn is ", phyn)
  
# M = int(input("Enter plaintext value: "))
# CT = encryption(M, e, n)
# decryption(CT, newd, n)
