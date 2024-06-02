a = 0
b = 1
c = a + b
sum = 0
while(c < 4000000):
    if(c%2 == 0):
        sum = sum + c
    a = b
    b = c
    c = a + b
print(sum)