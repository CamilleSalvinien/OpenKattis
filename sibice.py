N, W, H = map(int, input().split())

maxlength = int(((W*W)+(H*H))**0.5)

for i in range (N):
    match = int(input())
    if match <= maxlength:
        print('DA')
    else:
        print('NE')