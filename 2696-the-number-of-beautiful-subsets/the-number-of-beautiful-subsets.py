# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the total number of valid subsets found.
        self.result = 0
        # store the value of k.
        self.K = 0
    def dfs(self, nums, idx, mp):
        # base case : if have processed all elements the current subset is one valid subset.
        if idx == len(nums):
            # count this subset.
            self.result += 1
            return
        # do not take nums[idx] skip the current number and move to the next index.
        self.dfs(nums, idx + 1, mp)
        # take nums[idx] number can be added to the current subset only if: nums[idx] - K is not present and nums[idx] + K is not present absolute difference between any two selected numbers is not K.
        if (mp.get(nums[idx] - self.K, 0) == 0 and mp.get(nums[idx] + self.K, 0) == 0):
            # add nums[idx] to the current subset store its frequency in the hashmap.
            mp[nums[idx]] = mp.get(nums[idx], 0) + 1
            # recursively process the remaining elements.
            self.dfs(nums, idx + 1, mp)
            # backtracking remove nums[idx] from the current subset before trying another choice.
            mp[nums[idx]] -= 1
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        # reset the result in case the same solution object is used again.
        self.result = 0
        # store k so that dfs() can access it.
        self.K = k
        # hashmap storing the frequency of each number currently selected in the subset.
        mp = {}
        # start DFS from the first element.
        self.dfs(nums, 0, mp)
        # DFS also counts the empty subset problem asks for no empty subsets, so remove the empty subset from the answer.
        return self.result - 1

# Time Complexity : O(N)
# Space Complexity : O(N)