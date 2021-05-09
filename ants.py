# Take the number of test cases
testCases = int(input())

# For each test cases
for i in range (testCases):
  
  # Take as input the length of the pole and the quantity of ants
  lengthPole, quantityAnts = map(int,input().split())
  # Create an empty list
  ants = []

  # Take the place of where the ants are on the pole
  while len(ants) < quantityAnts:
    numAnts = list(map(int,input().split()))

    for i in range (len(numAnts)):
      ants.append(numAnts[i])

  # Create two list for the earliest possible time an ant falls off
  # and one for the latest possible time an ant falls off
  firstTime = []
  lastTime = []

  # For each ant add the distance for the right and the left of the pole
  for i in range (len(ants)):
    firstTime.append(min(ants[i],lengthPole-ants[i]))
    lastTime.append(max(ants[i],lengthPole-ants[i]))
  
  # Print out the max for both the earliest and latest time
  print(max(firstTime),max(lastTime))
