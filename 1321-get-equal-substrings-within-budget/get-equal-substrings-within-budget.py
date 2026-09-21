# Brute Force Code & Optimal Code
class Solution: 
    def equalSubstring(self, s, t, maxCost): 
        # length of the strings
        n = len(s) 
        # maximum length of valid substring
        maxLen = 0 
        # total cost of changing s to t for the current window
        currCost = 0 
        # left and right pointers
        i = 0 
        j = 0 
        # expand window using j
        while j < n: 
            # cost to change s[j] into t[j]
            currCost += abs(ord(s[j]) - ord(t[j])) 
            # if total cost exceeds maxCost shrink the window from the left
            while currCost > maxCost: 
                # remove the cost of s[i] -> t[i]
                currCost -= abs(ord(s[i]) - ord(t[i])) 
                # move left pointer forward
                i += 1 
            # current window is valid update maximum length
            maxLen = max(maxLen, j - i + 1) 
            # move right pointer forward
            j += 1 
        # return maximum possible length
        return maxLen

# Time Complexity : O(N)
# Space Complexity : O(N)