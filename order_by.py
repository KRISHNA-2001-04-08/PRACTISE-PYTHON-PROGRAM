a = [5, 2, 4, 1]

# Ascending Order
for i in range(4):
    for j in range(4):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print("Ascending:", a)

# Descending Order
print("Descending:", a[::-1])
