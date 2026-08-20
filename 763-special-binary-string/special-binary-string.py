# Brute Force Code & Optimal Code
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # list to store all top-level special substrings
        specials = []
        # starting index of the current special substring
        start = 0
        # balance counter: +1 for '1', -1 for '0'
        balance = 0
        # traverse the string to split it into top-level special substrings
        for i in range(len(s)):
            # update the balance '1' increases it, '0' decreases it
            balance += 1 if s[i] == '1' else -1
            # when the balance becomes zero a complete special substring is found
            if balance == 0:
                # extract the inner portion by removing the outermost '1' and '0'
                inner = s[start + 1:i]
                # recursively rearrange the inner substring to make it lexicographically largest then rebuild the special substring
                specials.append("1" + self.makeLargestSpecial(inner) + "0")
                # start searching for the next top-level special substring
                start = i + 1
        # arrange all top-level special substrings in descending lexicographical order
        specials.sort(reverse=True)
        # build the final largest special string
        result = ""
        for string in specials:
            result += string
        # return the lexicographically largest special binary string
        return result

# Time Complexity : O(n^2logN)
# Space Complexity : O(N)