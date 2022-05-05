import hashlib

def sha1(s):
    result = hashlib.sha1(s)
    return result.hexdigest()

def md5(s):
    result = hashlib.md5(s)
    return result.hexdigest()


str=input("Enter a string to encrypt it: ")

print(sha1(str.encode()))
print(md5(str.encode()))
