# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the total number of elements in the input array.
        self.n = 0
    def backtrack(self, nums, idx, curr, result):
        # check whether the current subsequence
        # is valid subsequence is valid if it contains at least 2 elements.
        if len(curr) > 1:
            # store a copy of the current subsequence use copy() because curr will be modified later during backtracking.
            result.append(curr.copy())
        # avoid duplicate choices at this level set stores values that have already been used at the current recursion level this prevents generating the same subsequence multiple times when duplicate values exist.
        st = set()
        # try every possible next element start from idx because a subsequence must preserve the original order of elements.
        for i in range(idx, self.n):
            # choose nums[i] when:
            # 1. curr is empty nums[i] is greater than or equal to the last element of curr this ensures the subsequence is non-decreasing.
            # 2. nums[i] has not already been used at this recursion level.
            if ((not curr or nums[i] >= curr[-1])and nums[i] not in st):
                # choose nums[i] add the current number to the subsequence.
                curr.append(nums[i])
                # explore further choices move to i + 1 because cannot reuse the same array position.
                self.backtrack(nums, i + 1, curr,result)
                # backtrack remove the last element so that can try another possible choice.
                curr.pop()
                # mark this value as used at the current recursion level if the same value appears again at this level, skip it.
                st.add(nums[i])
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        # store the number of elements in nums.
        self.n = len(nums)
        # store all valid subsequences.
        result = []
        # store the subsequence currently being built.
        curr = []
        # start backtracking from index 0.
        self.backtrack(nums, 0, curr, result)
        # return all valid non-decreasing subsequences of length at least 2.
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)