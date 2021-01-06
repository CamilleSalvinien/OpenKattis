n = int(input())
t = list(map(int, input().split()))
count = 0 

for i in t:
    if i < 0:
        count +=1
    else:
        pass

print (count)