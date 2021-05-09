# Take the name as input 
name = input()

# Create a list to track the uppercase letters
upperCaseOnly = []

# For each letter in the name
for letter in name:
    # If they are uppercase add it to the upperCaseOnly list
    if (letter.isupper()) == True:
        upperCaseOnly.append(letter)

# Print out the uppercase letters
print("".join(upperCaseOnly))
