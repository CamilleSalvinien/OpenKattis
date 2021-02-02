n = int(input())

for i in range(n):
    b, p = input().split()
    BPM = (60*int(b)/float(p))
    diff = (60/float(p))
    minABPM = BPM - diff
    maxABPM = BPM + diff
    print("{:.4f}".format(minABPM), "{:.4f}".format(BPM), "{:.4f}".format(maxABPM))
