n = int(input())

for i in range (n):
    a = input()
    if a[0] == "P":
        print("skipped")
        pass
    if a[0].isnumeric():
        b = a.split("+")
        print(int(b[0])+int(b[-1]))
