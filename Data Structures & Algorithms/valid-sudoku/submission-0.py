class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowTables = [{} for i in range(9)]
        colTables = [{} for i in range(9)]
        boxTables = [{} for i in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".": continue
                if board[i][j] in rowTables[i]: 
                    print("was in rows " + str(i) + " " + str(j))
                    print(rowTables[i])
                    return False
                if board[i][j] in colTables[j]:
                    print("was in cols")
                    return False

                """
                The ordering of the boxes goes
                 0 1 2
                 3 4 5
                 6 7 8
                
                0 <= i <= 2: first row
                3 <= i <= 5: second row
                6 <= i <= 8: third row

                0 <= j <= 2: first column
                3 <= j <= 5: second column
                6 <= j <= 8: third column

                * Modulus doesn't work for this! Think of it that boxes are mapped where
                every 3 rows/columns counts as a single row/column for the box row/column.
                Therefore, use integer division to reduce all values by a factor of 3.
                """
                boxIdx = (i // 3 * 3) + (j // 3)
                
                if board[i][j] in boxTables[boxIdx]:
                    print("was in boxes " + str(i) + " " + str(j))
                    print(boxTables[boxIdx])
                    return False

                rowTables[i][board[i][j]] = True
                colTables[j][board[i][j]] = True
                boxTables[boxIdx][board[i][j]] = True
        
        return True