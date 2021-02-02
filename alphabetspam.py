sentence = input()

whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0

for i in range (len(sentence)):
    if sentence[i] == "_":
        whitespace+=1
    elif sentence[i].isupper():
        uppercase+=1
    elif sentence[i].islower():
        lowercase+=1
    else:
        symbols+=1

print("{:6f}".format(whitespace/len(sentence)))
print("{:6f}".format(lowercase/len(sentence)))
print("{:6f}".format(uppercase/len(sentence)))
print("{:6f}".format(symbols/len(sentence)))