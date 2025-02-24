class Solution:
    def reverse(self, x: int) -> int:
        
        MAX, MIN = (2 ** 31) - 1, -1 * (2 ** 31) 
        sign = -1 if x < 0 else 1
        if sign == -1:
            x = sign * x
        
        ans = 0
        while x > 0:
            ans = ans * 10 + x%10
            x = x // 10

        ans = sign * ans

        if ans > MAX or ans < MIN:
            ans = 0

        return ans
