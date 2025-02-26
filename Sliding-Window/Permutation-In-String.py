class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        hm1, hm2 = {}, {}

        for char in s1:
            if char in hm1:
                hm1[char] += 1
            else:
                hm1[char] = 1

        for i in range(len(s1)):
            if s2[i] in hm2:
                hm2[s2[i]] += 1
            else:
                hm2[s2[i]] = 1

        left,right = 0,len(s1)-1

        while right < len(s2):

            if hm1 == hm2: 
                return True

            hm2[s2[left]] -= 1
            if hm2[s2[left]] == 0:
                del hm2[s2[left]]
            left = left + 1

            right = right + 1
            if right == len(s2):
                break

            if s2[right] in hm2:
                hm2[s2[right]] += 1
            else:
                hm2[s2[right]] = 1

        return False
