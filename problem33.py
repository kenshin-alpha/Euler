# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
tens = [10,20,30,40,50,60,70,80,90]
def factions(num,deno):
    return [(num%10/deno%10),(int(num/10)/int(deno/10)),(num%10/int(deno/10)),(int(num/10))/(deno%10)]
li = []
for i in range(10,100):
    for j in range(10,100):
        numerator = i
        denominator = j
        if(j not in tens):
            if(i/j < 1):
                if(numerator/denominator in factions(i,j)):
                    li.append([i,j])
print(li)
print(int(49/10)/(98%10), 49/98)