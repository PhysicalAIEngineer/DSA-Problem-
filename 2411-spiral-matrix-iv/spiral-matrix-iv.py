# Brute Force Code & Optimal Code
class Solution:
    def spiralMatrix(self, m, n, head):
        # create an m x n matrix initially fill every cell with -1 because some cells may remain empty if the linked list has fewer than m * n nodes.
        matrix = [[-1] * n for _ in range(m)]
        # direction tells us which way we are currently filling the matrix.
        # 1.  0 -> left to right
        # 2. 1 -> top to bottom
        # 3. 2 -> right to left
        # 4. 3 -> bottom to top
        direction = 0
        # four boundaries define the current outer layer.
        # 1. top   -> first available row
        # 2. down  -> last available row
        # 3. left  -> first available column
        # 4. right -> last available column
        top = 0
        down = m - 1
        left = 0
        right = n - 1
        # continue filling the matrix while there is still an unprocessed rectangular area.
        # 1. top <= down ensures that at least one row remains.
        # 2. left <= right ensures that at least one column remains.
        while top <= down and left <= right:
            # direction 0:  fill the current top row from left -> right.
            if direction == 0:
                for col in range(left, right + 1):
                    # if there are no more linked-list nodes cannot fill any more cells.
                    if head is None:
                        break
                    # put the current linked-list value into the current matrix cell.
                    matrix[top][col] = head.val
                    # move to the next linked-list node.
                    head = head.next
                # top row has now been processed so move the top boundary downward.
                top += 1
            # direction 1: fill the current right column from top -> down.
            if direction == 1:
                for row in range(top, down + 1):
                    # stop if the linked list has no more nodes.
                    if head is None:
                        break
                    # put the current linked-list value into the current matrix cell.
                    matrix[row][right] = head.val
                    # move to the next linked-list node.
                    head = head.next
                # right column has been processed so move the right boundary one step left.
                right -= 1
            # direction 2: fill the current bottom row from right -> left.
            if direction == 2:
                for col in range(right, left - 1, -1):
                    # stop if the linked list has no more nodes.
                    if head is None:
                        break
                    # put the current linked-list value into the current matrix cell.
                    matrix[down][col] = head.val
                    # move to the next linked-list node.
                    head = head.next
                # bottom row has been processed so move the bottom boundary one step upward.
                down -= 1
            # direction 3: fill the current left column from down -> top.
            if direction == 3:
                for row in range(down, top - 1, -1):
                    # stop if the linked list has no more nodes.
                    if head is None:
                        break
                    # put the current linked-list value into the current matrix cell.
                    matrix[row][left] = head.val
                    # move to the next linked-list node.
                    head = head.next
                # left column has been processed so move the left boundary one step right.
                left += 1
            # move to the next direction direction cycle: 0 -> 1 -> 2 -> 3 -> 0 -> ... using % 4 brings 4 back to 0.
            direction = (direction + 1) % 4
        # return the matrix containing the linked-list values in spiral order.
        return matrix

# Time Complexity : O(N)
# Space Complexity : O(N)