n = int(input())

for i in range (n):
    g = int(input())
    guest = list(map(int,input().split()))

    duplicates = [x for x in guest if guest.count(x) == 1]
    print("Case #" + str(i+1) + ":" + " " +''.join(map(str, duplicates)))
