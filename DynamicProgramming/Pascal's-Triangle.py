class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []

        output = [[1]]

        for i in range(1,numRows):
            curr_row, prev_row = [1], output[i-1]

            for i in range(len(prev_row)-1):
                curr_row.append(prev_row[i] + prev_row[i+1])

            curr_row.append(1)
            output.append(curr_row)

        return output
