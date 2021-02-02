cost = float(input())
lawns = int(input())
count = 0

for i in range (lawns):
    l,w = input().split()
    l = float(l)
    w = float(w)
    count+= cost*l*w

print("{:.8f}".format(count))
