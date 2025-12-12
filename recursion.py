def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive call

num = int(input("Enter a number: "))

if num < 0:
    print("Invalid input")
else:
    print("Factorial =", factorial(num))
