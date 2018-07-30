class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while(right >= left):
            mid = (left+right)/2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

tmp = Solution()
nums = [1,3,5,6]
val = 2
res = tmp.searchInsert(nums,val)
print res
