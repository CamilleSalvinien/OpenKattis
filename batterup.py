x = int(input())
y = [int(y) for y in input().split()]  
list = []
count = 0

for i in range(x):
  for x in (y):
    if x>(-1):
      count +=1
      list.append(x)
      i -=1
    else:
      i -=1

print((sum(list))/count)     

list = []
count = 0