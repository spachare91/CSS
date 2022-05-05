import math
msg="enemy attacks tonight"
msg=msg.replace(" ","")
key="20341"

arr=[]
i=0
for x in range(math.ceil(len(msg)/5)):
    arr.append(msg[i:i+5])
    i=i+5

if len(arr[-1])<5:
    for x in range(5-len(arr[-1])):
        arr[-1]+="z"


print(arr)

ans=[]
# now encrypt the block one by one using key.....
for x in arr:
    temp=""
    for y in key:
        temp+=str(x[int(y)])
    ans.append(temp)

print(ans)


