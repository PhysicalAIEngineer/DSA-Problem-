# Brute Force Code & Optimal Code
class Solution:
    # return all elements of the matrix in spiral order
    def spiralOrder(self, matrix):
        # number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])
        # store the elements in spiral order
        result = []
        # matrix to keep track of already visited cells
        visited = [[False] * cols for _ in range(rows)]
        # directions in clockwise order: right, down, left, up
        directions = [
            (0, 1),   # move right
            (1, 0),   # move down
            (0, -1),  # move left
            (-1, 0)   # move up
        ]
        # current direction index
        direction = 0
        # start from the top-left corner
        row = 0
        col = 0
        # visit every cell exactly once
        for _ in range(rows * cols):
            # add the current element to the answer
            result.append(matrix[row][col])
            # mark the current cell as visited
            visited[row][col] = True
            # compute the next position
            next_row = row + directions[direction][0]
            next_col = col + directions[direction][1]
            # change direction if the next position is outside the matrix or already visited
            if (next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or visited[next_row][next_col]):
                direction = (direction + 1) % 4
                # recompute the next position using the new direction
                next_row = row + directions[direction][0]
                next_col = col + directions[direction][1]
            # move to the next cell
            row = next_row
            col = next_col
        # return the spiral traversal
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)