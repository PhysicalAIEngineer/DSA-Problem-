# Optimal Code
class Solution:
    # check whether the given sudoku board is valid
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # set to store unique identifiers for digits appearing in rows, columns, and 3 × 3 sub-boxes
        seen = set()
        # traverse every cell in the sudoku board
        for i in range(9):
            for j in range(9):
                # ignore empty cells
                if board[i][j] == ".":
                    continue
                # create unique identifiers for:
                # - current digit in the row
                row = f"{board[i][j]}_row_{i}"
                # - current digit in the column
                col = f"{board[i][j]}_col_{j}"
                # - current digit in the 3 * 3 box 
                box = f"{board[i][j]}_box_{i // 3}_{j // 3}"
                # if any identifier already exists the sudoku board violates the sudoku rules
                if row in seen or col in seen or box in seen:
                    return False
                # record that the current digit has appeared in its row, column, and 3 × 3 box
                seen.add(row)
                seen.add(col)
                seen.add(box)
        # no Sudoku rule is violated
        return True

# Time Complexity : O(N^2)
# Space Complexity : O(N)