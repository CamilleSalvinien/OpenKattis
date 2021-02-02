n = int(input())

for i in range (n):
    command = input().split()
    if command[0] == 'Simon' and command[1] == 'says':
        lastPhrase = command[2::]
        output = ' '.join(map(str,lastPhrase))
        print(output)