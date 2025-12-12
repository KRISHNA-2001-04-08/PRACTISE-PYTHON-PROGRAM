a=[29,53,46,23,87,56,32,47,34]
b=[]
c=[]
count_even=0
count_odd=0
for i in a:
    if i%2==0:
        b.append(i)
        count_even=count_even+1
    else:
        c.append(i)
        count_odd=count_odd+1
print("even:",b)
print("odd:",c)    
print(count_even)
print(count_odd)