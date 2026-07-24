# Brute Force Code
class Solution:
    # check whether the given Sudoku board is valid
    def isValidSudoku(self, board):
        # check every row
        for row in range(9):
            # store the digits already seen in this row
            seen = []
            for col in range(9):
                # ignore empty cells
                if board[row][col] == ".":
                    continue
                # check whether the current digit already exists
                duplicate = False
                for value in seen:
                    if value == board[row][col]:
                        duplicate = True
                        break
                # duplicate digit found
                if duplicate:
                    return False
                # store the current digit
                seen.append(board[row][col])
        # check every column
        for col in range(9):
            # store the digits already seen in this column
            seen = []
            for row in range(9):
                # ignore empty cells
                if board[row][col] == ".":
                    continue
                # check whether the current digit already exists
                duplicate = False
                for value in seen:
                    if value == board[row][col]:
                        duplicate = True
                        break
                # duplicate digit found
                if duplicate:
                    return False
                # store the current digit
                seen.append(board[row][col])
        # check every 3 × 3 sub-box
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                # store the digits already seen in this box
                seen = []
                # traverse the current 3 × 3 sub-box
                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        # ignore empty cells
                        if board[row][col] == ".":
                            continue
                        # check whether the current digit already exists
                        duplicate = False
                        for value in seen:
                            if value == board[row][col]:
                                duplicate = True
                                break
                        # duplicate digit found
                        if duplicate:
                            return False
                        # store the current digit
                        seen.append(board[row][col])
        # no duplicates found in any row column, or 3 × 3 sub-box
        return True

# Time Complexity : O(N^6)
# Space Complexity : O(N)