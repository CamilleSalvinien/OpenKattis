while (True):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:   
        num = int(a/b)
        remainder = int(a%b)
        print(num, remainder, "/", b)
