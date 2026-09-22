# Brute Force Code & Optimal Code
class Solution: 
    def countKConstraintSubstrings(self, s, k): 
        # length of the string
        n = len(s) 
        # total number of valid substrings
        result = 0 
        # count of 0s and 1s in the current window
        count0 = 0 
        count1 = 0 
        # sliding window pointers
        i = 0 
        j = 0 
        # extend until the length of stirng 
        while j < n: 
            # add the current character to the window
            if s[j] == '0': 
                count0 += 1 
            else: 
                count1 += 1 
            # window is invalid only when count0 > k and count1 > k so keep shrinking from the left
            while count0 > k and count1 > k: 
                # remove s[i] from the window
                if s[i] == '0': 
                    count0 -= 1 
                else: 
                    count1 -= 1 
                # move left pointer forward
                i += 1 
            # current window [i...j] is valid number of valid substrings ending at j: j - i + 1
            result += (j - i + 1) 
            # move right pointer forward
            j += 1 
        # return total number of valid substrings
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)