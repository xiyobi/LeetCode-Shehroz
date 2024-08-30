nums = [0,0,1]
for i in nums:
    if i == 0:
        nums.remove(i)
        nums.append(0)
print(nums)