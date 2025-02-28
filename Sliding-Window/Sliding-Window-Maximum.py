class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        heapq.heapify(heap)

        for i in range(k-1):
            heapq.heappush(heap,(-1*nums[i],i))
        
        left = 0
        result = []
        for right in range(k-1,len(nums)):
            heapq.heappush(heap,(-1*nums[right],right))
            
            while heap[0][1] < left:
                heapq.heappop(heap)

            result.append(-1*heap[0][0])
            left += 1

        return result
