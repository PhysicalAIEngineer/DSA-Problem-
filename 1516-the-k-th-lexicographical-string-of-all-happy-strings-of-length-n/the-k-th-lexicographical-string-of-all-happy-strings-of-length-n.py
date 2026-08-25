# Brute Force Code & Optimal Code
class Solution:
    def solve(self, n, curr, result):
        # base case: if the current string reaches length n,have constructed one complete happy string.
        if len(curr) == n:
            # store the completed happy string.
            result.append(curr)
            return
        # try each possible character in lexicographical order: 'a' -> 'b' -> 'c'
        for ch in "abc":
            # happy string cannot contain the same character at two consecutive positions.
            if curr and curr[-1] == ch:
                continue
            # DO / CHOOSE
            # add the current character to the string.
            curr += ch
            # EXPLORE
            # recursively choose the next character.
            self.solve(n, curr, result)
            # UNDO / BACKTRACK
            # remove the last character so that can try another possible character.
            curr = curr[:-1]
    def getHappyString(self, n: int, k: int) -> str:
        # start with an empty string.
        curr = ""
        # store all generated happy strings.
        result = []
        # generate every possible happy string of length n.
        self.solve(n, curr, result)
        # if fewer than k happy strings exist the k-th string does not exist.
        if len(result) < k:
            return ""
        # characters are tried in the order 'a', 'b', 'c' so the generated strings are already in lexicographical order k is 1-based, while Python lists are 0-based so use k - 1.
        return result[k - 1]

# Time Complexity : O(N)
# Space Complexity : O(N)