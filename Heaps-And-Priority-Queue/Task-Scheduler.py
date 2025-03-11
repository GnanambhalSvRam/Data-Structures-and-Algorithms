class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        counter = Counter(tasks)
        for key in counter:
            heapq.heappush(heap, (-counter[key],key))
        taskIdx, countIdx = 1, 0

        nextAvailable = {task:0 for task in tasks}

        currTimer = 0

        while len(heap) > 0:
            currTimer += 1
            
            temp = []
            while len(heap) > 0:
                pair = heap[0]
                task = pair[taskIdx]
                count = -pair[countIdx]

                if nextAvailable[task] <= currTimer:
                    heapq.heappop(heap)
                    nextAvailable[task] = currTimer + n + 1
                    newCount = count - 1
                    if newCount > 0:  
                        heapq.heappush(heap,(-(newCount),task))
                    break
                
                else:
                    temp.append(heapq.heappop(heap))

            if len(temp) != 0:
                heap.extend(temp)
                heapq.heapify(heap)

        return currTimer
