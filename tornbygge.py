n = int(input())
nums = [int(item) for item in input().split()]
count = 1

for i in range(1,len(nums)):
    if nums[i]<=nums[i-1]:
        pass
    else:
        count+=1

print(count)