a = int(input("ENTER NUMBER: "))

if a >= 2:
    for i in range(2, a):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)   # This runs only if the loop does NOT break
else:
    print("not prime")
