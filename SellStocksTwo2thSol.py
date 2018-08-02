class Solution():
    def maxProfit(self,price):
        return sum(max(0,price[i+1]-price[i]) for i in range(len(price)-1))

tmp = Solution()
price = [7,1,5,4,6]
res = tmp.maxProfit(price)
print res
