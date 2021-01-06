n, m = (int(i) for i in input().split())

a = n-m
b = m-n

if n < m:
    if b == 1:
        print ('Dr. Chaz will have', b, 'piece of chicken left over!')
    else:
         print ('Dr. Chaz will have', b, 'pieces of chicken left over!')
  

else:
    if a == 1:
        print ('Dr. Chaz needs', a, 'more piece of chicken!')
    else:
        print ('Dr. Chaz needs', a, 'more pieces of chicken!')