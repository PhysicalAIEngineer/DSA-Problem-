# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the length of the string.
        self.n = 0
    def isPalindrome(self, s, l, r):
        # check whether s[l...r] is a palindrome
        # use two pointers:
        # l -> starts from the left
        # r -> starts from the right
        # move both pointers toward the center.
        while l < r:
            # if the characters on the two sides are different, the substring is not a palindrome.
            if s[l] != s[r]:
                return False
            # move the left pointer toward the center.
            l += 1
            # move the right pointer toward the center.
            r -= 1
        # all corresponding characters matched so the substring is a palindrome.
        return True
    def backtrack(self, s, idx, curr, result):
        # base case: if idx reaches the end of the string the entire string has been partitioned.
        if idx == self.n:
            # store a copy of the current partition copy() is necessary because curr will be modified later during backtracking.
            result.append(curr.copy())
            return
        # try every possible ending position current substring starts at idx try ending it at: idx, idx + 1, idx + 2, ..., n - 1
        for i in range(idx, self.n):
            # check whether s[idx...i] is a palindrome only palindrome substrings can be included in the current partition.
            if self.isPalindrome(s, idx, i):
                # choose the palindrome substring
                curr.append(s[idx:i + 1])
                # explore the remaining string next substring must start from i + 1 because s[idx...i] has already been selected.
                self.backtrack(s, i + 1, curr, result)
                # backtrack remove the last selected substring so that we can try another partition.
                curr.pop()
    def partition(self, s: str) -> list[list[str]]:
        # store the length of the string.
        self.n = len(s)
        # store all valid palindrome partitions.
        result = []
        # store the current partition being constructed.
        curr = []
        # start backtracking from index 0.
        self.backtrack(s, 0, curr, result)
        # return all possible palindrome partitions.
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)