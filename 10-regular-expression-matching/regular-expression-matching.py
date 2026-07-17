# Optimal Code
class Solution:
    # recursive function with memoization
    def solve(self, i: int, j: int, text: str, pattern: str) -> bool:
        # base case: if the pattern has been completely processed the text must also be completely processed for a successful match.
        if j == len(pattern):
            return i == len(text)
        # if this state has already been solved return the stored result.
        if self.dp[i][j] != -1:
            return bool(self.dp[i][j])
        # check whether the current characters match.
        # match occurs if:
        # 1. The text still has characters remaining.
        # 2. The pattern character equals the text character or the pattern contains '.' which matches any character.
        first_match = (i < len(text) and(pattern[j] == text[i] or pattern[j] == '.'))
        # if the next character in the pattern is '*' there are two possible choices:
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            ans = (
                # option 1: ignore the current character and '*' treat it as appearing zero times
                self.solve(i, j + 2, text, pattern) or
                # option 2: if the current characters match consume one character from the text while keeping the same pattern because '*' can represent multiple occurrences.
                (first_match and self.solve(i + 1, j, text, pattern))
            )
        else:
            # normal character match: both the current text and pattern characters must match, then continue with the next characters.
            ans = (first_match and self.solve(i + 1, j + 1, text, pattern))
        # store the computed result in the memoization table to avoid solving the same state again.
        self.dp[i][j] = 1 if ans else 0
        # return whether the remaining text matches the remaining pattern.
        return ans
    # main function
    def isMatch(self, text: str, pattern: str) -> bool:
        # create the memoization table. dp[i][j] stores whether text[i:] matches pattern[j:].
        # -1 = not computed
        #  0 = False
        #  1 = True
        self.dp = [[-1] * 21 for _ in range(21)]
        # start matching from the beginning of both the text and the pattern.
        return self.solve(0, 0, text, pattern)

# Time Complexity : O(N!)
# Space Complexity : O(N)