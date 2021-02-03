num = int(input())
names = []

for i in range (num):
    role = input()
    names.append(role)

if list(names) == sorted(names):
    print("INCREASING")
elif list(names) == sorted(names, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")