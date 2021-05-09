# Take the input of the sentence
sentence = input()

# Create four counters for the whitespace, lowercase,
# uppercase and symbols
whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0

# Loop through each character of the sentence given
for i in range (len(sentence)):
    # Increase the counter for the relevant character
    if sentence[i] == "_":
        whitespace+=1
    elif sentence[i].isupper():
        uppercase+=1
    elif sentence[i].islower():
        lowercase+=1
    else:
        symbols+=1

# For each counter print our the ratios of the counter to the
# length of the count, to the 10**(-6)
print("{:6f}".format(whitespace/len(sentence)))
print("{:6f}".format(lowercase/len(sentence)))
print("{:6f}".format(uppercase/len(sentence)))
print("{:6f}".format(symbols/len(sentence)))
