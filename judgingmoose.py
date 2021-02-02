l, r = map(int, input().split())

if l == 0 and r == 0:
    print("Not a moose")
elif l == r:
    print ("Even" + " " + str(l*2))
elif l < r:
    print("Odd" + " " + str(r*2))
elif r < l: 
    print("Odd" + " " + str(l*2))