class Solution():
    def maxProfit(self,price):
        maxSum = 0
        for i in range(len(price)-1):
            maxSum = maxSum + (max(0,price[i+1]-price[i]))             
        return maxSum

tmp = Solution()
price = [7,1,5,3,6]
res = tmp.maxProfit(price)
print res
