# Take the game play 
recordOfGame = input()

# Set up a counter for both teams
countA = 0
countB = 0

# Loop through the game play
for i in (recordOfGame):
    # If it is a letter, set the current team as the letter
    if i.isalpha():
      if i == "A":
        currentTeam = "A"
      else:
        currentTeam = "B"
    else:
      # Based on the current team, increment the correct counter
      if currentTeam == "A":
        countA +=1
      else:
        countB +=1

# Look at which counter is greatest, print out the team linked
# to the greatest score
if countB > countA:
  print("B")
else:
  print("A")
