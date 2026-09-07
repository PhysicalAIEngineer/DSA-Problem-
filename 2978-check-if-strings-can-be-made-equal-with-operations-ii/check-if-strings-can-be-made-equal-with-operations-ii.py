# Brute Force Code & Optimal Code
class Solution: 
    def checkStrings(self, s1, s2): 
        # store character frequencies for even indices 0, 2, 4, 6, ...
        even = [0] * 26 
        # store character frequencies for odd indices 1, 3, 5, 7, ...
        odd = [0] * 26 
        # length of the string
        n = len(s1) 
        # check every index in both strings
        for i in range(n): 
            # if index is even
            if i % 2 == 0: 
                # add the character from s1 to the even-frequency array
                even[ord(s1[i]) - ord('a')] += 1 
                # subtract the character from s2 from the even-frequency array
                even[ord(s2[i]) - ord('a')] -= 1 
            # If index is odd
            else:  
                # add the character from s1 to the odd-frequency array
                odd[ord(s1[i]) - ord('a')] += 1 
                # subtract the character from s2 from the odd-frequency array
                odd[ord(s2[i]) - ord('a')] -= 1 
        # Check the frequency difference for every character from 'a' to 'z'
        for i in range(26): 
            # if any frequency is different s1 and s2 cannot be transformed into each other
            if even[i] != 0 or odd[i] != 0: 
                return False 
        # all even-index characters and all odd-index characters have the same frequencies
        return True

# Time Complexity : O(N)
# Space Complexity : O(N)