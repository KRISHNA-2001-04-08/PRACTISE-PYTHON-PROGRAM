a = [1,3,4,3,5,2,1,4,3,5]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)
