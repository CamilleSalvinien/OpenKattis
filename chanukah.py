p = int(input())

for i in range (p):
    K, N = map(int, input().split())
    count = N
    for x in range (1, (N+1)):
        count+=x
    print(K, count)


