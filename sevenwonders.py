cards = list(input())
countT = 0
countC = 0
countG = 0

specialList = []

for i in range(len(cards)):
    if cards[i] == 'T':
        countT+=1
    elif cards[i] == 'C':
        countC+=1
    elif cards[i] == 'G':
        countG+=1
    else:
        pass

specialList.append(countC)
specialList.append(countT)
specialList.append(countG)
special = min(specialList)


totalCards=((int(countT)**2) + (int(countC)**2) + (int(countG)**2) + (special*7))

print(totalCards)
