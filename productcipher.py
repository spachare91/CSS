msg=input("Enter string to encrypt: ")

s=4

ans=""

for x in msg:
    if(x.isupper()):
        ans+=chr((ord(x)-65+s)%26 +65)

    else:
        ans+=chr((ord(x)-97 + s)%26 + 97)

print("value is : ",ans)
