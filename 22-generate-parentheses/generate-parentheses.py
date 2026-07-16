# Optimal Code
class Solution:
    def __init__(self):
        # list to store all valid parenthesis combinations
        self.result = []
    # backtracking function to generate valid parenthesis combinations
    def solve(self, n: int, current: str, open_count: int,close_count: int) -> None:
        # if the current string contains 2 * n characters, store it as a valid answer
        if len(current) == 2 * n:
            self.result.append(current)
            return
        # add an opening parenthesis if there are still opening brackets available
        if open_count < n:
            self.solve(n, current + '(', open_count + 1,close_count)
        # add a closing parenthesis only if it does not make the string invalid
        if close_count < open_count:
            self.solve(n, current + ')', open_count, close_count + 1)
    # generate all valid parenthesis combinations
    def generateParenthesis(self, n: int) -> list[str]:
        # clear any previous results
        self.result = []
        # start backtracking with an empty string and zero opening and closing parentheses
        self.solve(n, "", 0, 0)
        # return all valid combinations
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)