x = input()
words = x.split(" ")
count = 0

for i in range (len(words)):
    for j in range (i+1,len(words)):
        if words[i] == words[j]:
            count+=1
            
if count == 0:
    print('yes')
else:
    print('no')