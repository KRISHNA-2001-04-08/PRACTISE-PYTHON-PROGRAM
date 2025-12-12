a=[1,3,4,3,5,2,1,4,3,5]
b={}
for i in a:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
for key, value in b.items():
    print(key, ":", value)