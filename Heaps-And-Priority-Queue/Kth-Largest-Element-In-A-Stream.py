class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        self.length = 0
        heapq.heapify(self.heap)

        for num in nums:
            heapq.heappush(self.heap,num)
            self.length += 1

            if self.length > k:
                heapq.heappop(self.heap)
                self.length -= 1

    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap,val)
        self.length += 1

        if self.length > self.k:
            heapq.heappop(self.heap)
            self.length -= 1

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
