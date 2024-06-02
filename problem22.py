file_name = 'files/p022_names.txt'

file = open(file_name,'r')

content = file.read()

file.close()

list = content.split(",")



for i in range(len(list)):
    list[i] = list[i].strip('"')


list.sort()

result = 0

for i in range(len(list)):
    sum = 0
    for j in list[i]:
        sum = sum + ord(j) - 64
    result = result + ((i + 1) * sum)

print(result)
