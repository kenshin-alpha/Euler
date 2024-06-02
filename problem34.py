# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
fact = [1,1,2,6,24,120,720,5040,40320,362880]

def div(num):
    temp = str(num)
    sum = 0
    for i in temp:
        sum = sum + fact[int(i)]
    return sum



result = 0
for i in range(3,10000000):
    if(i == div(i)):
        result = result + i
        print(i)
print(result)