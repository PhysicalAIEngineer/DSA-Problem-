# Brute Force Code & Optimal Code
class Solution: 
    def checkInclusion(self, s1, s2): 
        # length of s1 and s2
        n = len(s1) 
        m = len(s2) 
        # if s1 is larger than s2 its permutation cannot be present in s2
        if n > m: 
            return False 
        # frequency array for s1 frequency array for current window of s2
        s1_freq = [0] * 26 
        s2_freq = [0] * 26 
        # count frequency of every character in s1
        for i in range(n): 
            s1_freq[ord(s1[i]) - ord('a')] += 1 
        # Sliding window over s2
        i = 0  # left pointer
        j = 0  # right pointer 
        while j < m: 
            # add s2[j] to the current window
            s2_freq[ord(s2[j]) - ord('a')] += 1 
            # window size should always be n
            if j - i + 1 > n:
                # remove the leftmost character because the window became larger than n
                s2_freq[ord(s2[i]) - ord('a')] -= 1 
                i += 1 
            # if both frequency arrays are equal current window is a permutation of s1
            if s1_freq == s2_freq: 
                return True 
            # move right pointer forward
            j += 1 
        # no permutation of s1 was found in s2
        return False

# Time Complexity : O(N)
# Space Complexity : O(N)