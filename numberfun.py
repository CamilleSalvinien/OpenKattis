number = int(input())

for index in range(number): 
  x,y,z = input().split()
  x = int(x)
  y = int(y)
  z = int(z)

  if (x - y) == z:
    print("possible")
  elif(x*y) == z:
    print("possible")
  elif(x/y) == z:
    print("possible")
  elif(x+y) == z:
    print("possible")
  elif (y-x) == z:
    print("possible")
  elif(y*x) == z:
    print("possible")
  elif(y/x) == z:
    print("possible")
  elif(y+x) == z:
    print("possible")
  else:
    print("impossible")