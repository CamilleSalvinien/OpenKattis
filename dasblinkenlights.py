x, y, z = (int(i) for i in input().split())

flag = False

if(x>y):
    max = x
    min = y
else:
    max = y
    min = x

for i in range (1,z+1):
    if(max*i > z):
        break
    if (max*i)%min == 0:
        flag = True
        break

if (flag):
    print("yes")
else:
    print("no")
