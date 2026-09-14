# Brute Force Code & Optimal Code
class Solution:
    def minimumLength(self, s: str) -> int:
        # length of the strings
        n = len(s)
        # two pointer 
        # i --> start from the left
        # j --> start from the right
        i = 0
        j = n - 1
        # continue while left and right characters are same
        while i < j and s[i] == s[j]:
            # store the common characters 
            ch = s[i]
            # remove all consecutive occurences of this characters from the left side
            while i < j and s[i] == ch:
                i += 1
            # remove all consecutive orrucences of this characters from the right side
            while j >= i and s[j] == ch:
                j -= 1
        # remaining characters from i to j give the minimum possible length
        return j - i + 1

# Time Complexity : O(N)
# Space Complexity : O(N)  