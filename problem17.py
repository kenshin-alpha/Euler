tens=[6,6,5,5,5,7,6,6]
etot=70
a=[3,3,5,4,4,3,5,5,4]
h=sum=36+etot
for i in tens:
    h=sum=sum+(10*i)+36
for i in a:
    b=i+7
    sum=sum+b
    sum=sum+((b+3)*99)+h
print sum+11

