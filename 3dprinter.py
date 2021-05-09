# Number of statues needed
number = int(input())

# Create two counters
firstCount = 1
secondCount = 1

# While the first count is less than the number of statues needed
while firstCount < number:
    secondCount += 1 
    firstCount = firstCount*2

# Output the number of days to print the number of statues
print(secondCount)
