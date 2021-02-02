n = int(input())

for i in range (n):
    x = int(input())
    current = 1

    for i in range (0,(x-1)):
        current = current*2 +1
        
    print(current)