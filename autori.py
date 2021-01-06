x = input()

list = []

for letter in x:
    if (letter.isupper()) == True:
        list.append(letter)

print("".join(list))