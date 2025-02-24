class Solution:
    def convert(self, s: str, numRows: int) -> str:

        #edge cases:
        if numRows == 1:
            return s

        if numRows == 0:
            return ""

        if len(s) <= 1:
            return s
        
        res = [[] for _ in range(numRows)]
        maxes,mins = numRows, numRows-2

        def throwMaxes(index):
            for i in range(maxes):
                if (index+i) >= len(s):
                    break
                res[i].append(s[index+i])

        def throwMins(index):
            lastIndex = numRows-1
            for i in range(mins):
                if (index+i) >= len(s):
                    break
                res[lastIndex-i-1].append(s[index+i])

        ptr = 0
        wasMins = True
        while ptr < len(s):

            if wasMins:
                throwMaxes(ptr)
                ptr = ptr + maxes
                wasMins = False

            else: 
                throwMins(ptr)
                ptr = ptr + mins
                wasMins = True

        result = ""
        for row in res:
            result = result + "".join(row)

        return result
