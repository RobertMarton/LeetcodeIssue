#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print"Total %d" % Employee.empCount

    def displayEmployee(self):
        print"Name:",self.name, ",Salary:",self.salary

class Solution(object):
    def __int__(self,nums,target):
        self.nums = nums
        self.target = target
        
    def twoSum(self,nums,target):
        """
        :type nums:list[int]
        :type target:int
        :rtype: List[int]
        """

        dic = dict()
        for index,value in enumerate(nums):
            sub = target-value
            if sub in dic:
                return [dic[sub],index]
            else:
                dic[value] = index
emp1 = Employee("Napoleon",9999)
emp2 = Employee("Bonaparte",8888)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total %d" % Employee.empCount
nums = [2,7,11,15]
target = 9
res = Solution()
gg = res.twoSum(nums,target)
print gg
