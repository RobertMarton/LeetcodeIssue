class Solution():
    def ithlist(self,numRows):
        res = [1]
        for i in range(1,numRows+1):
          res =  map(lambda x,y:x+y, [0]+res,res+[0])
        return res

tmp = Solution()
numRows = 3
res = tmp.ithlist(numRows)
print res
        
