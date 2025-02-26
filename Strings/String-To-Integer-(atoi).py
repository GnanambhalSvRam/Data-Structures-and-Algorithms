class Solution:
    def myAtoi(self, s: str) -> int:

        if len(s) == 0:
            return 0

        def removeWhiteSpaces():
            ptr = 0
            while ptr < len(s) and s[ptr] == ' ':
                ptr += 1
            return ptr
        
        def checkSign(ptr):
            sign = 1
            if s[ptr] == '-':
                sign = -1
                ptr += 1
            elif s[ptr] == '+':
                ptr += 1

            return (ptr,sign)

        def getNums(ptr,sign):

            MAX, MIN = 2**31 - 1, -1 * 2**31
            result = 0

            while (ptr < len(s)) and( s[ptr].isalpha() == False) and (s[ptr] not in ('+','-','.',' ')):
                result = result * 10 + int(s[ptr])
                ptr += 1
            
            result = sign * result
            
            if result > MAX: 
                result = MAX
            if result < MIN:
                result = MIN

            return result

        ptr = removeWhiteSpaces()
        if ptr >= len(s):
            return 0
        ptr,sign = checkSign(ptr)
        result = getNums(ptr,sign)

        return result
