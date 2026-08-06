# Brute Force Code & Optimal Code
class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        # number of rows in the image
        m = len(img)
        # number of columns in the image
        n = len(img[0])
        # all 9 possible positions around the current cell include [0,0] because the current cell is also part of the average.
        directions = [[-1, -1], [-1, 0], [-1, 1],[0, -1],  [0, 0],  [0, 1],[1, -1],  [1, 0],  [1, 1]]
        # create the result matrix initially, every value is 0.
        result = [[0] * n for _ in range(m)]
        # visit every cell in the image
        for i in range(m):
            for j in range(n):
                # store the sum of all valid neighboring values
                total = 0
                # count how many valid cells are included
                count = 0
                # check all 9 positions around the current cell
                for direction in directions:
                    # calculate the neighboring row
                    new_i = i + direction[0]
                    # calculate the neighboring column
                    new_j = j + direction[1]
                    # check whether the neighboring cell is inside the image boundaries some cells near the edge or corner do not have all 8 neighbors.
                    if (0 <= new_i < m and 0 <= new_j < n):
                        # add the valid neighboring value
                        total += img[new_i][new_j]
                        # count this valid cell
                        count += 1
                # calculate the average of all valid cells performs integer division and removes the decimal part.
                result[i][j] = total // count
        # return the smoothed image
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)