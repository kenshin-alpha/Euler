
import math

num = 987654321
def primes_natural(n):
    li = []
    for j in range(2,n+1):
        flag =True
        for i in range(2,int(math.sqrt(j)) + 1):
            if(j%i == 0):
                flag = False
                break
        if(flag):
            li.append(j)
   

    return li





def prime_eratosthenes(n):
    prime_list = []
    primes = []
    for i in range(2, n+1):
        if i not in prime_list:
            
            primes.append(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
    return primes

primes = primes_natural(num)
di = {
    1 : ['1'],
    2 : ['1','2'],
    3 : ['1','2','3'],
    4 : ['1','2','3','4'],
    5 : ['1','2','3','4','5'],
    6 : ['1','2','3','4','5','6'],
    7 : ['1','2','3','4','5','6','7'],
    8 : ['1','2','3','4','5','6','7','8'],
    9 : ['1','2','3','4','5','6','7','8','9'],
}

for i in primes:
    x = di[str(i).__len__()]
    y = list(set(str(i)))
    y.sort()
    if(x == y):
        print(i)

