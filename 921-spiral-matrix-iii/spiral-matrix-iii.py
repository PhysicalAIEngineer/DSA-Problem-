# Brute Force Code & Optimal Code
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rstart: int, cstart: int) -> List[List[int]]:
        # four movement directions in clockwise order:
        # 1. 0 -> east (right)
        # 2. 1 -> south (down)
        # 3. 2 -> west (left)
        # 4. 3 -> north (up)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # store all cells that are inside the matrix and are visited during the spiral traversal
        result = []
        # number of steps of move in the current direction
        step = 0
        # start with the east direction
        direction = 0
        # starting position is always the fisrt cell in the spiral
        result.append([rstart, cstart])
        # continue moving until every cell in the matrix has been added to the result
        while len(result) < rows * cols:
            # increase the steop count before moving in east and west directions for spiral follows this pattern:
            # 1. east -> 1 step
            # 2. south -> 1 step
            # 3. west -> 2 step
            # 4. north -> 2 step
            # 5. east -> 3 step
            # 6. south -> 3 step
            # 7. west -> 4 step
            # 8. north -> 4 step
            # therefore the step count increases after every two directions
            if direction == 0 or direction == 2:
                step += 1
            # move the required number of steps in the current direction
            for _ in range(step):
                # move the current position by one cell
                rstart += directions[direction][0]
                cstart += directions[direction][1]
                # spiral can temporarily move outside the matrix boundaries only stores position that are actutally inside the matrix
                if (0 <= rstart < rows and 0 <= cstart < cols):
                    result.append([rstart, cstart])
            # change direction clockwise
            # 1. east -> south
            # 2. south -> west
            # 3. west -> north
            # 4. north -> east
            # %4 brings the direction back to 0 after reaching direction 3
            direction = (direction + 1) % 4
        # return all matrix cells in spiral order
        return result 

# Time Complexity : O(N^2)
# Space Complexity : O(N)