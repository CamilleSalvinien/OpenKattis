words = input().split()
totalCount = len(words)
countAE = 0

substring = "ae"

for i in range (len(words)):
    if (words[i].find(substring)== -1):
        pass
    else:
        countAE+=1

if (countAE/totalCount)>=(4/10):
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
