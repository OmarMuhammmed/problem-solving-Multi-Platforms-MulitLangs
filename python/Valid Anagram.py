# https://leetcode.com/problems/valid-anagram/description/

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if Counter(s) == Counter(t):
            return True
        else :
            return False
        

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        if len(s) != len(t):
            return False

        counter = {}
        # anagram
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        # nagaram
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1

        return True
