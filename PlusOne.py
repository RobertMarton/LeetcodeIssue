class Solution():
    def PlusOne(self,digit):
        sum = 0
        for i in digit:
            sum = sum * 10 + i
        
        return [int(x) for x in str(sum + 1)]

tmp = Solution()
digit = [1,9]
res = tmp.PlusOne(digit)
print res
