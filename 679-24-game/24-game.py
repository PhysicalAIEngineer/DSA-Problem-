# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store a small tolerance value for comparing floating-point numbers with 24.
        self.epsilon = 0.1
    def solve(self, cards):
        # base case: if only one number remains, all operations have been completed.
        if len(cards) == 1:
            # check whether the remaining value is close enough to 24.
            return abs(cards[0] - 24) <= self.epsilon
        # try every number as the first operand.
        for i in range(len(cards)):
            # try every number as the second operand.
            for j in range(len(cards)):
                # same element cannot be used twice.
                if i == j:
                    continue
                # store all numbers except cards[i] and cards[j].
                temp = []
                for k in range(len(cards)):
                    # keep numbers that were not selected.
                    if k != i and k != j:
                        temp.append(cards[k])
                # select the two numbers.
                a = cards[i]
                b = cards[j]
                # store all possible results obtained by combining a and b for addition and multiplication a op b and b op a produce the same result. for subtraction and division both orders must be considered.
                possibleVal = [a + b, a - b, b - a, a * b]
                # try a / b if b is not zero division by zero is not allowed.
                if abs(b) > 0.0:
                    possibleVal.append(a / b)
                # try b / a if a is not zero division by zero is not allowed.
                if abs(a) > 0.0:
                    possibleVal.append(b / a)
                # try every possible result of combining the selected pair.
                for val in possibleVal:
                    # DO / CHOOSE
                    # add the result of the chosen operation to the remaining numbers.
                    temp.append(val)
                    # EXPLORE
                    # recursively solve the smaller problem  two numbers have been replaced by one result, so the number of elements decreases by one.
                    if self.solve(temp):
                        # way to make 24 has been found.
                        return True
                    # UNDO / BACKTRACK
                    # remove the operation result so that another operation can be tried.
                    temp.pop()
        # if every pair and every operation has been tried and none can produce 24, return False.
        return False
    def judgePoint24(self, cards):
        # convert all integers to floating-point numbers floating-point values are needed because division may produce decimal results.
        nums = []
        for card in cards:
            nums.append(float(card))
        # start the backtracking process with all cards function returns True if some combination of operations can produce 24.
        return self.solve(nums)

# Time Complexity : O(N)
# Space Complexity : O(N)