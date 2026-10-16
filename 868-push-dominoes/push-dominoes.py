# Brute Force Code & Optimal Code
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # add sentinel dominoes at both ends to simplify handing eage cases
        s = "L" + dominoes + "R"
        # total length of the modified strings
        n = len(s)
        # list used to bulid the final answer
        result = []
        # initalize two poitner
        # left = previous non standing domino
        left = 0
        # right = next non standing domino
        right = 1
        # traverse the modified string
        while right < n:
            # skip all standing domioes
            if s[right] == ".":
                right += 1
                continue
            # number of standing dominoes between two non dot dominoes
            middle_length = right - left - 1
            # igonre the left sentinel "L" when buliding the answer
            if left > 0:
                result.append(s[left])
            # case 1: both ends push in the same direction
            if s[left] == s[right]:
                result.append(s[left] * middle_length)
            # case 2: forces move away from each other so no domino in the middle falls
            elif s[left] == "L" and s[right] == "R":
                result.append("." * middle_length)
            # case 3: forces move toward each other half fall right and half fall left and the middle one if nay stays upright
            else:
                result.append('R' * (middle_length // 2) +'.' * (middle_length % 2) +'L' * (middle_length // 2))
            # move the left pointer to the current non standing domino
            left = right
            right += 1
        # convert the result list into the final string
        return "".join(result)

# Time Complexity : O(N)
# Space Complexity : O(N)