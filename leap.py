a=int(input("ENTER YEAR: "))
if (a%4==0 and a%100!=0) or a%400==0:
    print("LEAP YEAR")
else:
    print("Non Leap Year")