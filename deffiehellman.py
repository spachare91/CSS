p=int(input("First public value: "))
g=int(input("Second public value: "))

#secret key for alice 
x=int(input("secret key for alice: "))

# secret key for bob
y=int(input("secret key for bob: "))

# alice will find r1 and send it to the bob
r1=pow(g,x)%p

# bob will find r2 and send it to the alice
r2=pow(g,y)%p

# then alice will find k using r2
k1=pow(r2,x)%p

# then bob will find k using r1
k2=pow(r1,y)%p

print("value of k1 is ",k1)

print("value of k2 is ",k2)

