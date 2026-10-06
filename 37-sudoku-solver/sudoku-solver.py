class Solution: 
    def solveSudoku(self, board: list[list[str]]) -> None: 
        """ 
        Do not return anything, modify board in-place instead. 
        """ 

        # Store numbers already used in each row
        rows = [set() for _ in range(9)] 

        # Store numbers already used in each column
        cols = [set() for _ in range(9)] 

        # Store numbers already used in each 3x3 box
        boxes = [set() for _ in range(9)] 

        # Store coordinates of all empty cells
        empty_cells = [] 
 
        # Step 1: Pre-populate the sets
        # and collect all empty cell coordinates
        for r in range(9): 
            for c in range(9): 

                # Get current cell value
                val = board[r][c] 

                # If cell already contains a number
                if val != '.': 

                    # Add number to its row
                    rows[r].add(val) 

                    # Add number to its column
                    cols[c].add(val) 

                    # Find the 3x3 box index
                    # Box index will be from 0 to 8
                    box_idx = (r // 3) * 3 + (c // 3) 

                    # Add number to its box
                    boxes[box_idx].add(val) 

                else: 
                    # Store the empty cell coordinates
                    empty_cells.append((r, c)) 
 
 
        # Step 2: Backtracking over pre-collected empty cells
        def backtrack(idx: int) -> bool: 

            # Base case:
            # If all empty cells are filled,
            # Sudoku is successfully solved
            if idx == len(empty_cells): 
                return True 
 
            # Get current empty cell
            r, c = empty_cells[idx] 

            # Find the 3x3 box containing this cell
            box_idx = (r // 3) * 3 + (c // 3) 
 
            # Try digits from 1 to 9
            for d in '123456789': 

                # Check whether digit is not already used
                # in the current row, column, or 3x3 box
                if d not in rows[r] and d not in cols[c] and d not in boxes[box_idx]: 

                    # Place the digit on the board
                    board[r][c] = d 

                    # Mark digit as used in the row
                    rows[r].add(d) 

                    # Mark digit as used in the column
                    cols[c].add(d) 

                    # Mark digit as used in the 3x3 box
                    boxes[box_idx].add(d) 
 
                    # Move directly to the next empty cell
                    if backtrack(idx + 1): 
                        return True 
 
                    # Backtrack:
                    # Remove the digit because this choice
                    # did not lead to a valid solution
                    board[r][c] = '.' 

                    # Remove digit from the row
                    rows[r].remove(d) 

                    # Remove digit from the column
                    cols[c].remove(d) 

                    # Remove digit from the box
                    boxes[box_idx].remove(d) 
 
            # No digit works for this cell
            return False 
 
 
        # Start backtracking from the first empty cell
        backtrack(0)