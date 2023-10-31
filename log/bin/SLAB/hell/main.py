#method to generate Public key
def keygeneration(P,G,pk):
  Key=(G**pk)%P
  return Key

#method to generate Secret Key
def SecretKey(y,a,P):
  SKey=(y**a)%P
  return SKey

#taking user inputs
P=int(input("Enter value of q for A: "))
G=int(input("Enter value of ∝ for A: "))
#taking private key and ensuring it is less than G
Aflag=1
# while Aflag!=0:
a=int(input("Enter key component for A: "))
  # if (a<=G):
  #   Aflag=0
  # else:
  #   print("Private key should be less than ∝")
  #   print("Retry")

# Bflag=1
# while Bflag!=0:
b=int(input("Enter key component for B: "))
  # if (b<=G):
  #   Bflag=0
  # else:
  #   print("Private key should be less than ∝")
  #   print("Retry")

#printing the Public Key
A_Key = keygeneration(P,G,a)
print("\nPublic Key of A: ",A_Key)
B_Key = keygeneration(P,G,b)
print("Public Key of B: ",B_Key)

#printing the Secret Key
A_SKey = SecretKey(B_Key,a,P)
B_SKey = SecretKey(A_Key,b,P)
print("\nSecret key for A: ",A_SKey)
print("Secret Key for B: ",B_SKey)