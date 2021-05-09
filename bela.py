# Take the input of the number of hands and the value of suits
numberOfHands, valueSuit = input().split()
numberOfHands = int(numberOfHands)
count = 0

# Loop trhough 4 times as much as number of hands
for i in range (4*numberOfHands):
    card = input()
    # Split the card as the value and the suit
    lastChar = card[-1]
    firstChar = card[0]
    
    # Adding to the counter is the card is dominant
    if lastChar == valueSuit:
        if firstChar == 'A':
            count+=11
        elif firstChar == 'K':
            count+=4
        elif firstChar == 'Q':
            count+=3
        elif firstChar == 'J':
            count+=20
        elif firstChar == 'T':
            count+=10
        elif firstChar == '9':
            count+=14
    # Adding to the counter is the card is not dominant
    if lastChar != valueSuit:
        if firstChar == 'A':
            count+=11
        elif firstChar == 'K':
            count+=4
        elif firstChar == 'Q':
            count+=3
        elif firstChar == 'J':
            count+=2
        elif firstChar == 'T':
            count+=10

# Print out the total value of the cards
print(count)
