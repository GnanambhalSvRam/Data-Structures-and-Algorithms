class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}
        left = 0
        maxInWindow = 0
        result = 0

        for right in range(len(s)):

            char = s[right]
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
            maxInWindow = max(maxInWindow,freq[char])
            windowSize = right - left + 1

            if windowSize - maxInWindow > k:
                freq[s[left]] -= 1
                left += 1

            result = max(result, right-left+1)

        return result
