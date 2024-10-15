class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[len(digits)-1] in [0,1,2,3,4,5,6,7,8]:
            digits[len(digits)-1] += 1
            return digits
        
        i = 0
        value = 0

        for digit in digits[::-1]:
            value = value + digit * 10**i
            i += 1
        value = value + 1

        res = []
        while value > 0:
            res.append(value % 10)
            value = value//10
        res.reverse()
        
        return res
