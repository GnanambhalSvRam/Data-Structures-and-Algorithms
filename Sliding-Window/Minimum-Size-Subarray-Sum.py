class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            if target <= nums[0]:
                return 1
            return 0

        left, right = 0,0
        sumSoFar = nums[0]
        result = float('inf')

        while right < len(nums):

            if sumSoFar >= target:
                noof = right - left + 1
                result = min(result,noof)

                if result == 1:
                    return result

                sumSoFar = sumSoFar - nums[left]
                left = left + 1

            else:
                if right < len(nums) - 1:
                    sumSoFar = sumSoFar + nums[right + 1]
                right = right + 1

        if result == float('inf'):
            return 0
        return result
