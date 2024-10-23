class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkLine(line: List[str]) -> bool:
            mySet = []
            for num in line:
                if num == '.':
                    continue
                if num in mySet:
                    return False
                mySet.append(num)
            return True

        def checkGrid(x: int, y: int) -> bool:
            mySet = []
            for i in range(x,x+3):
                for j in range(y,y+3):
                    num = board[i][j]
                    print("The current number being tested is " + str(num))
                    if num == '.':
                        continue
                    if num in mySet:
                        print(str(num) + " already in set!")
                        return False
                    mySet.append(num)
            print("Grid starting at (" + str(x) + "," + str(y) + ") has passed the check. The grid elements are: ")
            print(mySet)
            return True

        for i in range(0,9): #checking the rows
            if not checkLine(board[i]):
                return False
        print("All rows checked!")

        for i in range(9): #checking the columns
            column = [board[j][i] for j in range(9)]
            if not checkLine(column):
                return False
        print("All columns checked!")

        for x in [0,3,6]: #checking the grids
            for y in [0,3,6]:
                res = checkGrid(x, y)
                if not res:
                    return False

        return True

