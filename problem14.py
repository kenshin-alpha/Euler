b=0
for i in range(1,1000000):
    a=[]
    a.append(i)
    p=i
    while(i!=1):
        if(i%2==0):
            i=i/2
            a.append(i)
        else:
            i=3*i+1
            a.append(i)
    if(len(a)>b):
        b=len(a)
        print b,p


