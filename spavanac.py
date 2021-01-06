x,y = list(map(int, input().split()))

if y >= 45:
        y -= 45

else:
    if x == 0:
        x = 23
        y += 15
    else:
        x -= 1
        y += 15
print(x,y)