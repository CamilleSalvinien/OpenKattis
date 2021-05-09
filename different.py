# Import the system library
import sys

# Read the lines as they are pushed using the system library
for line in sys.stdin.readlines():
    # Take as input the two integers
    a, b = map(int, line.split())
    # Print out the absolute differnce of the two integers
    print(abs(a-b))
