king, queen, rooks, bishops, knights, pawns = [int(x) for x in input().split()]

if king == 1:
    k = 0
else:
    k = 1 - (king)

if queen == 1:
    q = 0
else:
    q = 1 - (queen)

if rooks == 2:
    r = 0
else:
    r = 2 - (rooks)

if bishops == 2:
    b = 0
else:
    b = 2 - (bishops)

if knights == 2:
    kn = 0
else:
    kn = 2 - (knights)

if pawns == 8:
    p = 0
else:
    p = 8 - (pawns)

print(k, q, r, b, kn, p)
