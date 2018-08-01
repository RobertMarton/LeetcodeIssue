class Solution():
    def triangle(self,numrows):
        res = [[1]]
        for i in range(1,numrows):
            res.append(map(lambda x,y:x+y, [0]+res[-1],res[-1]+[0]))
        return res

tmp = Solution()
numrows = 4
res = tmp.triangle(numrows)
print res
