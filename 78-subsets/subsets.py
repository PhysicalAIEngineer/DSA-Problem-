# Brute Force & Optimal Code
class Solution:
    def __init__ (self):
        # list to stroe all possible subsets
        self.result = []
    # backtracking function to generate all subsets
    def solve(self, nums: list[int], index: int, current: list[int]):
        # if all element have been processed store the current subsets
        if index >= len(nums):
            self.result.append(current[:])
            return 
        # include the current element
        current.append(nums[index])
        # recur for the next element 
        self.solve(nums, index + 1, current)
        # backtrack by removing the last elements
        current.pop()
        # exclude the current elements
        self.solve(nums, index + 1, current)
    # return all possible subsets
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # clear any previously stored subsets
        self.result = []
        # list to bulid the current subsets
        current = []
        # start generating subsets
        self.solve(nums, 0, current)
        # return all generated subsets
        return self.result

# Time Complexity : O(N!)
# Space Complexity : O(N)