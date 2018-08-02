class Solution():
    def maxProfit(self,price):
        curSum = maxSum = 0
        for i in range(1,len(price)):
            curSum = max(0, curSum+price[i]-price[i-1])
            maxSum = max(curSum,maxSum)
        return maxSum

tmp = Solution()
price = [7,1,5,3,6,4]
res = tmp.maxProfit(price)
print res
