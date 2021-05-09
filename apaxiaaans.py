# Take as input the single name
phrase = input()

# Create a list for the shortest pssible name
short = []

# Loop through the length of the list, always add the first letter to short
for i in phrase:
    if (len(short)) == 0:
        new = i
        short.append(new)
    else:
        # if the current letter doesn't match the previous append it to the list 
        if i != new:
            short.append(i)
            new = i

# Print out the shortest possible name
print(''.join(short))
