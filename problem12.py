import math
def numberOfDivisors(number):
    nod=0
    sqrt = int(math.sqrt(number))
    for i in range(1,sqrt+1):
        if(number%i==0):
            nod=nod+2
    if(sqrt*sqrt==number):
        nod=nod-1
    return nod
number = 0;
i = 1;
j = 0 
while(numberOfDivisors(number) < 500):
    number =number+ i
    i=i+1
    if(j<numberOfDivisors(number)):
        j=numberOfDivisors(number)
        print j,number
        
print(number)
