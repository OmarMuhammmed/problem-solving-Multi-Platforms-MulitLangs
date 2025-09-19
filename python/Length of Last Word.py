# https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        string = s.strip()
        print(string)
        for char in reversed(s):
            if char != ' ' :
                res+=1
            else:
                break    


        return res         
