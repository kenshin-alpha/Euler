result = 0
resultSolutions = 0

for i in range(2,1000,2):
    numSolutions = 0
    for j in range(2,int(i/3)):
        if(i*(i-2*j) % (2*(i - j)) == 0):
            numSolutions += 1
    if(numSolutions > resultSolutions):
        resultSolutions = numSolutions
        result = i

print(result)