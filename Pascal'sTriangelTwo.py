class Solution():
    def ithlist(self,numrows):
        if numrows == 0 :return []
        res = [[1]]
        for i in range(1,numrows+1):
            res.append(map(lambda x,y:x+y,res[-1]+[0],[0]+res[-1]))
        return res[numrows]

tmp = Solution()
numrows = 3
res = tmp.ithlist(numrows)
print res
