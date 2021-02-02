n = int(input())

for i in range (n):
    b = int(input())

    cities = []
    count = 0

    for i in range (b):
        name = input()
        if name not in cities:
            cities.append(name)
            count+=1
        else:
            pass
    
    print(count)