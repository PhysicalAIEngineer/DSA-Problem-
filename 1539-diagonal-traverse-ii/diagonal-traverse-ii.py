# Brute Force Code & Optimal Code
class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        # dictionary where:
        # key   -> diagonal number
        # value -> elements belonging to that diagonal
        diagonals = {}
        # traverse every row
        for row in range(len(nums)):
            # traverse every column in the current row nums can be a jagged 2D list, so use len(nums[row]) instead of one fixed column size.
            for col in range(len(nums[row])):
                # cells that belong to the same diagonal have the same value of row + col. therefore, these cells belong to the same diagonal.
                diagonal = row + col
                # if this diagonal does not exist yet create an empty list for it.
                if diagonal not in diagonals:
                    diagonals[diagonal] = []
                # add the current element to its diagonal
                diagonals[diagonal].append(nums[row][col])
        # store the final traversal order
        result = []
        # process diagonals from the smallest diagonal number to the largest.
        for diagonal in range(len(diagonals)):
            # reverse the elements inside the diagonal while traversing the original matrix elements are collected from top to bottom required diagonal order is from bottom to top so  reverse the list.
            diagonals[diagonal].reverse()
            # add every element from the current diagonal to the final answer.
            for value in diagonals[diagonal]:
                result.append(value)
        # return the elements in diagonal order
        return result

# Time Complexity : O(N^2)
# Space Complexity : O(N)