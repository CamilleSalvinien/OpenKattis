n = int(input())
count = 0
num = 0

for i in range (n):
    x = int(input())
    num+=1
    if x == num:
        pass
    else:
        while x != num:
            print(num)
            count+=1
            num+=1
    
if count == 0:
    print("good job")
