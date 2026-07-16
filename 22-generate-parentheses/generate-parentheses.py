# Brute Force Code
class Solution:
    def __init__(self):
        # list to store all valid parenthesis combinations
        self.result = []
    # check whether a generated parenthesis string is valid
    def isValid(self, string: str) -> bool:
        # variable to track the balance of parentheses
        count = 0
        # traverse every character in the string
        for ch in string:
            # opening parenthesis increases the balance
            if ch == '(':
                count += 1
            # closing parenthesis decreases the balance
            else:
                count -= 1
            # if the balance becomes negative, there are more closing brackets than opening brackets
            if count < 0:
                return False
        # string is valid only if all parentheses are balanced
        return count == 0
    # backtracking function to generate every possible parenthesis string
    def solve(self, current: list[str], n: int) -> None:
        # if the current string has length 2 * n
        if len(current) == 2 * n:
            # convert the character list into a string
            candidate = "".join(current)
            # store the string only if it is valid
            if self.isValid(candidate):
                self.result.append(candidate)
            return
        # choose an opening parenthesis
        current.append('(')
        # recur for the next position
        self.solve(current, n)
        # backtrack by removing the last character
        current.pop()
        # choose a closing parenthesis
        current.append(')')
        # recur for the next position
        self.solve(current, n)
        # backtrack by removing the last character
        current.pop()
    # return all valid parenthesis combinations
    def generateParenthesis(self,n: int) -> list[str]:
        # clear any previous results
        self.result = []
        # list to build the current combination
        current = []
        # start the backtracking process
        self.solve(current, n)
        # return all valid combinations
        return self.result

# Time Complexity : O(N!)
# Space Complexity : O(N)