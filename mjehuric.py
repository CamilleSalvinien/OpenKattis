numbers = list(map(int,input().strip().split()))

while numbers != [1,2,3,4,5]:
    if numbers[0] > numbers[1]:
        numbers[0], numbers[1] = numbers[1], numbers[0]
        print(*numbers)
    if numbers[1] > numbers[2]:
        numbers[1], numbers[2] = numbers[2], numbers[1]
        print(*numbers)
    if numbers[2] > numbers[3]:
        numbers[2], numbers[3] = numbers[3], numbers[2]
        print(*numbers)
    if numbers[3] > numbers[4]:
        numbers[3], numbers[4] = numbers[4], numbers[3]
        print(*numbers)


    