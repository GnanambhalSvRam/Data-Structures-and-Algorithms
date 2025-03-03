class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = set()
        left = 0
        result = 0

        for right in range(len(s)):

            if s[right] not in visited:
                visited.add(s[right])

            else:
                for i in range(left,right):
                    if s[i] == s[right]:
                        left = i+1
                        break
                    visited.discard(s[i])

            result = max(result,len(visited))

        return result
