countA = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
countT = 0
countJ = 0
countQ = 0
countK = 0

x = input()
letters = list(x)

for i in range(len(letters)):
    if letters[i] == "A":
        countA+=1
    elif letters[i] == "2":
        count2+=1
    elif letters[i] == "3":
        count3+=1
    elif letters[i] == "4":
        count4+=1  
    elif letters[i] == "5":
        count5+=1
    elif letters[i] == "6":
        count6+=1
    elif letters[i] == "7":
        count7+=1
    elif letters[i] == "8":
        count8+=1
    elif letters[i] == "9":
        count9+=1
    elif letters[i] == "T":
        countT+=1
    elif letters[i] == "J":
        countJ+=1
    elif letters[i] == "Q":
        countQ+=1
    elif letters[i] == "K":
        countK+=1
    else:
        pass

a = [countA, count2, count3, count4, count5, count6, count7, count8, count9, countT, countJ, countQ, countK]
a.sort()

print(a[-1])