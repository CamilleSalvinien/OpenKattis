n = int(input())
count = 0

for i in range (n):
    x = input()
    e = int(x[-1])
    a = int(x[:-1])
    
    count+= (a**e)

print(count)

