# Optimal Code
class Solution:
    # return the best hour to close the shop so that the total penalty is minimum
    def bestClosingTime(self, customers: str) -> int:
        # total number of hours
        n = len(customers)
        # prefixN[i] stores the number of 'N's in: customers[0 ... i-1] example: customers = "YYNY" prefixN = [0, 0, 0, 1, 1] prefixN[3] = 1 because customers[0:3] = "YYN" contains one 'N'.
        prefixN = [0] * (n + 1)
        # suffixY[i] stores the number of 'Y's in: customers[i ... n-1] example: customers = "YYNY" suffixY = [3, 2, 1, 1, 0] suffixY[2] = 1 because customers[2:] = "NY" contains one 'Y'.
        suffixY = [0] * (n + 1)
        # build the prefixN array traverse from left to right.
        for i in range(1, n + 1):
            # current character is customers[i - 1]
            if customers[i - 1] == 'N':
                # if it is 'N', increase the count from the previous prefix.
                prefixN[i] = prefixN[i - 1] + 1
            else:
                # if it is 'Y', the number of 'N's remains unchanged.
                prefixN[i] = prefixN[i - 1]
        # build the suffixY array traverse from right to left because suffix information depends on the next position.
        for i in range(n - 1, -1, -1):
            # if the current hour has customers
            if customers[i] == 'Y':
                # add this 'Y' to the suffix count.
                suffixY[i] = suffixY[i + 1] + 1
            else:
                # 'N' does not contribute to the closed-shop penalty.
                suffixY[i] = suffixY[i + 1]
        # store the smallest penalty found so far
        min_penalty = float("inf")
        # store the closing hour that gives the smallest penalty
        min_hour = float("inf")
        # check every possible closing hour possible closing hours are: 0, 1, 2, ..., n closing at hour i means: before i -> shop is open from i onward -> shop is closed
        for i in range(n + 1):
            # penalty when closing at hour i
            # prefixN[i]: number of 'N's while the shop is open
            # suffixY[i]: number of 'Y's while the shop is CLOSED.
            # therefore: total penalty = open 'N' penalties + closed 'Y' penalties
            curr_penalty = prefixN[i] + suffixY[i]
            # if this closing hour has a smaller penalty update the best answer using < instead of <= is important if two hours have the same minimum penalty, the earlier hour is kept.
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                min_hour = i
        # return the earliest closing hour having the minimum penalty.
        return min_hour

# Time Complexity : O(N)
# Space Complexity : O(N)