import math
def sumOfFactors(number):
    sqrt=int(math.sqrt(number))
    sumi=1
    if(number==sqrt*sqrt):
        sumi=sumi+sqrt
        sqrt=sqrt-1
    for i in range(2,sqrt+1):
        if(number%i==0):
            sumi=sumi+i+(number/i)
    return sumi
sumAmicible=0
upperlimit=10000
for i in range(2,upperlimit):
    factorsi=sumOfFactors(i)
    if(factorsi>i and factorsi<=upperlimit):
        factorsj=sumOfFactors(factorsi)
        if(factorsj==i):
            sumAmicible=sumAmicible+i+factorsi
            print i,factorsi
print sumAmicible
