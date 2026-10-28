# Brute Force Code & Optimal Code
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        # step 1 : calculate the length of both strings 
        # m = total number of characters in s1.
        # n = total number of characters in s2.
        # these lengths determine the dimensions of the memoization table and the initial recursive state.
        m = len(s1)
        n = len(s2)
        # step 2 : create the memoization table 
        # t[i][j] stores the minimum edit distance required to convert the first i characters of s1 into the first j characters of s2. table has (m + 1) rows and (n + 1) columns extra row and column represent empty prefixes initialize every cell to -1 to indicate that the corresponding state has not yet been calculated.
        self.t = [[-1] * (n + 1) for _ in range(m + 1)]
        # recursive function:
        # m = number of characters remaining in the prefix of s1.
        # n = number of characters remaining in the prefix of s2.
        # returns the minimum number of operations needed to transform s1[:m] into s2[:n].
        def solve(m, n):
            # base case : if either prefix is empty, we can no longer compare characters from both strings.
            if m == 0 or n == 0:
                # if s1's prefix is empty, insert all n characters from s2's prefix.
                # if s2's prefix is empty, delete all m characters from s1's prefix.
                # if both prefixes are empty, no operations are needed therefore, the answer is m + n.
                return m + n
            # memoization : check whether the minimum edit distance for the current state (m, n) has already been calculated if t[m][n] is not -1, return the cached answer instead of solving the same state again.
            if self.t[m][n] != -1:
                return self.t[m][n]
            # case 1 : last characters match
            # compare the last characters of the current prefixes: s1[m - 1] and s2[n - 1].
            if s1[m - 1] == s2[n - 1]:
                # since the characters are already equal do not need to insert, delete, or replace either character ignore this matching pair and solve the
                # remaining prefixes.
                self.t[m][n] = solve(m - 1, n - 1)
            else:
                # case 2 : last characters do not match
                # must perform an edit operation there are three possible choices:
                # 1. insert a character.
                # 2. delete a character.
                # 3. replace a character.
                # Each operation costs 1.
                # calculate the cost of each choice and select the operation with the minimum total cost.
                # operation 1 : insert
                # insert the last character of s2 into s1 after accounting for this character still need to convert s1[:m] into s2[:n - 1] remaining subproblem is solve(m, n - 1). add 1 for the insertion operation.
                insertC = 1 + solve(m, n - 1)
                # operation 2: delete 
                # delete the last character of s1 prefix of s1 becomes one character shorter while the prefix of s2 remains unchanged remaining subproblem is solve(m - 1, n) add 1 for the deletion operation.
                deleteC = 1 + solve(m - 1, n)
                # operation 3: replace 
                # replace the last character of s1 with the last character of s2.
                # both characters are now accounted for, so solve the remaining prefixes: solve(m - 1, n - 1) add 1 for the replacement operation.
                replaceC = 1 + solve(m - 1, n - 1)
                # choose the operation with the smallest cost store the minimum edit distance for the current state (m, n) in the memoization table.
                self.t[m][n] = min(insertC, deleteC, replaceC)
            # return the computed minimum edit distance result is cached, so any future call with the same state can reuse it.
            return self.t[m][n]
        # step 3: start the recursion
        # initially, we consider both complete strings: s1[:m] and s2[:n] return the minimum number of insertions, deletions and replacements required to transform s1 into s2.
        return solve(m, n)

# Time Complexity : O(N)
# Space Complexity : O(N)