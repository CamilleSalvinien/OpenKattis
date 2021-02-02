n, m = map(int, input().split())
arr=[]
frequencies = {}

for i in range (1, n+1):
    for x in range (1, m+1):
        arr.append(i+x)

def mode(arr):
    if len(arr) == 0:
        return []

for num in arr:
    frequencies[num] = frequencies.get(num,0) + 1

mode = max([value for value in frequencies.values()])

modes = []

for key in frequencies.keys():
    if frequencies[key] == mode:
        modes.append(key)

for i in range (len(modes)):
    print(modes[i])