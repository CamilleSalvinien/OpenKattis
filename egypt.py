while (True):
    numbers = list(map(int, input().split()))
    numbers.sort()
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])

    if a == 0 and b == 0 and c == 0:
        break
    elif ((a**2)+(b**2)) == (c**2):
        print("right")
    else:
        print("wrong")