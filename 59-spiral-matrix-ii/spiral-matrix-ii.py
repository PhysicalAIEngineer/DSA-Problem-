# Brute Force & Optimal Code
class Solution:
    # generate an n x n matrix filled with numbers from 1 to n² in spiral order
    def generateMatrix(self, n: int) -> list[list[int]]:
        # if n is 0, there is no matrix to create
        if n == 0:
            return []
        # create an n x n matrix initially filled with zeros
        matrix = [[0] * n for _ in range(n)]
        # define the four boundaries of the current layer
        top = 0
        down = n - 1
        left = 0
        right = n - 1
        # direction controls the current movement:
        # 0 -> left to right
        # 1 -> top to bottom
        # 2 -> right to left
        # 3 -> bottom to top
        direction = 0
        # number to be inserted into the matrix
        counter = 1
        # continue while there are unfilled cells remaining
        while top <= down and left <= right:
            # direction 0: fill the top row from left to right
            if direction == 0:
                for col in range(left, right + 1):
                    matrix[top][col] = counter
                    counter += 1
                # top row is now filled so move the top boundary down
                top += 1
            # direction 1: fill the right column from top to bottom
            elif direction == 1:
                for row in range(top, down + 1):
                    matrix[row][right] = counter
                    counter += 1
                # right column is now filled so move the right boundary left
                right -= 1
            # direction 2: fill the bottom row from right to left
            elif direction == 2:
                for col in range(right, left - 1, -1):
                    matrix[down][col] = counter
                    counter += 1
                # bottom row is now filled so move the bottom boundary up
                down -= 1
            # direction 3: fill the left column from bottom to top
            else:
                for row in range(down, top - 1, -1):
                    matrix[row][left] = counter
                    counter += 1
                # left column is now filled so move the left boundary right
                left += 1
            # move to the next direction 0 -> 1 -> 2 -> 3 -> 0
            direction = (direction + 1) % 4
        # return the completed spiral matrix
        return matrix

# Time Complexity : O(N)
# Space Complexity : O(N)