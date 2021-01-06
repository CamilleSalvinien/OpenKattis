x, y, z = (int(i) for i in input().split())

if y < (x/2):
    y = x-y
else:
    y = y

if z < (x/2):
    z = x-z
else:
    z = z

print(y*z*4)