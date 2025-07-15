class Solution():
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1:
            digits[0] += 1
            return [int(d) for d in str(digits[0])]

        digits[-1] += 1

        for i in range(len(digits)-1, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1

        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits

        return digits



obj = Solution()
obj.plusOne([9])
