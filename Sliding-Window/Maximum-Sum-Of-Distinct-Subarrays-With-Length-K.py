class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        def noDuplicates(hmap) -> bool:
            for val in hmap.values():
                if val > 1: 
                    return False
            return True

        freq = {num: 0 for num in set(nums)}
        total, maxSoFar = 0,0
        visited = set()

        for i in range(k-1):
            freq[nums[i]] += 1
            total = total + nums[i]
            visited.add(nums[i])

        for left,right in enumerate(range(k-1,len(nums))):

            freq[nums[right]] += 1
            total += nums[right]
            visited.add(nums[right])

            if len(visited) == k: #There are no duplicates in the current window
                maxSoFar = max(maxSoFar, total)

            total -= nums[left]
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                visited.discard(nums[left])

        return maxSoFar
