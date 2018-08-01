class Solution():
    def MergeSortedArray(self,nums,m,nums2,n):
        while m>0 and n>0:
            if nums[m-1]>nums2[n-1]:
                nums[m+n-1]=nums[m-1]
                m = m - 1
            else :                
                nums[m+n-1] = nums2[n-1]
                n = n - 1
        if n>0:
            nums[:n] = nums2[:n]


