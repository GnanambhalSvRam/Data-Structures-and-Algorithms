class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        prev = curr = [1]
        rows = rowIndex + 1

        for i in range(1,rows):
            
            curr = [1]
            for j in range(len(prev)-1):
                curr.append(prev[j] + prev[j+1])
            curr.append(1)

            prev = curr

        return curr
