# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the number of elements in nums.
        self.n = 0
        # memoization table t[target][idx] stores the number of ways to form 'target' starting from index 'idx'.
        self.t = []
    def solve(self, idx, nums, target):
        # base case: target becomes 0 have successfully formed the required target, so this represents one valid combination.
        if target == 0:
            return 1
        # Invalid case if we have gone beyond the array there are no more numbers to choose if target becomes negative the current combination has exceeded the required target.
        if idx >= self.n or target < 0:
            return 0
        # check memoization table if this state has already been calculated return the stored answer instead of solving the same state again.
        if self.t[target][idx] != -1:
            return self.t[target][idx]
        # store the total number of valid combinations found for the current state.
        result = 0
        # try every possible number can choose any number from idx to n - 1 as the next element of the combination.
        for i in range(idx, self.n):
            # choose nums[i] subtract nums[i] from the remaining target start again from index 0 because:
            # 1. numbers can be used multiple times.
            # 2. order matters.
            take_i = self.solve(0, nums, target - nums[i])
            # add the number of valid combinations obtained by choosing nums[i].
            result += take_i
        # store the answer for the current state so that it can be reused later.
        self.t[target][idx] = result
        # return the number of valid combinations.
        return result
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # store the number of elements in nums.
        self.n = len(nums)
        # create the memoization table.
        # 1. rows represent the remaining target.
        # 2. columns represent the current index.
        # -1 means this state has not been calculated yet.
        self.t = [[-1] * self.n for _ in range(target + 1)]
        # start the recursive process with:
        # idx = 0 --> use every number.
        # target = target need to form the complete target.
        return self.solve(0, nums, target)

# Time Complexity : O(N)
# Space Complexity : O(N)