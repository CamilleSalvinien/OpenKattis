import math
A, B, C, D = map(int, input().split())
s = ((A+B+C+D)/2)
print(round(math.sqrt((s-A)*(s-B)*(s-C)*(s-D)),6))
