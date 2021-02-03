rows = []

for i in range (5):
    sentence = input()
    if "FBI" in sentence:
        rows.append(i+1)
    else:
        pass

if not rows:
    print("HE GOT AWAY!")
else:
    print(' '.join(map(str,rows)))