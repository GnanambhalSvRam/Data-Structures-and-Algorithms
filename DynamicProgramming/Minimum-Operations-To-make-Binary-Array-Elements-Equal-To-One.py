class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def isWindowComplete(left,right):
            
            for i in range(left, right+1):
                if nums[i] == 0:
                    return False
            return True

        count = 0
        left, right = 0, 2

        while right < len(nums):

            if nums[left] == 0:
                for i in range(left,right+1):
                    nums[i] = nums[i] ^ 1 #flip the numbers in the window
                count += 1

            left += 1
            right += 1

        if isWindowComplete(left,len(nums)-1):
            return count
        return -1
