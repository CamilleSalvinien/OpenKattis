n = int(input())
elem = input()
a_list = elem.split()
count = 0

map_object = map(int, a_list)

listInt = list(map_object)

for i in range (n):
    if listInt[i] < 0:
        count+=listInt[i]
    
print(abs(count))
