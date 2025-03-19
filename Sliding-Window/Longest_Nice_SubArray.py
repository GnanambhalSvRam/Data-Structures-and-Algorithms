class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        maxSoFar = 0
        left = 0
        cummulative = 0

        for right in range(len(nums)):

            current = nums[right]

            while cummulative & current != 0:
                cummulative = cummulative ^ nums[left]
                left += 1

            cummulative = cummulative | current
            maxSoFar = max(maxSoFar, right-left+1)

        return maxSoFar
