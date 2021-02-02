n = int(input())
a = int(1)

for i in range (n):
    k = list(map(int, input().split()))
    print(sum(k[1::])-k[0]+ a)