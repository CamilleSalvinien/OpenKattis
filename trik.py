move = list(input())
current = 1

for i in range(len(move)):
    if current == 1:
        if move[i]=="A":
            current = 2
        elif move[i]=="B":
            current = 1
        elif move[i] =="C":
            current = 3
    elif current == 2:
        if move[i]=="A":
            current = 1
        elif move[i]=="B":
            current = 3
        elif move[i] =="C":
            current = 2
    elif current == 3:
        if move[i]=="A":
            current = 3
        elif move[i]=="B":
            current = 2
        elif move[i] =="C":
            current = 1
    
print(current)