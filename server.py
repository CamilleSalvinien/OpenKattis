n, t = map(int, input().split())
task = list(input().split())

count = t
number = 0

for i in range (len(task)):
    if int(task[i]) > count:
        break
    else:
        count-=int(task[i])
        number+=1

print(number)