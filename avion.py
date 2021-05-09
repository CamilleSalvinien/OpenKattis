# Create a list to track which rows containg FBI
rows = []

# Run through all five sentences,
# If FBI add the index+1 of the sentence
for i in range (5):
    sentence = input()
    if "FBI" in sentence:
        rows.append(i+1)
    else:
        pass

# If no sentence contains FBI print out HE GOT AWAY
# Else print out the indexes+1
if not rows:
    print("HE GOT AWAY!")
else:
    print(' '.join(map(str,rows)))
