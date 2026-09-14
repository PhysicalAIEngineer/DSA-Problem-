# Brute Force Code & Optimal Code
class Solution:
    def minWindow(self, s, t):
        # length of string s
        n = len(s)
        # frequency map for characters of t
        mp = {}
        # store frequency of every character required from t
        for ch in t:
            mp[ch] = mp.get(ch, 0) + 1
        # total number of characters still required
        requiredCount = len(t)
        # sliding window pointers
        i = 0
        j = 0
        # starting index of the minimum window
        minStart = 0
        # length of the minimum valid window
        minWindow = float('inf')
        # expand the window using j
        while j < n:
            ch_j = s[j]
            # if this character is still required decrease the number of required characters
            if mp.get(ch_j, 0) > 0:
                requiredCount -= 1
            # decrease its frequency in the map negative value means we have extra copies
            mp[ch_j] = mp.get(ch_j, 0) - 1
            # if all characters of t are present try to shrink the window from the left
            while requiredCount == 0:
                # update minimum window if current window is smaller
                if minWindow > j - i + 1:
                    minWindow = j - i + 1
                    minStart = i
                # character leaving the window
                ch_i = s[i]
                # restore its frequency
                mp[ch_i] = mp.get(ch_i, 0) + 1
                # if frequency becomes positive this character is now missing from the window
                if mp[ch_i] > 0:
                    requiredCount += 1
                # move left pointer forward
                i += 1
            # move right pointer forward
            j += 1
        # if no valid window was found
        if minWindow == float('inf'):
            return ""
        # return the minimum window substring
        return s[minStart:minStart + minWindow]

# Time Complexity : O(N)
# Space Complexity : O(N)