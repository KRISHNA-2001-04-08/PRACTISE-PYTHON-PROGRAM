numbers = [1, 2, 4, 6, 7]

m = []

for i in range(min(numbers), max(numbers) + 1):
    if i not in numbers:
        m.append(i)

print("Missing numbers:", m)
