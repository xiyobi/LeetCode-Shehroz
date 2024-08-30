def removeDuplicates( nums):
        dc ={}
        for i in nums:
            dc[i] = nums.count(i)
        n = list((dc.keys()))
        nums = n.copy()
        return len(nums)


son = [0,0,1,1,1,2,2,3,3,4]
natija =removeDuplicates(son)            
print(natija)