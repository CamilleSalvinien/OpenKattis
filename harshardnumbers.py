n = int(input())
if n == 0:
    n+=1

for i in range (n, 1000000001):
    if n%(sum(int(digit) for digit in str(n))) == 0:
        print(n)
        break
    else:
        pass
    n+=1







