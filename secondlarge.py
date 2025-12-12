a = [23, 54, 35, 63, 32]

first = a[0]
second = a[0]

for i in a:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print("First:", first)
print("Second:", second)
