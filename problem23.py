import math
num=28123
def sumDiv(number):
    sum=1
    sqrt=int(math.sqrt(number))
    if(number==sqrt*sqrt):
        sum=sum+sqrt
        sqrt=sqrt-1
    for i in range(2,sqrt+1):
        if(number%i==0):
            sum=sum+i+(number/i)
    return sum

abundunt=[]
for i in range(2,num+1):
    if(sumDiv(i)>i):
        abundunt.append(i)
print i,len(abundunt)
sumAbundunt=[0]*(num+1)
k=0
for i in range(0,len(abundunt)):
    for j in range(i,len(abundunt)):
        k=abundunt[i]+abundunt[j]
        if(k<=num):
            sumAbundunt[k]=True
        else:
            break
    print i
sum=0
for i in range(1,num):
    if(not sumAbundunt[i]):
        sum=sum+i
    print i
print sum



