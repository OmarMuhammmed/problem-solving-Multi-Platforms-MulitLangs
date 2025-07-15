# https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        arr = [] 
        for current in range(len(nums)):
            total += nums[current]
            arr.append(total)

        return arr    

obj = Solution()
obj.runningSum([1,2,3,4])    
