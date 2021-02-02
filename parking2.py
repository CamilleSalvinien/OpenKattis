t = int(input())

for i in range(t):
    n = int(input())
    stores =  list(map(int,input().strip().split()))[:n] 
    minDist = (max(stores)-min(stores))*2
    print(minDist)