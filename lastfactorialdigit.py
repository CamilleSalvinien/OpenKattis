n = int(input())
import math

for i in range (n):
    x = int(input())
    fact = math.factorial(x)
    fact = str(fact)
    print(fact[-1])