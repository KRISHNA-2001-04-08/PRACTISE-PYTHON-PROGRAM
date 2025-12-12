a=[34,53,12,61]
#print(max(a))
b=a[0]
for i in a:
    if i>b:
        b=i
print(b)