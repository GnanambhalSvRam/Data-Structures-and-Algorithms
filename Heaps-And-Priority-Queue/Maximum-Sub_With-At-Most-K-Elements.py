class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        
        n,m = len(grid), len(grid[0])
        result = 0
        main_heap = []
        heapq.heapify(main_heap)

        for i in range(n):
            sub_heap = []
            heapq.heapify(sub_heap)
            row = grid[i]

            for element in row:
                heapq.heappush(sub_heap,element)
                if len(sub_heap) > limits[i]:
                    heapq.heappop(sub_heap)

            while sub_heap:
                heapq.heappush(main_heap, heapq.heappop(sub_heap))
                if len(main_heap) > k:
                    heapq.heappop(main_heap)

        while main_heap:
            result += heapq.heappop(main_heap)

        return result
