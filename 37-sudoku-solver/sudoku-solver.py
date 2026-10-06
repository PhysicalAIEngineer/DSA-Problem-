# Brute Force Code & Optimal Code
class Solution:
    def solveSudoku(self, board: list[list[str]]):
        # track filled numbers in each row and col in 3 * 3 box 
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        # pre populate the sets and collect all empty cell coorinates
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)
                else:
                    empty_cells.append((r, c))
        # backtracking over pre collected empty cells
        def backtrack(idx: int):
            # base case all empty cells filled sucessfully
            if idx == len(empty_cells):
                return True
            r, c = empty_cells[idx]
            box_idx = (r // 3) * 3 + (c // 3)
            # iterate though all 9 possible 
            for d in "123456789":
                if d not in rows[r] and d not in cols[c] and d not in boxes[box_idx]:
                    # place digits
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[box_idx].add(d)
                    # move direclty to the next empty cell
                    if backtrack(idx + 1):
                        return True
                    # backtrack & undo choices
                    board[r][c] = "."
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[box_idx].remove(d)
            return False
        backtrack(0)

# Time Complexity : O(N)
# Space Complexity : O(N)