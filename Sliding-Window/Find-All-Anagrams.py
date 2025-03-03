class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        pmap,smap = Counter(p), {}
        left = 0
        result = []

        for right in range(len(s)):

            if s[right] in smap:
                smap[s[right]] += 1
            else:
                smap[s[right]] = 1

            if (right-left+1) > len(p): #window size exceeding
                if smap[s[left]] == 1:
                    del smap[s[left]]
                else:
                    smap[s[left]] -= 1
                left += 1

            if smap == pmap:
                result.append(left)

        return result
