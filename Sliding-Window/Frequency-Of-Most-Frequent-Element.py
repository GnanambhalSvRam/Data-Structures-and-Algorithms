class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()
        
        left, maxFreq = 0,0
        windowTotal, windowSize = 0,0

        for right in range(len(nums)):

            windowTotal += nums[right]
            windowSize += 1

            #Shrink while this condition is true
            while windowSize * nums[right] > windowTotal + k:
                windowTotal -= nums[left]
                windowSize -= 1
                left += 1

            maxFreq = max(maxFreq,windowSize)

        return maxFreq

'''
Time complexity: O(NLogN)
'''
