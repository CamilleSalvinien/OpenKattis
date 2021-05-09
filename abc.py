# Take the input numbers and sort them
numbers = sorted(list(map(int, input().split())))

# Take the letters as input in a list
letters = list(input())

# Create a list to print out the output
output = []

# Loop for the numbers of letters given
for i in range (len(letters)):
    # If the letter is an A, append to the first place of the output list
    if letters[i] == "A":
        output.append(numbers[0])
    # If the letter is a B, append to the second place of the output list
    elif letters[i] == "B":
        output.append(numbers[1])
    # If the letter is a C, append to the third place of the output list
    elif letters[i] == "C":
        output.append(numbers[2])

# Print out the output
print(' '.join(str(j) for j in output))
