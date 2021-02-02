n = int(input())
cups = {}

for i in range (n):
    a, b = input().split()

    if a.isnumeric():
        number = int(int(a)/2)
        color = b
    else:
        number = int(b)
        color = a

    cups[color]=number

for w in sorted(cups, key=cups.get, reverse=False):
    print(w)