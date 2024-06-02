n = 1000
sum = 0
for i in range(1,n+1):
    sum = sum + i**i

print(sum % (10**10))
