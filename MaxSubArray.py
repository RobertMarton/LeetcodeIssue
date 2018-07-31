class Solution():
    def MaxSubSum(self,nums):
        maxSum = curSum = nums[0]
        for i in range(1,len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)
            print i
        return maxSum

tmp = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
res = tmp.MaxSubSum(nums)
print res
