l = int(input())
d = int(input())
x = int(input())

list = []

for i in range (l,(d+1)):
    sum = 0
    y = int(i)
    while y > 0:
        rem = y % 10
        sum = sum + rem
        y = int(y/10)
    if sum == x:
        list.append(i)

print(list[0])
print(list[-1])