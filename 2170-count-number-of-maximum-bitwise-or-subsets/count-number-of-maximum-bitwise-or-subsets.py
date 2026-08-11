# Optimal Code
class Solution:
    # recursive function with memoization
    # 1. idx     : current index in nums
    # 2. curror  : bitwise OR of elements selected so far
    # 3. nums    : input array
    # 4. maxor   : maximum possible OR
    # 5. t       : DP/memoization table
    def countSubsets(self, idx, curror, nums, maxor, t):
        # base case: all elements have been processed.
        if idx == len(nums):
            # if current OR equals maximum OR this is one valid subset.
            if curror == maxor:
                return 1
            # otherwise, this subset is invalid.
            return 0
        # check whether this state has already been calculated.
        if t[idx][curror] != -1:
            return t[idx][curror]
        # choice 1: include nums[idx] in the subset.
        takeCount = self.countSubsets(idx + 1, curror | nums[idx], nums, maxor, t)
        # choice 2: do not include nums[idx].
        notTakeCount = self.countSubsets(idx + 1, curror, nums, maxor, t)
        # combine both choice total number of valid subset is : subset that take nums[idx] + subset that do not take nums[idx]
        t[idx][curror] = takeCount + notTakeCount
        # return the calcualted answer for this (idx, curror) state
        return t[idx][curror]
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # find the maximum possible OR the maximum OR is the OR of all elements.
        maxor = 0
        # calculate or all element
        for num in nums:
            maxor |= num
        # number of elements.
        n = len(nums)
        # DP table:
        # t[idx][curror]
        # idx     -> current position
        # curror  -> OR obtained so far
        # -1 means the state has not been calculated yet.
        t = [[-1] * (maxor + 1) for _ in range(n + 1)]
        # initially no elements have been selected so current OR is 0.
        curror = 0
        # start recursion from index 0.
        return self.countSubsets(0, curror, nums, maxor, t)

# Time Complexity : O(N)
# Space Complexity : O(N)