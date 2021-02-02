w = int(input())
n = int(input())
count=0

for i in range (n):
    a,b = map(int, input().split())
    count+=(a*b)

print(count/w)