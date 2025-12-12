"""a=input("ENTER WORD: ")
b=a[::-1]
if a==b:
    print("palindrome")
else:
    print("not palindrome")"""


a = input("ENTER WORD: ")
rev = ""

for i in reversed(a):
    rev = rev + i

if a == rev:
    print("palindrome")
else:
    print("not palindrome")
