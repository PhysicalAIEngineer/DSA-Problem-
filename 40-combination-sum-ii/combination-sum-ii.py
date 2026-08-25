# Brute Force Code & Optimal Code
class Solution:
    def solve(self, candidates, target, curr, result, idx):
        # if the remaining target becomes negative the current combination cannot be valid since all candidate values are positive adding more elements will only make the target smaller.
        if target < 0:
            return
        # if the remaining target becomes 0 the current combination adds up exactly to the required target.
        if target == 0:
            # store a copy of the current combination.
            result.append(curr.copy())
            return
        # try choosing every candidate starting from the current index.
        for i in range(idx, len(candidates)):
            # skip duplicate values at the same recursion level if the first 1 has already started a branch at this level, the second 1 should not start another identical branch.
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            # choose candidates[i].
            curr.append(candidates[i])
            # recursively process the remaining candidates pass i + 1 because every element can be used at most once.
            self.solve(candidates, target - candidates[i],curr, result, i + 1)
            # backtrack remove the chosen element so that can try another candidate.
            curr.pop()
    def combinationSum2(self, candidates: list[int],target: int) -> list[list[int]]:
        # sort the candidates sorting places duplicate values next to each other which allows us to easily skip duplicate branches.
        candidates.sort()
        # store all valid combinations.
        result = []
        # store the combination currently being constructed.
        curr = []
        # start backtracking from index 0.
        self.solve(candidates, target, curr, result, 0)
        # return all unique combinations whose sum is equal to target.
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)