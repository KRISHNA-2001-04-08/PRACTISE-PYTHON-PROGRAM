"""
a=int(input("ENTER NUMBER: "))
b=str(a)

for i in reversed(b):
     print(i,end="")
     
"""
num = int(input("Enter a number: "))

rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)
