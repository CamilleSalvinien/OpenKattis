scores = {}

for i in range (1,6):
    x,y,b,a = input().split()
    x = int(x)
    y = int(y)
    b = int(b)
    a = int(a)
    total = x+y+b+a
    scores[i] = total

v = list(scores.values())
k = list(scores.keys())

print(k[v.index(max(v))] , max(v))
