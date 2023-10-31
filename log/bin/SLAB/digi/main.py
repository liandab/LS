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

#function to generate digital signature
def encryption(M, d, n):
    M = pow(M, d, n)
    S = M % n
    print("Your Digital Signature is: ", S)
    return S

#function to decrypt and validate signature
def decryption(S, M, n, e):
    tempM = pow(S, e, n)
    newM = tempM % n
    if (newM==M):
      print("Digital Signature Accepted")
    else:
      print("Invalid Digital Signature")
    
  
#taking user inputs
print("Are you going to give values of p and q?")
quest = input("Y/N: ")
if quest.lower() == 'n':
  n=int(input("Enter the value of n : "))
  factors=findfactors(n)
  p=factors[0]
  q=factors[1]
else:
    p = int(input("Enter value of p: "))
    q = int(input("Enter value of q: "))


erd = input("Are you giving the value of 'e' or 'd'? : ")
if erd.lower() == 'e':
  e = int(input("Enter value of e: "))
  newd = findeord((p - 1) * (q - 1), e)
else:
  d = int(input("Enter value of d: "))
  newd = d

n = p * q
phyn = (p - 1) * (q - 1)
  
print("Value of n is ", n, " and phyn is ", phyn)
  
M = int(input("Enter plaintext value: "))
S = encryption(M, newd, n)
decryption(S, M, n, e)
