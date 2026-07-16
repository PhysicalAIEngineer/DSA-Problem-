# Optimal Codd
class Solution:
    def __init__(self):
        # list to store all possible permutations
        self.result = []
        # total number of elements in the array
        self.n = 0
    # backtracking function to generate all permutations using in-place swapping
    def solve(self, index: int, nums: list[int]) -> None:
        # if every position has been fixed store a copy of the current permutation
        if index == self.n:
            self.result.append(nums[:])
            return
        # try placing every remaining element at the current position
        for i in range(index, self.n):
            # swap the current element into the current position
            nums[index], nums[i] = (nums[i], nums[index])
            # Recur to fix the next position
            self.solve(index + 1, nums)
            # backtrack by restoring the original order
            nums[index], nums[i] = (nums[i], nums[index])
    # return all possible permutations
    def permute(self, nums: list[int]) -> list[list[int]]:
        # clear any previous stored permutations
        self.result = []
        # store the total number of elements
        self.n = len(nums)
        # start generating permutations from the first position
        self.solve(0,nums)
        # return all generated permutations
        return self.result

# Time Complexity : O(N!)
# Space Complexity : O(N)
