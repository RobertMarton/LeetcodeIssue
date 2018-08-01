class Solution(object):
    def removeDuplicates(self,nums):
        if not nums :
            return 0
        index = 0 
        for  i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                pass
            else :
                index = index + 1
                nums[index] = nums[i]
        return index+1

nums = [1,1,2]
tmp = Solution()
res = tmp.removeDuplicates(nums)
print res
    
