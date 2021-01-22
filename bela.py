n, b = input().split()
n = int(n)
count = 0
2
for i in range (4*n):
    c = input()
    lastChar = c[-1]
    firstChar = c[0]
    
    if lastChar == b:
        if firstChar == 'A':
            count+=11
        elif firstChar == 'K':
            count+=4
        elif firstChar == 'Q':
            count+=3
        elif firstChar == 'J':
            count+=20
        elif firstChar == 'T':
            count+=10
        elif firstChar == '9':
            count+=14
        else:
            pass
    if lastChar != b:
        if firstChar == 'A':
            count+=11
        elif firstChar == 'K':
            count+=4
        elif firstChar == 'Q':
            count+=3
        elif firstChar == 'J':
            count+=2
        elif firstChar == 'T':
            count+=10
        else:
            pass

print(count)

        