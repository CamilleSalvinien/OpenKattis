list = []
count = 0

for i in range (10):
    x = int(input())
    a = x%42
    if a in list:
        pass
    else:
        list.append(a)
        count+=1

print(count)