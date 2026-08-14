class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftRow, rightRow = 0, len(matrix) - 1
        midRow = rightRow // 2
        lastColumn = len(matrix[0]) - 1

        foundRow = False
        while not foundRow and leftRow <= rightRow:
            if matrix[midRow][0] <= target and matrix[midRow][lastColumn] >= target:
                foundRow = True
            else:
                if matrix[midRow][0] > target:
                    rightRow = midRow - 1
                else:
                    leftRow = midRow + 1
                midRow = (rightRow - leftRow) // 2 + leftRow
        
        if not foundRow: return False

        left, right = 0, lastColumn
        mid = right // 2
        while left <= right:
            if matrix[midRow][mid] == target: return True
            elif matrix[midRow][mid] < target: left = mid + 1
            else: right = mid - 1

            mid = (right - left) // 2 + left
        
        return False