import math
p=int(input("Enter 1st prime number: "))

q=int(input("Enter 2nd prime number: "))

msg=int(input("Enter message to encrypt: "))

n=p*q
phi=(p-1)*(q-1)

# find public key to encrypt data..(e)
e=None
for  x in range(2,phi):
    if math.gcd(x,phi)==1:
        e=x
        break
# find private key to decrypt data...(d)
d=None
for x in range(1,n):
    if (x*e)%phi==1:
        d=x
        break

print("public key is :",e)
print("private key is :",d)
print("Message is :",msg)

print("------------Encrypting msg----------------")
enc= pow(msg,e)%n
print(enc)

print("------------Decrypting msg----------------")
dec= pow(enc,d)%n
print(dec)

