sentence = input()
sentenceList = list(sentence)

newSentence = []
count = 0

while (count < len(sentenceList)):
    if sentenceList[count] == "a" or sentenceList[count] == "e" or sentenceList[count] == "i" or sentenceList[count] == "o" or sentenceList[count] == "u":
        newSentence.append(sentenceList[count])
        count+=3
    else:
        newSentence.append(sentenceList[count])
        count+=1


print(''.join(map(str, newSentence)))