# Brute Force Code & Optimal Code
class Solution:
    def solve(self, i, n, result, used):
        # base case : if i reaches the end of the result array every required number has been placed successfully because always try numbers from largest to smallest, the first complete valid sequence found is the lexicographically largest sequence.
        if i >= len(result):
            return True
        # if the current position is already occupied by the second occurrence of a previous number skip this position and move forward.
        if result[i] != -1:
            return self.solve(i + 1, n, result, used)
        # try every number from largest to smallest trying larger numbers first helps us find the lexicographically largest valid sequence first.
        for num in range(n, 0, -1):
            # if this number has already been placed it cannot be used again.
            if used[num]:
                continue
            # TRY
            # mark the current number as used.
            used[num] = True
            # place the first occurrence at index i.
            result[i] = num
            # EXPLORE
            # number 1 appears only once in the sequence.
            if num == 1:
                # continue filling the next position.
                if self.solve(i + 1, n, result, used):
                    return True
            else:
                # for numbers greater than 1, the two occurrences must have exactly num positions between their indices.
                j = i + num
                # second position must:
                # 1. be inside the result array.
                # 2. be currently empty.
                if (j < len(result) and result[j] == -1):
                    # place the second occurrence of num.
                    result[j] = num
                    # continue filling the remaining positions.
                    if self.solve(i + 1, n, result, used):
                        return True
                    # backtrack remove the second occurrence because this placement did not lead to a solution.
                    result[j] = -1
            # UNDO / BACKTRACK
            # mark the number as unused so that another placement can be tried in a different branch.
            used[num] = False
            # remove the first occurrence from the current position.
            result[i] = -1
        # none of the available numbers can produce a valid sequence from this position.
        return False
    def constructDistancedSequence(self, n: int) -> list[int]:
        # required sequence contains: one occurrence of 1 & two occurrences of every number from 2 to n  initially, every position is empty and represented by -1.
        result = [-1] * (2 * n - 1)
        # used[num] tells us whether number num has already
        # been placed in the sequence size is n + 1 so that numbers can be accessed directly using their values.
        used = [False] * (n + 1)
        # start backtracking from the first position.
        self.solve(0, n, result, used)
        # return the lexicographically largest valid sequence.
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)