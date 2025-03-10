class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 0:
            return 0
        
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        size = len(heap)

        while size > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            size -= 2

            if stone1 == stone2:
                continue

            heapq.heappush(heap,-abs(stone1-stone2))
            size += 1

        if size == 0:
            return 0
        return -heapq.heappop(heap)
