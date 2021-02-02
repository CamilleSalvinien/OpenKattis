x = int(input())
binary = bin(x).replace("0b","")
list = list(binary)
list.reverse()

newlist = ''.join([str(elem) for elem in list])

print(int(newlist,2))

