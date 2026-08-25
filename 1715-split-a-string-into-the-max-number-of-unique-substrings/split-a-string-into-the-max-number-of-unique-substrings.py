# Brute Force Code & Optimal Code
class Solution:
    def solve(self, s, idx, st, currCount, maxCount):
        # pruning currently at index idx there are (len(s) - idx) characters remaining in the best possible case, could split every remaining character into a separate substring therefore, the maximum number of new substrings
        if currCount + (len(s) - idx) <= maxCount:
            return maxCount
        # base case: if idx reaches the end of the string the entire string has been split successfully.
        if idx == len(s):
            # update the maximum number of unique substrings found so far.
            return max(maxCount, currCount)
        # try every possible substring starting from idx, try every possible ending position j.
        for j in range(idx, len(s)):
            # create the substring from idx to j.
            sub = s[idx:j + 1]
            # choose this substring only if it has not already been used in the current partition.
            if sub not in st:
                # choose add the substring to the set of used substrings.
                st.add(sub)
                # recursively split the remaining part of the string j + 1 is the first index after the selected substring currCount + 1 because we selected one new unique substring.
                maxCount = self.solve(s, j + 1, st, currCount + 1, maxCount)
                # backtrack remove the substring so that it can be considered again in a different branch.
                st.remove(sub)
        # return the best answer found from this state.
        return maxCount
    def maxUniqueSplit(self, s: str) -> int:
        # store all substrings currently used in the current partition set provides fast lookup to check whether a substring is already present.
        st = set()
        # store the maximum number of unique substrings found so far.
        maxCount = 0
        # number of substrings selected so far.
        currCount = 0
        # start backtracking from index 0.
        maxCount = self.solve(s, 0, st, currCount, maxCount)
        # return the maximum number of unique substrings.
        return maxCount

# Time Complexity : O(N)
# Space Complexity : O(N)