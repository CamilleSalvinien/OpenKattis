e,f,c = map(int, input().split())
count = 0

bottles = e+f

while bottles >= c:
    new = int(bottles/c)
    bottles = new + bottles%c
    count+=new

print(count)