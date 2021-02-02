n = int(input())
a = list(input().split())
numbers = []

for i in range (len(a)):
    if a[i].isnumeric() == True:
        numbers.append(int(a[i]))
    elif a[i] == "mumble":
        numbers.append(i+1)

count = 0

for i in range (len(numbers)):
    if numbers[i] == (i+1):
        pass
    else:
        count+=1

if count == 0:
    print("makes sense")
else:
    print("something is fishy")