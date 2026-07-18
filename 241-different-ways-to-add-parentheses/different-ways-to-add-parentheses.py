# Brute Force & Optimal Code
class Solution:
    # recursive function to compute all possible results
    def solve(self, expression: str) -> list[int]:
        # list to store every possible result for the current expression
        result = []
        # traverse every character in the expression
        for i in range(len(expression)):
            # if the current character is an operator split the expression into two parts
            if expression[i] in "+-*":
                # recursively compute all possible results for the left sub-expression
                left_results = self.solve(expression[:i])
                # recursively compute all possible results for the right sub-expression
                right_results = self.solve(expression[i + 1:])
                # combine every possible left result with every possible right result
                for left in left_results:
                    for right in right_results:
                        # apply the current operator
                        if expression[i] == "+":
                            result.append(left + right)
                        elif expression[i] == "-":
                            result.append(left - right)
                        else:  # '*'
                            result.append(left * right)
        # if no operator exists in the expression it represents a single number
        if not result:
            result.append(int(expression))
        # return all possible results for the current expression
        return result
    # return every possible result obtained by placing parentheses in different ways
    def diffWaysToCompute(self, expression: str) -> list[int]:
        # start the recursive divide-and-conquer process
        return self.solve(expression)

# Time Complexity : O(N)
# Space Complexity : O(N)