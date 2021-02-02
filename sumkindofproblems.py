n = int(input())

for i in range (n):
    k, s = map(int, input().split())
    s1 = int(s*(s+1)/2)
    s2 = int(s**2)
    s3 = int(s*(s+1))
    
    print(k, s1, s2, s3)

