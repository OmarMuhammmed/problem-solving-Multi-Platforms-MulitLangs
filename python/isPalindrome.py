# leetCode -> https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        filtered = "".join([c for c in s if c.isalnum()])
        return filtered == filtered[::-1]     

        