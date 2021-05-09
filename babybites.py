# Take the number of bites and what Arild says
numOfBites = int(input())
talk = list(input().split())
# Create a list to track if the couting is correct
numbers = []

# Add the numbers, and add the index+1 if mumble
for i in range (len(talk)):
    if talk[i].isnumeric() == True:
        numbers.append(int(talk[i]))
    elif talk[i] == "mumble":
        numbers.append(i+1)

# Create a counter
count = 0

# Check if the number is equal to index+1
# Otherwise increment counter by 1
for i in range (len(numbers)):
    if numbers[i] == (i+1):
        pass
    else:
        count+=1

# If the counter is equal to 0 print out MAKES SENSE
# Else print out SOMETHING IS FISHY
if count == 0:
    print("makes sense")
else:
    print("something is fishy")
