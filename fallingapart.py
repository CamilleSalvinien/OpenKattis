alice = 0
bob = 0

n = int(input())
objects = list(map(int, input().split()))
objects = sorted(objects, reverse = True)

for i in range (n):
    if i%2 == 0:
        alice+=int(objects[i])
    else:
        bob+=int(objects[i])
        
print(alice, bob)