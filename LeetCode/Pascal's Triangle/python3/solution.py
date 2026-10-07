class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        prev_rows = self.generate(numRows - 1)
        prev_row = prev_rows[-1]
        current_row = [1]
        for i in range(1, len(prev_row)):
            current_row.append(prev_row[i - 1] + prev_row[i])
        current_row.append(1)
        prev_rows.append(current_row)
        return prev_rows

# Given an integer numRows, return the first numRows of Pascal's triangle.

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]
