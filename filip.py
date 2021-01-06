x, y = input().split()

n = int(x)    

countn = 0 
while (n>0):
  dig = n%10
  countn = countn*10+dig
  n=n//10


m = int(y)    

countm = 0 
while (m>0):
  dig = m%10
  countm = countm*10+dig
  m=m//10


if countm < countn:
  print(countn)
else:
  print(countm)