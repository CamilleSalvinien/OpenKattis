N = int(input())
count = 0

for i in range(N):
  word = input().lower()
  if 'pink' in word or 'rose' in word:
      count+=1

if count == 0:
  print("I must watch Star Wars with my daughter")
else:
  print(count)