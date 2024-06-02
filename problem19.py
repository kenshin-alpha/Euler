j=2
s=0
for x in range(1901,2001):
    if(x%4!=0):
        a=[31,28,31,30,31,30,31,31,30,31,30,31]
        for i in a:
            j=j+i
            if(j%7==0):
                s=s+1
    else:
        a=[31,29,31,30,31,30,31,31,30,31,30,31]
        for i in a:
            j=j+i
            if(j%7==0):
                s=s+1
print s

