class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.bigHeap = []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.smallHeap, -1*num) #inserting into the max-heap

        #check if all the elements in the smaller heap is smaller than the bigger one
        if self.smallHeap and self.bigHeap and ((-1*self.smallHeap[0]) > self.bigHeap[0]):
            element = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.bigHeap,element)
        
        #check if both the heaps do not differ by 1 in their lengths
        if len(self.smallHeap) > len(self.bigHeap) + 1:
            element = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.bigHeap,element)

        if len(self.bigHeap) > len(self.smallHeap) + 1:
            element = heapq.heappop(self.bigHeap)
            heapq.heappush(self.smallHeap, -1*element)

    def findMedian(self) -> float:
        
        if len(self.smallHeap) == len(self.bigHeap): 
            return (-1*self.smallHeap[0] + self.bigHeap[0])/2
        elif len(self.smallHeap) > len(self.bigHeap):
            return -1*self.smallHeap[0]
        return self.bigHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
