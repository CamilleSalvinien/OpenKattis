# Take the number of bats and bat scores as in put
numOfBats = int(input())
bats = [int(y) for y in input().split()]  

# Create two counts, one to count the sum of all bats (not walks)
# and the count of bats (not walks)
countSum = 0
countBat = 0

# Increment the counters if the integer is greater or equal to 0
for i in range (len(bats)):
    if bats[i] >= 0:
        countSum += int(bats[i])
        countBat += 1

# Print the ratio of the sum of bats divided by the number of bats
print(countSum/countBat) 
