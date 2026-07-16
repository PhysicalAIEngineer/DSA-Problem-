# Brute Force Code 
class Solution:
    def __init__ (self):
        # list to store all possible permutaions
        self.result = []
        # set to keep track of element that are already included in the current permutation
        self.used = set()
        # total number of element in the array
        self.n = 0
    # backtracking function to generate all permutations
    def solve(self, current: list[int], nums: list[int]):
        # if the current permutations contains all elements store copy of its
        if len(current) == self.n:
            self.result.append(current[:])
            return 
        # try every element in the array
        for i in range(self.n):
            # skip the element if its has alredy been used
            if nums[i] not in self.used:
                # choose the currnet elements
                current.append(nums[i])
                self.used.add(nums[i])
                # recurision to bulid the remaining position
                self.solve(current, nums)
                # backtrack removing the current elements
                self.used.remove(nums[i])
                current.pop()
    # return all possible permutaions
    def permute(self, nums: list[int]):
        # clear any previous stored permutations
        self.result = []
        self.used = set()
        # list to bulid the current permutations
        self.n = len(nums)
        # list to bulid current permutaions
        current = []
        # start generating permutations
        self.solve(current, nums)
        # return all generated permutations
        return self.result

# Time Complexity : O(N!)
# Space Complexity : O(N)

