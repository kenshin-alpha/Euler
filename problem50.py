def prime_eratosthenes(n):
    prime_list = []
    primes = []
    for i in range(2, n+1):
        if i not in prime_list:
            primes.append(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)

    return primes
    




primes = prime_eratosthenes(1000)


print(len(primes))

num = []
for i in range(0,len(primes)):
    sum = 0
    for j in range(i,len(primes)):
        sum = sum + primes[j]
        if(sum in primes):
            count = j - i + 1
            num.append(count)
     
   
print(max(num))