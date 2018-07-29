class Solution(object):
    def removeDuplicates(self,nums):
        """
        :type nums:List[int]
        :type: int
        """

        if not nums:
            return 0
        index = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[index]:
                index = index + 1
                nums[index] = nums[i]

        return index + 1
tmp = Solution()
nums = [1,1,2]
res = tmp.removeDuplicates(nums)
print res
