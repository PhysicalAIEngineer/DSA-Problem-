# Brute Force Code & Optimal Code
class Solution:
    # recursive function to check whether the square string can be partitioned into numbers whose sum equals num
    def check(self, i: int, current_sum: int, s: str, num: int, dp: list[list[int]]) -> bool:
        # base case: if all digits have been processed return True only if the accumulated sum equals num
        if i == len(s):
            return current_sum == num
        # prune the recursion if the current sum already exceeds the target value
        if current_sum > num:
            return False
        # return the previously computed result for this state if available
        if dp[i][current_sum] != -1:
            return bool(dp[i][current_sum])
        # store whether a valid partition exists
        possible = False
        # try every possible substring starting at index i
        for j in range(i, len(s)):
            # current substring
            current_string = s[i:j + 1]
            # convert the substring into an integer
            addend = int(current_string)
            # recursively check the remaining part after adding the current number
            possible = possible or self.check(j + 1, current_sum + addend, s, num,dp)
            # if a valid partition is found memoize and return immediately
            if possible:
                dp[i][current_sum] = 1
                return True
        # memoize the result for the current state
        dp[i][current_sum] = 1 if possible else 0
        # return whether a valid partition exists
        return possible
    # return the punishment number from 1 to n
    def punishmentNumber(self, n: int) -> int:
        # store the final punishment number
        punishment_number = 0
        # check every number from 1 to n
        for num in range(1, n + 1):
            # compute the square of the current number
            square_num = num * num
            # convert the square into a string so it can be partitioned
            s = str(square_num)
            # DP table for memoization dp[index][current_sum]
            dp = [[-1] * (num + 1) for _ in range(len(s))]
            # if the square can be partitioned into numbers whose sum equals num add the square to the answer
            if self.check(0, 0, s, num, dp):
                punishment_number += square_num
        # return the total punishment number
        return punishment_number

# Time Complexity : O(N)
# Space Complexity : O(N)