class Solution():
    def RemoveElement(self,nums,val):
        index = 0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[index] = nums[i]
                index = index + 1
        return index

tmp = Solution()
nums = [2,2,3,3]
val = 3
res = tmp.RemoveElement(nums,val)
print res
