while (True):
    n = int(input())
    if n == -1:
        break
    else:
        total = 0
        previous = 0

        for i in range(n):
            a,b = map(int,input().split())
            total+=((b-previous)*a)
            previous = b
        
        print(str(total) + " miles")

