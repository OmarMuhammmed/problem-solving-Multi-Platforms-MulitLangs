# https://leetcode.com/problems/two-sum/description/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_list = range(len(nums))
        for n in num_list : 
            for i in num_list[n+1:] :
                if nums[n] + nums[i] == target :
                    return [i, n]
            
