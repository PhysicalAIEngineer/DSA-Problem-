# Brute Force Code & Optimal Code
class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        # base case: initial string contains only the character 'a'
        if k == 1:
            return 'a'
        # total number of operations
        n = len(operations)
        # current length of the string after each operation initially, the string contains only one character
        length = 1
        # store the type of the operation that creates the k-th character
        operation_type = 0
        # store the corresponding position of the k-th character in the first half of the string
        new_k = 0
        # find the first operation whose resulting string contains the k-th character
        for i in range(n):
            # each operation doubles the string length
            length *= 2
            # if the current string length is large enough the k-th character is created during this operation
            if length >= k:
                # save the operation type (0 or 1)
                operation_type = operations[i]
                # map the position in the second half back to the corresponding position in the first half
                new_k = k - (length // 2)
                # stop searching
                break
        # recursively determine the original character before the current operation was applied
        result = self.kthCharacter(new_k, operations)
        # if the operation type is 0 the copied character remains unchanged
        if operation_type == 0:
            return result
        # if the operation type is 1 increment the character by one wrap around from 'z' back to 'a'
        if result == 'z':
            return 'a'
        # return the next alphabet character
        return chr(ord(result) + 1)

# Time Complexity : O(N^2)
# Space Complexity : O(N)