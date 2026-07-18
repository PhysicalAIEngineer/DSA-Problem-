# Brute Force Code & Optimal Code
class Solution:
    # recursive function to generate numbers in lexicographical order
    def solve(self, current: int, n: int, result: list[int]) -> None:
        # stop if the current number exceeds n
        if current > n:
            return
        # add the current number to the result
        result.append(current)
        # try appending digits from 0 to 9
        for next_digit in range(10):
            next_num = current * 10 + next_digit
            # no need to continue if the number exceeds n
            if next_num > n:
                return
            # recur for the next lexicographical number
            self.solve(next_num, n, result)
    # return numbers from 1 to n in lexicographical order
    def lexicalOrder(self, n: int) -> list[int]:
        result = []
        # start DFS from each leading digit (1 to 9)
        for num in range(1, 10):
            self.solve(num, n, result)
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)