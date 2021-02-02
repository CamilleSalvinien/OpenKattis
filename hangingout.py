l, x = map(int, input().split())
countCurrent = 0
skipGroup = 0

for i in range (x):
    word, amount = map(str, input().split())
    amount = int(amount)
    if i == 0:
        if amount > l:
            skipGroup+=1
        else:
            countCurrent = amount
    elif word == "enter":
        if (countCurrent+amount) > l:
            skipGroup+=1
        else:
            countCurrent+=amount
    elif word == "leave":
        countCurrent-=amount 

print(skipGroup)


    
         