def removeDuplicates( nums):
        son = set(nums)
        nums.clear()
        for i in son:
                nums.append(i)
        nums.sort()
        return len(nums)

son = [0,0,1,1,1,2,2,3,3,4]
natija =removeDuplicates(son)            
print(natija)
