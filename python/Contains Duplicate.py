# LeetCode -> https://leetcode.com/problems/contains-duplicate/description/


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        repeted = []
        for n in nums:
            if n in repeted :
                return True
            repeted.append(n)

        return False