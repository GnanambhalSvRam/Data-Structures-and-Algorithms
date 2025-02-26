class Solution:
    def minFlips(self, s: str) -> int:
        
        s = s + s
        left,right = 0,0

        alt1, alt2 = "", ""
        for i in range(len(s)):
            if i % 2 == 0:
                alt1 = alt1 + "1"
                alt2 = alt2 + "0"
            else:
                alt1 = alt1 + "0"
                alt2 = alt2 + "1"

        result = len(s)
        diff1,diff2 = 0,0
        left = 0

        for right in range(len(s)):
            if s[right] != alt1[right]:
                diff1 += 1
            if s[right] != alt2[right]:
                diff2 += 1

            if (right-left+1) > len(s)//2:
                if s[left] != alt1[left]:
                    diff1 -= 1
                if s[left] != alt2[left]:
                    diff2 -= 1
                left += 1

            if (right-left+1) == len(s)//2:
                result = min(result, diff1, diff2)

        return result
