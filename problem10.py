a=[2]
h=0
for i in range(3,2000000):
    o=0
    for j in a:
        if(i%j==0):
            o=o+1
            break
    if(o==0):
        a.append(i)
        h=h+i
        print i
print h+2


