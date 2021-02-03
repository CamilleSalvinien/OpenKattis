numbers = list(map(int, input().split()))
numbers = sorted(numbers)

letters = list(input())
output = []

for i in range (len(letters)):
    if letters[i] == "A":
        output.append(numbers[0])
    elif letters[i] == "C":
        output.append(numbers[2])
    else:
        output.append(numbers[1])

print(' '.join(str(p) for p in output))