x = int(input())
n = int(input())

count = x

for i in range (n):
    s = int(input())
    count+=(x-s)

print(count)