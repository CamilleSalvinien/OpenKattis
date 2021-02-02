n = int(input())
count = 0
days = []

for i in range (n):
    s, t = map(int, input().split())

    for x in range (s, (t+1)):
        if x in days:
            pass
        else:
            days.append(x)
            count+=1
    
print(count)
